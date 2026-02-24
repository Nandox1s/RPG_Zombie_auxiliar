def necessidade(p1, hora, ultimaVez, necessidade, tempo):
    if ultimaVez is None:
        ultimaVez = hora  
    diferenca = (hora - ultimaVez)
    if diferenca < 0:
        diferenca += 24
    if diferenca > tempo:
        if getattr(p1, necessidade) != 2:
            p1.aplicarEfeito(necessidade, 1)
            print("Você sente", necessidade)
            return hora 
    return ultimaVez
