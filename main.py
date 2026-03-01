from Atributos.personagem import Personagem
from Atributos.personagem import Habilidades
import Sobrevivencia.gerar
import Sobrevivencia.testes
import Sobrevivencia.zombies
import Sobrevivencia.necessidades

personagens = []

# =========================
# CARREGAR OU CRIAR PERSONAGEM
# =========================
while True:
    nome = input("Carregar Personagem: ")
    if nome == "criar":
        DICHabilidades = {}
        FIS, INT, SOC = 0, 0, 0
        nome_novo = input("Nome: ")
        idade = int(input("Idade: "))
        emprego = input("Emprego: ")

        # Distribuição de pontos
        while (FIS + INT + SOC) != 9:
            print("Você tem 9 pontos para distribuir, caso não consiga tente novamente")
            FIS = int(input("FIS: "))
            INT = int(input("INT: "))
            SOC = int(input("SOC: "))

        print("Você tem 4 pontos para distribuir nas habilidades")
        habilidades_validas = [
            "armas_de_fogo","armas_brancas","desarmado","demolicao","conducao",
            "persuasao","lideranca","furtividade","cozinha","reparos","ciencias",
            "medicina","informatica","eletronica","psicologia","administracao"
        ]
        print("Habilidades disponíveis:", ", ".join(habilidades_validas))

        soma = 0
        while True:
            key = input("Habilidade: ")
            value = int(input("Valor: "))

            if key not in habilidades_validas:
                DICHabilidades = {}
                soma = 0
                print("Habilidade inválida. Habilidades resetadas, tente novamente")
                continue

            DICHabilidades[key] = value * 10
            soma = sum(DICHabilidades.values())

            if soma > 40:
                DICHabilidades = {}
                soma = 0
                print("Usou mais que 4 pontos. Habilidades resetadas, tente novamente")
                continue

            aux = input("Continuar S/N: ")
            if aux.lower() == "n":
                break

        Sobrevivencia.gerar.criarDinamico(nome_novo, idade, emprego, FIS, INT, SOC, DICHabilidades)

    elif nome == "x":
        break

    else:
        try:
            # checa se já carregou personagem com esse nome
            if not any(p.nome == nome for p in personagens):
                p = Personagem.carregar(f"Salvos/{nome}.json")
                personagens.append(p)
                print(f"Personagem {nome} carregado.")
            else:
                print(f"Personagem {nome} já está carregado.")
        except:
            print(f"Não foi possível carregar {nome}.")

# =========================
# LOOP PRINCIPAL DE AÇÕES
# =========================
while True:
    print("-"*10)

    nome = input("Personagem da ação: ")
    p1 = Personagem.carregar(f"Salvos/{nome}.json")

    minutos_totais = p1.MIN
    dia, hora, minuto = Sobrevivencia.necessidades.atualizar_tempo(minutos_totais)

    acao = input("Ação: ")
    p1.aplicarEfeito("ACT", 1)

    tempo_gasto = 0  # quanto tempo a ação consumiu

    # =========================
    # AÇÕES
    # =========================

    if acao == "x":
            break
    
    elif acao == "zombieAtaque":
        zombieFIS = int(input("Fisico do zumbie: "))
        print(Sobrevivencia.testes.zombieAtaque(p1))

    elif acao == "zombieLutar":
        dado = int(input("Dados: "))
        print("Físico máximo é 4")
        zombieFIS = int(input("FisicoZombie: "))
        print(Sobrevivencia.testes.zombieLutar(p1, dado, zombieFIS))

    elif acao == "zombieFugir":
        dado = int(input("Dado: "))
        print(Sobrevivencia.testes.zombieFugir(p1, dado))

    elif acao == "desarmado":
        dado = int(input("Dado: "))
        print(Sobrevivencia.testes.desarmado(p1, dado))

    elif acao == "armaBranca":
        item = input("Item: ")
        dado = int(input("Dados: "))
        try:
            print(Sobrevivencia.testes.armasBrancas(p1, item, dado))       
        except:
            print("Item não encontrado ou algum outro Erro")

    elif acao == "atirar":
        arma = input("arma: ")
        municao = int(input("Municao: "))
        if p1.removerItem(arma, municao) == "minimo":
            print("Munição Acabou")
            continue
        alvos = int(input("Alvos: "))
        Sobrevivencia.testes.armasFogo(p1, arma, municao, alvos)

    elif acao == "adicionar":
        if (len(p1.inventario)) < (6 + p1.bolsa):
            item = input("Item: ")
            valor = int(input("Valor: "))
            p1.adicionarItem(item, valor)
        else:
            print("Não tem espaço")

    elif acao == "aplicarEfeito":
        efeito = input("Efeito: ")
        valor = int(input("Valor: "))
        p1.aplicarEfeito(efeito, valor)

    elif acao == "removerEfeito":
        atributo = input("Atributo: ")
        valor = int(input("Valor: "))
        p1.removerEfeito(atributo, valor)

    elif acao == "removerItem":
        item = input("Item: ")
        p1.deletarItem(item)

    elif acao == "testeSorte":
        dado = int(input("Dado: "))
        atributo = input("Nome do atributo: ")
        atributo = Sobrevivencia.testes.mod(p1, atributo)
        habilidade = input("Nome da habilidade: ")
        nivelHabilidade = getattr(p1,habilidade,0)
        dificuldade = int(input("Dificuldade: "))
        tempoadd = int(input("Minutos: "))
        minutos_totais  += tempoadd
        print(Sobrevivencia.testes.testeSorte(p1, dado, atributo, habilidade, nivelHabilidade, dificuldade))

    elif acao == "testeHab":
        habilidade = input("Nome da habilidade: ")
        nivelHabilidade = getattr(p1,habilidade,0)
        dificuldade = int(input("Dificuldade: "))
        tempoadd = int(input("Minutos: "))
        minutos_totais  += tempoadd
        print(Sobrevivencia.testes.testeHabilidade(p1, habilidade, nivelHabilidade, dificuldade))

    elif acao == "testeAtr":
        atributo = input("Nome do Atributo: ")
        atributo = Sobrevivencia.testes.mod(p1, atributo)
        dificuldade = int(input("Dificuldade: "))
        tempoadd = int(input("Minutos: "))
        minutos_totais  += tempoadd
        print(Sobrevivencia.testes.testeAtributo(atributo, dificuldade))

    elif acao == "checkItem":
        item = input("Item: ")
        p1.checkItem(p1, item)

    elif acao == "gerarLoot":
        local = input("Local: ")
        max_zumbi = Sobrevivencia.zombies.max_zombie(local)
        Sobrevivencia.gerar.gerar_loot(local)
        zombiesLocal = Sobrevivencia.zombies.gerar_zombies(local, max_zumbi)

    elif acao == "sairLocal":
        try:
            print(f"Você saiu do local {zombiesLocal.nome}.")
            del zombiesLocal
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
        Sobrevivencia.testes.lootear(p1, dado)

    elif acao == "medicamento":
        item = input("Item: ")
        Sobrevivencia.testes.medicamento(p1, item)

    elif acao == "tempo":
        print(f"Dia {dia} - {hora:02d}:{minuto:02d}")

    elif acao == "tempoAdd":
        aux = input("Dia,hora,minuto: ")
        if aux == "dia":
            tempoadd = int(input("Dia: "))
            minutos_totais += tempoadd*60*24
        if aux == "hora":
            tempoadd = int(input("Hora: "))
            minutos_totais += tempoadd*60
        if aux == "min":
            tempoadd = int(input("Minutos: "))
            minutos_totais += tempoadd

    elif acao == "tempoRmv":
        aux = input("Dia,hora,minuto: ")
        if aux == "dia":
            tempoadd = int(input("Dia: "))
            minutos_totais -= tempoadd*60*24
        if aux == "hora":
            tempoadd = int(input("Hora: "))
            minutos_totais -= tempoadd*60
        if aux == "min":
            tempoadd = int(input("Minutos: "))
            minutos_totais -= tempoadd

    elif acao == "check":
        p1.check(nome)

    elif acao == "dormir":
        horas = int(input("Horas: "))
        minutos_dormidos = horas * 60
        minutos_totais += minutos_dormidos
        for p in personagens:
            actAtual = p.ACT
            p.removerEfeito("ACT", actAtual)
            if 6 < horas < 12:
                p.removerEfeito("sono", 1)
            if horas > 12:
                p.removerEfeito("sono", 2)
            if p.sono == 0:
                print(f"{p.nome} está descansado")
        print(dia, ":", hora, ":", minuto)

    elif acao == "comer":
        try:
            item = input("Item: ")
            if p1.removerItem(item, 1) == "minimo":
                print("Item acabou")
                continue
            p1.adicionarEfeito("ultimaRefeicao",minutos_totais)
            p1.removerEfeito("fome", 1)
            minutos_totais  += 15
            print("Comeu")
            if p1.fome == 0:
                print("Está saciado")
        except:
            print("Não foi achado o item")

    elif acao == "beber":
        try:
            item = input("Item: ")
            if p1.removerItem(item, 1) == "minimo":
                print("Item acabou")
                continue
            p1.adicionarEfeito("ultimaBebida",minutos_totais)
            p1.removerEfeito("sede", 1)
            minutos_totais  += 15
            print("Bebeu")
            if p1.sede == 0:
                print("Está hidratado")
        except:
            print("Não foi achado o item")

    elif acao == "usar":
        try:
            item = input("Item: ")
            valor = int(input("Valor: "))
            if p1.removerItem(item, 1) == "minimo":
                p1.deletarEfeito(item)
                print("lixo jogado fora")
                continue
            efeito = input("Efeito: ")
            p1.removerEfeito(efeito, valor)
        except:
            print("Item não encontrado")

    elif acao == "testeMoral":
        if p1.MORAL < 5:
            dado = int(input("Dados: "))
            if (dado + (p1.MORAL * (p1.MORAL * 0.1))) < p1.MORAL:
                print("Você cometeu suicídio")
            else:
                print("Você permanece bem...")

    elif acao == "encontro":
        zombiesLocal.encontro()

    elif acao == "transferir":
        nome = input("Transferência para: ")
        p2 = Personagem.carregar(f"Salvos/{nome}.json")
        item = input("Item: ")
        p1.transferencia(p1,p2,item)

    elif acao == "bandagem":
        parte = input("Parte: ")
        Sobrevivencia.necessidades.bandagem(p1,parte)

    elif acao == "help":
        print("=== Lista de Ações Disponíveis ===")
        print("x                -> sair do jogo")
        print("zombieAtaque     -> enfrentar ataque de zumbi")
        print("zombieLutar      -> lutar contra zumbi (dados + físico)")
        print("zombieFugir      -> tentar fugir de zumbi")
        print("desarmado        -> lutar desarmado")
        print("armaBranca       -> atacar com arma branca")
        print("atirar           -> atacar com arma de fogo")
        print("adicionar        -> adicionar item ao inventário")
        print("aplicarEfeito    -> aplicar efeito a um atributo")
        print("removerEfeito    -> remover efeito de um atributo")
        print("removerItem      -> remover item do inventário")
        print("testeSorte       -> realizar teste de sorte")
        print("testeHab         -> realizar teste de habilidade")
        print("testeAtr         -> realizar teste de atributo")
        print("checkItem        -> verificar item no inventário")
        print("gerarLoot        -> gerar loot em local")
        print("lootear          -> tentar coletar loot")
        print("medicamento      -> usar medicamento")
        print("sairLocal        -> sair do local atual")
        print("removerZombie    -> remover zumbis do local")
        print("tempo            -> mostrar tempo atual")
        print("tempoAdd         -> adicionar minutos ao tempo")
        print("tempoRmv         -> remover minutos do tempo")
        print("check            -> checar status do personagem")
        print("dormir           -> descansar e recuperar sono")
        print("comer            -> consumir alimento")
        print("beber            -> consumir bebida")
        print("usar             -> usar item genérico")
        print("testeMoral       -> realizar teste de moral")
        print("encontro         -> Endcontro com zumbis em locais")
        print("transferir       -> Transferi itens entre personagens")
        print("bandagem          -> Curar com bandagem parte do corpo")
        print("help             -> mostrar esta lista de comandos")        
        print("=================================")


    else:
        print("Ação inválida")

    # AVANÇA TEMPO

    minutos_totais += tempo_gasto
    minutos_totais += 1  # tempo mínimo por ação

    dia, hora, minuto = Sobrevivencia.necessidades.atualizar_tempo(minutos_totais)

    # NECESSIDADES 

    for p in personagens:
        p.ultimaBebida = Sobrevivencia.necessidades.necessidade(
            p, minutos_totais, p.ultimaBebida, "sede", 4*60
        )
        p.ultimaRefeicao = Sobrevivencia.necessidades.necessidade(
            p, minutos_totais, p.ultimaRefeicao, "fome", 6*60
        )
        p.ultimoSono = Sobrevivencia.necessidades.necessidade(
            p, minutos_totais, p.ultimoSono, "sono", 16*60
        )

    # CANSAÇO

    if p1.ACT != 0 and (p1.ACT % 48) == 0:
        p1.aplicarEfeito("sono", 1)
        print("Sente sono por cansaço")

    # EVENTOS

    Sobrevivencia.zombies.gerar_aleatorio(p1)

    if p1.MORAL < 5 and 18 < hora < 23:
        print("Fazer teste da MORAL")

    if p1.CONS >= 10:
        p1.aplicarEfeito("MORAL", 1)

    # SINCRONIZA E SALVA
    
    for p in personagens:
        p.MIN = minutos_totais