class Efeitos:
    def __init__(self, 
        sono=0, fome=0,
        sede=0,
        medo=0, panico=0, sangramento=0, adrenalina=0, dor=0,
        mal=0, alcool=0, abstinencia=0,
        infec=0, cocaina=0,
        cabeça=0, tronco=0,
        pernaDireita=0, pernaEsquerda=0,
        braçoDireito=0, braçoEsquerdo=0
    ):
        self.sono = sono
        self.fome = fome
        self.sede = sede
        self.medo = medo
        self.dor = dor
        self.panico = panico
        self.sangramento = sangramento
        self.adrenalina = adrenalina
        self.mal = mal
        self.alcool = alcool
        self.abstinencia = abstinencia
        self.infec = infec
        self.cocaina = cocaina

        # partes do corpo como efeitos individuais
        self.cabeça = cabeça
        self.tronco = tronco
        self.pernaDireita = pernaDireita
        self.pernaEsquerda = pernaEsquerda
        self.braçoDireito = braçoDireito
        self.braçoEsquerdo = braçoEsquerdo
