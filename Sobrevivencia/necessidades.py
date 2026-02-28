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

def bandagem(p1,parte):
    if parte == "cabeça":
        p1.aplicarEfeito("cabeçaCura",getattr(p1,"cabeça"))
        p1.removerEfeito("cabeça",getattr(p1,"cabeça"))
    elif parte == "tronco":
        p1.aplicarEfeito("troncoCura",getattr(p1,"tronco"))
        p1.removerEfeito("tronco",getattr(p1,"tronco"))
    elif parte == "braçoEsquedo":
        p1.aplicarEfeito("braçoEsquedoCura",getattr(p1,"braçoEsquedo"))
        p1.removerEfeito("braçoEsquedo",getattr(p1,"braçoEsquedo"))
    elif parte == "braçoDireito":
        p1.aplicarEfeito("braçoDireitoCura",getattr(p1,"braçoDireito"))
        p1.removerEfeito("braçoDireito",getattr(p1,"braçoDireito"))
    elif parte == "pernaDireita":
        p1.aplicarEfeito("pernaDireitaCura",getattr(p1,"pernaDireita"))
        p1.removerEfeito("pernaDireita",getattr(p1,"pernaDireita"))
    elif parte == "pernaEsquerda":
        p1.aplicarEfeito("pernaEsquerdaCura",getattr(p1,"pernaEsquerda"))
        p1.removerEfeito("pernaEsquerda",getattr(p1,"pernaEsquerda"))

