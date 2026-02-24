from Atributos.personagem import Personagem
import Sobrevivencia.gerar
import Sobrevivencia.testes
import Sobrevivencia.zombies

acoesCombate = {
    "zombieFugir": Sobrevivencia.testes.zombieFugir,
    "desarmado": Sobrevivencia.testes.desarmado,
}

minuto = 0

nome = input("Personagem: ")
hora = int(input("Hora do dia: "))
ultimaBebida = hora
ultimaRefeicao = hora
ultimoSono = hora
p1 = Personagem.carregar(f"Salvos/{nome}.json")
dia = p1.DIA
while True:
    p1 = Personagem.carregar(f"Salvos/{nome}.json")
    mod = p1.modificador(nome)
    acao = input("Ação: ")
    p1.aplicarEfeito("ACT",1)

    #Horario
    if hora > 24:
        hora = 0
        dia += 1 
        p1.aplicarEfeito("DIA",1)
    
    if minuto > 60:
        minuto %= 60
        hora += 1

    #Ações e efeitos em tempo de jogo
    if acao != "check" and acao != "tempo" and acao != "beber" and acao != "comer":
        beberD = (hora - ultimaBebida)
        comerD = (hora - ultimaRefeicao)
        sonoD  = (hora - ultimoSono)

        if beberD < 0:
            beberD += 24
        if beberD > 6:
            if p1.sede != 2:
                print("ficar de olho")
                p1.aplicarEfeito("sede",1)

        if comerD < 0:
            comerD += 24
        if comerD > 8:
            if p1.fome != 2:
                p1.aplicarEfeito("fome",1)

        if sonoD < 0:
            sonoD += 24
        if sonoD > 16:
            if p1.sono != 2:
                p1.aplicarEfeito("sono",1)

    
    #Cansaço
    if (p1.ACT%96)==0:
        if p1.ACT != 0:
            p1.aplicarEfeito("sono",1)
            print("Sente sono por cansaço")
    
    #Interface
    if acao == "x":
        break

    elif acao == "zombieAtaque":
        print(Sobrevivencia.testes.zombieAtaque(p1,mod))

    elif acao == "zombieLutar":
        dado = int(input("Dados: "))
        print("Físico máximo é 4")
        zombieFIS = int(input("FisicoZombie: "))
        print(Sobrevivencia.testes.zombieLutar(p1,dado,mod,zombieFIS))

    elif acao == "armaBranca":
        item = input("Item: ")
        dado = int(input("Dados: "))
        try:
            print(Sobrevivencia.testes.armasBrancas(p1,item,dado,mod))       
        except:
            print("Item não encontrado ou algum outro Erro")

    elif acao == "adicionar":
        if (len(p1.inventario)) < (6+p1.bolsa):
            item = input("Item: ")
            valor = int(input("Valor: "))
            p1.adicionarItem(item,valor)
        else:
            print("Não tem espaço")
        
    elif acao == "aplicarEfeito":
        efeito = input("Efeito: ")
        valor = int(input("Valor: "))
        p1.aplicarEfeito(efeito,valor)

    elif acao == "removerEfeito":
        atributo = input("Atributo: ")
        valor = int(input("Valor: "))
        p1.removerEfeito(atributo,valor)

    elif acao == "removerItem":
        item = input("Item: ")
        p1.deletarItem(item)

    elif acao == "testeSorte":
        dado = int(input("Dado: "))
        atributo = int(input("Atributo: "))
        habilidade = input("Habilidade: ")
        nivelHabilidade = int(input("Nível da Habilidade: "))
        dificuldade = int(input("Dificuldade: "))
        tempoadd = int(input("Minutos: "))
        minuto += tempoadd
        print(Sobrevivencia.testes.testeSorte(p1,dado,atributo,habilidade,nivelHabilidade,dificuldade,mod))

    elif acao == "testeHab":
        habilidade = input("Nome da Habilidade: ")
        nivelHabilidade = int(input("Nível da Habilidade: "))
        dificuldade = int(input("Dificuldade: "))
        tempoadd = int(input("Minutos: "))
        minuto += tempoadd
        print(Sobrevivencia.testes.testeHabilidade(p1,habilidade,nivelHabilidade,dificuldade,mod))

    elif acao == "testeAtr":
        atributo = int(input("Atributo: "))
        dificuldade = int(input("Dificuldade: "))
        tempoadd = int(input("Minutos: "))
        minuto += tempoadd
        print(Sobrevivencia.testes.testeAtributo(atributo,dificuldade,mod))
    
    elif acao == "atirar":
        arma = input("arma: ")
        municao = int(input("Municao: "))
        if p1.removerItem(arma, municao) == "minimo":
            print("Munição Acabou")
            continue
        alvos = int(input("Alvos: "))
        Sobrevivencia.testes.armasFogo(p1,arma, municao, alvos, mod)   # agora passa p1 direto

    elif acao == "checkItem":
        item = input("Item: ")
        p1.checkItem(p1,item)

    elif acao == "gerarLoot":
        local = input("Local: ")
        max_zumbi = Sobrevivencia.zombies.max_zombie(local)
        Sobrevivencia.gerar.gerar_loot(local)
        zombiesLocal = Sobrevivencia.zombies.gerar_zombies(local,max_zumbi)

    elif acao == "sairLocal":
        try:
            print(f"Você saiu do local {zombiesLocal.nome}.")
            del zombiesLocal   # exclui o objeto da memória
        except:
            print("Nenhum local ativo para sair.")

    elif acao == "removerZombie":
        try:
            quantidade = int(input("Quantos zumbis remover? "))
            if zombiesLocal:
                zombiesLocal.remover_zumbi(quantidade)
            else:
                print("Nenhum local ativo para remover zumbis.")
        except:
            print("Erro ao tentar remover zumbis")

    elif acao == "lootear":
        dado = int(input("Dados: "))
        Sobrevivencia.testes.lootear(p1,dado,mod)

    elif acao == "medicamento":
        item = input("Item: ")
        Sobrevivencia.testes.medicamento(p1,item)

    elif acao in acoesCombate:
        dado = int(input("Dado: "))
        resultado = acoesCombate[acao](p1, dado, mod) 
        print(resultado)

    elif acao == "tempo":
        print(dia,":",hora,":",minuto)

    elif acao == "tempoAdd":
        tempoadd = int(input("Minutos: "))
        minuto += tempoadd

    elif acao == "tempoRmv":
        tempormv = int(input("Tempo: "))
        minuto += tempormv

    elif acao == "check":
        p1.check(nome)

    elif acao == "dormir":
        quantHoras = int(input("Horas: "))
        actAtual = p1.ACT
        p1.removerEfeito("ACT",actAtual)
        if quantHoras > 6 and quantHoras < 12:
            p1.removerEfeito("sono",1)
        if quantHoras > 12:
            p1.removerEfeito("sono",2)
        hora += quantHoras
        print(dia,":",hora,":",minuto)
        if p1.sono == 0:
            print("Está descansado")

    elif acao == "comer":
        try:
            item = input("Item: ")
            if p1.removerItem(item,1) == "minimo":
                print("Item acabou")
                continue
            ultimaRefeicao = hora
            p1.removerEfeito("fome",1)
            minuto += 15
            print("Comeu")
            if p1.fome == 0:
                print("Está saciado")
        except:
            print("Não foi achado o item")

    elif acao == "beber":
        try:
            item = input("Item: ")
            if p1.removerItem(item,1) == "minimo":
                print("Item acabou")
                continue
            ultimaBebida = hora
            p1.removerEfeito("sede",1)
            minuto += 15
            print("Bebeu")
            if p1.sede == 0:
                print("Está hidratado")
        except:
            print("Não foi achado o item")

    elif acao == "usar":
        try:
            item = input("Item: ")
            if p1.removerItem(item,1) == "minimo":
                p1.deletarEfeito(item)
                print("lixo jogado fora")
                continue
            efeito = input("Efeito: ")
            p1.removerEfeito(efeito,1)
        except:
            print("Item não encontrado")

    elif acao == "testeMoral":
        if p1.MORAL < 5:
            dado = int(input("Dados: "))
            if (dado+(p1.MORAL*(p1.MORAL*0.1))) < p1.MORAL:
                print("Você cometeu suicídio")
            else:
                print("Você permanece bem...")

    elif acao == "help":
        print("=== Lista de Ações Disponíveis ===")
        print("x                -> sair do jogo")
        print("zombieAtaque     -> enfrentar ataque de zumbi")
        print("zombieLutar      -> lutar contra zumbi (dados + físico)")
        print("armaBranca       -> atacar com arma branca")
        print("adicionar        -> adicionar item ao inventário")
        print("aplicarEfeito    -> aplicar efeito a um atributo")
        print("removerEfeito    -> remover efeito de um atributo")
        print("removerItem      -> remover item do inventário")
        print("testeSorte       -> realizar teste de sorte")
        print("testeHab         -> realizar teste de habilidade")
        print("testeAtr         -> realizar teste de atributo")
        print("atirar           -> atacar com arma de fogo")
        print("checkItem        -> verificar item no inventário")
        print("gerarLoot        -> gerar loot em local")
        print("lootear          -> tentar coletar loot")
        print("medicamento      -> usar medicamento")
        print("zombieFugir      -> tentar fugir de zumbi")
        print("desarmado        -> lutar desarmado")
        print("tempo            -> mostrar tempo atual")
        print("tempoAdd         -> adicionar minutos ao tempo")
        print("tempoRmv         -> remover minutos do tempo")
        print("check            -> checar status do personagem")
        print("dormir           -> descansar e recuperar sono")
        print("comer            -> consumir alimento")
        print("beber            -> consumir bebida")
        print("usar             -> usar item genérico")
        print("testeMoral       -> realizar teste de moral")
        print("help             -> mostrar esta lista de comandos")
        print("=================================")

    else:
        print("Ação inválida")

    try:
        zombiesLocal.encontro()
    except:
        Sobrevivencia.zombies.gerar_aleatorio(p1)

    if p1.MORAL < 5:
        if hora > 18 and hora < 23:
            print("Fazer teste da MORAL")
    if p1.CONS == 10:
        p1.aplicarEfeito("MORAL",1)

    minuto += 1 
    print("-"*10)

    