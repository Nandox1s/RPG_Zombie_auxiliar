from Atributos.personagem import Personagem
from random import randint

def testeSorte(p1,dados,atributo,habilidade,nivelHabilidade,dificuldade,mod):
    teste = (dados+atributo)+((nivelHabilidade*0.01)*(dados+atributo))
    print(teste)
    if (teste-mod) >= dificuldade:
        p1.aplicarEfeito(habilidade,1)
        return "Conseguiu"
    else: 
        p1.aplicarEfeito(habilidade,1)
        return "Errou"

def testeHabilidade(p1,habilidade,nivelHabilidade,dificuldade,mod):
    if ((0.1*nivelHabilidade)-mod) >= dificuldade:
       p1.aplicarEfeito(habilidade,1)
       return "Conseguiu"
    else: 
        p1.aplicarEfeito(habilidade,1)
        return "Errou"

def testeAtributo(atributo,dificuldade,mod):
    if (atributo-mod) >= dificuldade:
       return "Conseguiu"
    else: return "Errou"

#Combate

def ferimento(p1):
        onde = randint(1, 6)
        mapa = {
            1: "cabeça",
            2: "braçoEsquerdo",
            3: "braçoDireito",
            4: "pernaDireita",
            5: "pernaEsquerda",
            6: "tronco"
        }
        parte = mapa[onde]
        p1.aplicarEfeito(parte, 1)
        print(f"Ferimento em {parte}")

def zombieAtaque(p1,mod):
    dadoZombie = randint(1,6)
    ataqueZombie = randint(1,2)
    if ataqueZombie == 1:
        print("Dado do Zombie:",dadoZombie)
        if dadoZombie > (p1.FIS-mod):
            ferimento(p1)
            return "Zombie agarrou"
        else: return "Zombie errou"
    if ataqueZombie == 2:
        print("Dado do Zombie:",dadoZombie)
        if dadoZombie > (p1.FIS-mod):
            ferimento(p1)
            return "Zombie te bateu"
        else: return "Zombie errou"        
    
def zombieLutar(p1, dado, mod, zombieFIS):
    dadoZombie = randint(1,6)
    print("Dado do Zombie:",dadoZombie)
    if (dado+p1.FIS)-mod > (zombieFIS+dadoZombie):
        return "Você derrubou ele"
    else: 
        ferimento(p1)
        p1.aplicarEfeito("sangramento",1)
        p1.aplicarEfeito("infec",1)
        return "Ele te mordeu"

def zombieFugir(p1, dado, mod):
    if (dado+p1.FIS)-mod > 4:
        ferimento(p1)
        return "Você fugiu"
    else: 
        ferimento(p1)
        p1.aplicarEfeito("sangramento",1)
        p1.aplicarEfeito("infec",1)
        return "Ele te mordeu"

def desarmado(p1,dado,mod):
    teste = (dado+p1.FIS)+((dado+p1.desarmado)*(p1.desarmado*0.1))-mod
    print(teste)
    p1.aplicarEfeito("desarmado",1)
    

    if dado == 1:
        return "Erro Critico"
    elif (teste < 4):
        return "Errou"
    elif (teste >= 4) and (teste < 6): 
        return "tronco"
    elif teste >= 6:
        return "cabeça"

def armasBrancas(p1,arma,dado,mod):
    teste1 = dado+p1.FIS
    teste = teste1+((p1.armas_brancas*0.01)*teste1)-mod
    print(teste)
    p1.aplicarEfeito("armas_brancas",1)
    p1.removerItem(arma,1)
    
    if teste < 6:
        return "Errou"
    elif teste >= 6 and teste < 8:
        return "Tronco"
    elif teste >= 8 and teste < 10:
        return "Braços ou Pernas"
    elif teste >= 10:
        return "Cabeça"

def armasFogo(p1,arma, municao, alvos, mod):
    p1.removerItem(arma, municao)
    p1.aplicarEfeito("armas_de_fogo",1)
    for i in range(municao):
        for z in range(alvos):
            dado = int(input("Dado: "))
            teste1 = dado + p1.FIS
            teste = teste1 + ((p1.armas_de_fogo * 0.01) * teste1) - mod
            if teste == 2:
                print("Erro crítico")
            elif teste < 6:
                print("Errou")
            elif 6 <= teste < 8:
                print("Tronco")
            elif 8 <= teste < 9:
                print("Braços ou Pernas")
            elif 9 <= teste < 11:
                print("Mãos ou pés")
            elif teste == 11:
                print("Cabeça")
            elif teste > 12:
                print("Olhos")

#ações

def lootear(p1,dado,mod):
    teste = (p1.INT+dado)-mod
    if teste == 2:
        print("Nada")
    elif teste > 2 and teste <= 6:
        print("Pouco 1/3")
    elif teste > 6 and teste <= 11:
        print("Médio: 2/3")
    elif teste >= 12:
        print("Tudo")

def medicamento(p1, Item):
    try: 
        if Item == "analgesico":
            p1.removerItem(Item, 1)
            p1.removerEfeito("dor", 1)
            print("Analgesico usado: dor reduzida")
        if Item == "antibiotico":
            p1.removerItem(Item, 1)
            p1.removerEfeito("infec", randint(1, 4))
            print("Antibiotico usado: infecção reduzida")
        if Item == "antisseptico":
            p1.removerItem(Item, 1)
            p1.removerEfeito("infec", 1)
            print("Antisseptico usado: infecção reduzida")
        if Item == "bandagem":
            p1.removerItem(Item, 1)
            p1.removerEfeito("sangramento", 1)
            print("Bandagem usada: sangramento estancado")
        if Item == "curativo_estéril":
            p1.removerItem(Item, 1)
            p1.removerEfeito("sangramento", 1)
            print("Curativo estéril usado: sangramento estancado")
        if Item == "sutura":
            p1.removerItem(Item, 1)
            #p1.removerEfeito("ferimentoGrave", randint(1, 3))
            print("Sutura usada: ferimento grave tratado")
        if Item == "agulha_seringa":
            p1.removerItem(Item, 1)
            p1.removerEfeito("infec", randint(1, 4))
            print("Agulha e seringa usadas: infecção reduzida")
        if Item == "compressa":
            p1.removerItem(Item, 1)
            p1.removerEfeito("sangramento", randint(1, 4))
            print("Compressa usada: sangramento reduzido")
        if Item == "kit_primeiros_socorros":
            p1.removerItem(Item, 1)
            #p1.removerEfeito("ferimento", randint(5, 15))
            print("Kit de primeiros socorros usado: ferimento tratado")
        if Item == "alcool":
            p1.removerItem(Item, 1)
            p1.removerEfeito("infec", randint(5, 15))
            print("Álcool usado: infecção reduzida")
        if Item == "sabonete":
            p1.removerItem(Item, 1)
            p1.removerEfeito("infec", 1)
            print("Sabonete usado: infecção reduzida")
        if Item == "luvas_latex":
            p1.removerItem(Item, 1)
            print("Luvas de látex usadas: proteção aplicada")
        if Item == "máscara_cirurgica":
            p1.removerItem(Item, 1)
            print("Máscara cirúrgica usada: proteção aplicada")
        if Item == "analgesico_forte":
            p1.removerItem(Item, 1)
            p1.removerEfeito("dor", randint(1, 3))
            print("Analgesico forte usado: dor intensa reduzida")
        if Item == "antivirais":
            p1.removerItem(Item, 1)
            p1.removerEfeito("infec", randint(0, 2))
            print("Antivirais usados: infecção viral reduzida")
        if Item == "soro":
            p1.removerItem(Item, 1)
            p1.removerEfeito("sede", randint(1, 4))
            print("Soro usado: sede reduzida")
        if Item == "estetoscopio":
            p1.removerItem(Item, 1)
            print("Estetoscópio usado: diagnóstico realizado")
        if Item == "tesoura_medica":
            p1.removerItem(Item, 1)
            print("Tesoura médica usada: ferramenta aplicada")
        if Item == "pinça":
            p1.removerItem(Item, 1)
            print("Pinça usada: ferramenta aplicada")
        print("usado")
    except:
        print("Item não encontrado")


