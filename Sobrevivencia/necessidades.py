def necessidade(p1, minutos_totais, ultimaVez, necessidade, tempo):
    if ultimaVez is None:
        return minutos_totais  

    diferenca = minutos_totais - ultimaVez

    if diferenca >= tempo:
        if getattr(p1, necessidade) != 2:
            p1.aplicarEfeito(necessidade, 1)
            print("Você sente", necessidade)
            return minutos_totais

    return ultimaVez

def atualizar_tempo(minutos_totais):
    dia = minutos_totais // 1440
    resto = minutos_totais % 1440

    hora = resto // 60
    minuto = resto % 60

    return dia, hora, minuto