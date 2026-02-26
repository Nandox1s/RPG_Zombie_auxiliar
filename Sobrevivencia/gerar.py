import random
from random import randint

casa = {
    # comidas
    "enlatado_atum": lambda: 1,
    "enlatado_sardinha": lambda: 1,
    "enlatado_milho": lambda: 1,
    "bife": lambda: 3,
    "arroz": lambda: 3,
    "macarrao": lambda: 3,
    "bolacha": lambda: 1,
    "chocolate": lambda: 1,
    "enlatado_feijão": lambda: 1,
    # bebidas
    "agua": lambda: 4,
    "refri": lambda: 1,
    "suco": lambda: 2,
    "cerveja": lambda: 1,
    # armas improvisadas
    "taco_golfe": lambda: randint(15, 35),
    "taco_baseball": lambda: randint(25, 75),
    "chave_fenda": lambda: randint(40, 75),
    "faca_cozinha": lambda: randint(20, 40),
    # ferramentas
    "martelo": lambda: randint(40, 75),
    "chave_inglesa": lambda: randint(50, 100),
    "serrote": lambda: 1,
    "pe_cabra": lambda: randint(75,150),
    # utilidades
    "lanterna": lambda: randint(20, 40),
    "vela": lambda: 1,
    "isqueiro": lambda: randint(10, 20),
    "pilha": lambda: 1,
    "bateria": lambda: 1,
    # eletrônicos
    "radio": lambda: 1,
    "walkie_talkie": lambda: 1,
    "relógio": lambda: 1,
    # primeiros socorros
    "bandagem": lambda: 1,
    "kit_primeiros_socorros": lambda: randint(1, 10),
    "alcool": lambda: randint(3, 10),
    "remedio_dor": lambda: randint(1,8),
    # adições
    "mochila": lambda: randint(2,8),
    "pistola": lambda: randint(0,12),
    "rifle": lambda: randint(0,6),
}

def gerar_casa():
    casa_atual = {}
    itens_sorteados = random.choices(
        list(casa.keys()),
        weights = [
            # comidas
            8, 8, 8, 5, 6, 6, 5, 4, 4,
            # bebidas
            10, 6, 6, 3,
            # armas improvisadas
            4, 1, 2, 3,
            # ferramentas
            2, 2, 2, 2,
            # utilidades
            3, 2, 3, 4, 2,
            # eletrônicos
            2, 2, 2,
            # primeiros socorros
            3, 2, 2, 2,
            #adições
            2, 1, 1


        ],
        k=randint(1, 12)
    )

    for item in itens_sorteados:
        if item in casa_atual:
            casa_atual[item]["quantidade"] += 1
        else:
            casa_atual[item] = {
                "quantidade": 1,
                "durabilidade": casa[item]()
            }

    # saída mais agradável
    print("\n--- Inventário da Casa ---")
    for item, dados in casa_atual.items():
        print(f"{item:<15} | Quantidade: {dados['quantidade']} | Durabilidade: {dados['durabilidade']}")
    print("---------------------------\n")

    return casa_atual

mercado = {
    # comidas
    "enlatado_feijao": lambda: 1,
    "enlatado_sopa": lambda: 1,
    "enlatado_milho": lambda: 1,
    "arroz": lambda: 3,
    "macarrao": lambda: 3,
    "bolacha": lambda: 1,
    "chocolate": lambda: 1,
    "batata": lambda: 1,
    "cenoura": lambda: 1,
    "maca": lambda: 1,
    "banana": lambda: 1,
    # bebidas
    "agua": lambda: 4,
    "refri": lambda: 1,
    "suco": lambda: 2,
    "cerveja": lambda: 1,
    "saco_cafe": lambda: 4,
    # ferramentas pequenas
    "faca_cozinha": lambda: randint(20, 40),
    "martelo": lambda: randint(25, 50),
    "chave_inglesa": lambda: randint(25, 50),
    "serrote": lambda: randint(30, 60),
    "alicate": lambda: randint(20, 40),
    # armas improvisadas
    "taco_baseball": lambda: randint(25, 50),
    "cano_metal": lambda: randint(30, 60),
    "garrafa_vidro": lambda: randint(5, 15),
    # utilidades
    "lanterna": lambda: randint(20, 40),
    "pilha": lambda: randint(5, 15),
    "isqueiro": lambda: randint(10, 20),
    "vela": lambda: 1,
    "saco_plastico": lambda: 1,
    "corda": lambda: randint(15, 30),
    "fita_isolante": lambda: randint(10, 25),
    "manta_termica": lambda: 1,
    # eletrônicos e comunicação
    "radio": lambda: randint(20, 40),
    "walkie_talkie": lambda: randint(20, 40),
    "relógio": lambda: randint(15, 30),
    "bateria_grande": lambda: randint(30, 60),
    "carregador_portatil": lambda: randint(20, 40),
    # primeiros socorros
    "bandagem": lambda: 1,
    "kit_primeiros_socorros": lambda: randint(10, 20),
    "alcool": lambda: 1,
    "remedio_dor": lambda: 1,
    "antibiotico": lambda: 1,
    # higiene e misc
    "sabonete": lambda: 1,
    "papel_higienico": lambda: 1,
    "detergente": lambda: 1,
    "fita_adesiva": lambda: randint(10, 25),
}

def gerar_mercado():
    mercado_atual = {}
    itens_sorteados = random.choices(
        list(mercado.keys()),
        weights = [
            # comidas
            8, 8, 8, 6, 6, 5, 4, 5, 5, 6, 6,
            # bebidas
            10, 6, 6, 3, 4,
            # ferramentas pequenas
            3, 2, 2, 2, 2,
            # armas improvisadas
            2, 2, 3,
            # utilidades
            3, 4, 3, 2, 2, 2, 2, 1,
            # eletrônicos e comunicação
            2, 2, 2, 1, 1,
            # primeiros socorros
            3, 2, 2, 2, 1,
            # higiene e misc
            2, 2, 2, 2
        ],
        k=randint(1, 15)
    )

    for item in itens_sorteados:
        if item in mercado_atual:
            mercado_atual[item]["quantidade"] += 1
        else:
            mercado_atual[item] = {
                "quantidade": 1,
                "durabilidade": mercado[item]()
            }

    print("\n--- Inventário do Mercadinho ---")
    for item, dados in mercado_atual.items():
        print(f"{item:<20} | Quantidade: {dados['quantidade']} | Durabilidade: {dados['durabilidade']}")
    print("---------------------------------\n")

    return mercado_atual

posto = {
    # combustíveis e suprimentos automotivos
    "galao_gasolina": lambda: randint(1, 4),
    "frasco_oleo": lambda: randint(1, 3),
    "oleo_motor": lambda: randint(1, 3),
    "filtro_oleo": lambda: 1,
    "combustivel_portatil": lambda: randint(1, 3),
    # baterias e partida
    "bateria_carro": lambda: randint(40, 80),
    "jump_starter": lambda: randint(30, 70),
    # ferramentas automotivas
    "macaco_hidraulico": lambda: randint(50, 100),
    "chave_roda": lambda: randint(30, 60),
    "kit_reparo_pneu": lambda: randint(10, 30),
    "ferramentas_mecanico": lambda: randint(20, 50),
    # iluminação e energia
    "lanterna_potente": lambda: randint(40, 80),
    "lanterna_solar": lambda: randint(50, 100),
    "bateria_grande": lambda: randint(30, 60),
    "carregador_portatil": lambda: randint(20, 40),
    "pilha": lambda: randint(5, 15),
    # conveniência e comida
    "bebida_energetica": lambda: 1,
    "snack": lambda: 1,
    "agua": lambda: 4,
    "refri": lambda: 1,
    # itens de sobrevivência e utilidades
    "corda": lambda: randint(15, 30),
    "fita_isolante": lambda: randint(10, 25),
    "manta_termica": lambda: 1,
    "saco_plastico": lambda: 1,
    "isqueiro": lambda: randint(10, 20),
    # navegação e informação
    "mapa_cidade": lambda: 1,
    "relógio": lambda: randint(15, 30),
    # primeiros socorros
    "bandagem": lambda: 1,
    "kit_primeiros_socorros": lambda: randint(5, 15),
    "alcool": lambda: 1,
    # itens raros/úteis
    "kit_reparo_carro": lambda: randint(20, 50),
    "ferramenta_multifuncoes": lambda: randint(20, 45),
    "lanterna_tatica": lambda: randint(60, 120),
    "cigarros": lambda: 1
}

def gerar_posto():
    posto_atual = {}

    weights = [
        # combustíveis e suprimentos automotivos
        2, 2, 2, 1, 1,
        # baterias e partida
        1, 1,
        # ferramentas automotivas
        1, 2, 2, 2,
        # iluminação e energia
        2, 1, 1, 1, 3,
        # conveniência e comida
        4, 4, 10, 6,
        # itens de sobrevivência e utilidades
        3, 3, 1, 2, 3,
        # navegação e informação
        1, 2,
        # primeiros socorros
        3, 2, 2,
        # itens raros/úteis
        1, 1, 1, 1
    ]

    itens_sorteados = random.choices(
        list(posto.keys()),
        weights=weights,
        k=randint(1, 12)
    )

    for item in itens_sorteados:
        if item in posto_atual:
            posto_atual[item]["quantidade"] += 1
        else:
            posto_atual[item] = {
                "quantidade": 1,
                "durabilidade": posto[item]()
            }

    print("\n--- Inventário do Posto de Gasolina ---")
    for item, dados in posto_atual.items():
        print(f"{item:<22} | Quantidade: {dados['quantidade']:<2} | Durabilidade: {dados['durabilidade']}")
    print("----------------------------------------\n")

    return posto_atual

hospital = {
    # medicamentos e suprimentos
    "analgesico": lambda: randint(1, 6),
    "antibiotico": lambda: randint(1, 4),
    "antisseptico": lambda: 1,
    "bandagem": lambda: 1,
    "curativo_estéril": lambda: 1,
    "sutura": lambda: randint(1, 3),
    "agulha_seringa": lambda: randint(1, 4),
    "compressa": lambda: randint(1, 4),
    "kit_primeiros_socorros": lambda: randint(5, 15),
    # equipamentos médicos
    "oximetro": lambda: randint(10, 30),
    "termometro": lambda: randint(10, 25),
    "máscara_oxigenio": lambda: randint(20, 40),
    "tanque_oxigenio_pequeno": lambda: randint(30, 60),
    # suprimentos de higiene
    "alcool": lambda: randint(5, 15),
    "sabonete": lambda: 1,
    "luvas_latex": lambda: randint(5, 20),
    "máscara_cirurgica": lambda: randint(5, 20),
    # itens raros/úteis
    "analgesico_forte": lambda: randint(1, 3),
    "antivirais": lambda: randint(0, 2),
    "soro": lambda: randint(1, 4),
    "estetoscopio": lambda: randint(15, 35),
    # ferramentas e utilidades
    "tesoura_medica": lambda: randint(20, 40),
    "pinça": lambda: randint(15, 30),
    "lanterna": lambda: randint(20, 40),
    "pilha": lambda: randint(5, 15),
    # documentos e mapas (pouco comuns)
    "prontuario": lambda: 1,
    "mapa_hospital": lambda: 1
}

def gerar_hospital():
    hospital_atual = {}

    weights = [
        # medicamentos e suprimentos
        8, 3, 6, 10, 6, 2, 3, 4, 2,
        # equipamentos médicos
        1, 2, 1, 1,
        # suprimentos de higiene
        6, 3, 4, 4,
        # itens raros/úteis
        1, 1, 2, 1,
        # ferramentas e utilidades
        3, 3, 4, 4,
        # documentos e mapas
        1, 1
    ]

    itens_sorteados = random.choices(
        list(hospital.keys()),
        weights=weights,
        k=randint(1, 12)
    )

    for item in itens_sorteados:
        if item in hospital_atual:
            hospital_atual[item]["quantidade"] += 1
        else:
            hospital_atual[item] = {
                "quantidade": 1,
                "durabilidade": hospital[item]()
            }

    print("\n--- Inventário do Hospital ---")
    for item, dados in hospital_atual.items():
        print(f"{item:<22} | Quantidade: {dados['quantidade']:<2} | Durabilidade: {dados['durabilidade']}")
    print("--------------------------------\n")

    return hospital_atual

delegacia = {
    # armas de fogo (condição/durabilidade)
    "pistola": lambda: randint(30, 100),
    "revolver": lambda: randint(30, 100),
    "espingarda": lambda: randint(30, 100),
    # munições (quantidade)
    "municao_pistola": lambda: randint(6, 30),
    "municao_revolver": lambda: randint(6, 24),
    "municao_espingarda": lambda: randint(2, 12),
    # proteção e acessórios
    "colete_balistico": lambda: randint(50, 100),
    "coldre": lambda: randint(20, 60),
    "algemas": lambda: 1,
    # comunicação e iluminação
    "radio_policial": lambda: randint(30, 80),
    "lanterna_tatica": lambda: randint(40, 100),
    "pilha": lambda: randint(5, 20),
    # ferramentas e reparo
    "kit_reparo": lambda: randint(10, 30),
    "ferramentas_mecanico": lambda: randint(20, 50),
    # navegação e documentos
    "mapa_cidade": lambda: 1,
    "distintivo": lambda: 1,
    "uniforme": lambda: 1,
    "documentos": lambda: 1,
    "chave_veiculo": lambda: 1,
    # primeiros socorros e defesa não letal
    "bandagem": lambda: 1,
    "spray_pimenta": lambda: randint(1, 3),
    "lanterna": lambda: randint(15, 40),
}

def gerar_delegacia():
    delegacia_atual = {}

    weights = [
        # armas de fogo
        1, 1, 1,
        # munições
        3, 3, 2,
        # proteção e acessórios
        1, 2, 2,
        # comunicação e iluminação
        2, 2, 3,
        # ferramentas e reparo
        2, 2,
        # navegação e documentos
        1, 1, 1, 1, 1,
        # primeiros socorros e defesa não letal
        3, 2, 4
    ]

    itens_sorteados = random.choices(
        list(delegacia.keys()),
        weights=weights,
        k=randint(1, 10)
    )

    for item in itens_sorteados:
        if item in delegacia_atual:
            delegacia_atual[item]["quantidade"] += 1
        else:
            delegacia_atual[item] = {
                "quantidade": 1,
                "durabilidade": delegacia[item]()
            }

    print("\n--- Inventário da Delegacia ---")
    for item, dados in delegacia_atual.items():
        print(f"{item:<20} | Quantidade: {dados['quantidade']:<2} | Durabilidade: {dados['durabilidade']}")
    print("--------------------------------\n")

    return delegacia_atual

oficina = {
    # peças e consumíveis
    "oleo_motor": lambda: randint(1, 4),
    "filtro_oleo": lambda: randint(1, 3),
    "filtro_ar": lambda: randint(1, 3),
    "vela_ignicao": lambda: randint(1, 6),
    "correia_tempo": lambda: randint(1, 2),
    "alternador_usado": lambda: randint(10, 40),
    "bomba_combustivel": lambda: randint(10, 40),
    "pneu_estepe": lambda: randint(20, 60),
    "parafuso_porcas": lambda: randint(5, 20),
    "graxa_lubrificante": lambda: randint(1, 3),
    # ferramentas manuais
    "chave_inglesa": lambda: randint(30, 80),
    "chave_roda": lambda: randint(30, 70),
    "macaco_hidraulico": lambda: randint(50, 120),
    "chave_impacto": lambda: randint(40, 100),
    "martelo": lambda: randint(20, 60),
    "alicate": lambda: randint(20, 50),
    "serra_metal": lambda: randint(25, 60),
    "pe_cabra": lambda: randint(50, 120),
    # ferramentas elétricas
    "furadeira": lambda: randint(30, 80),
    "esmerilhadeira": lambda: randint(30, 80),
    "soldador": lambda: randint(40, 100),
    "compressor_ar": lambda: randint(60, 140),
    # peças eletrônicas e sensores
    "sensor_oxigenio": lambda: randint(10, 30),
    "modulo_ignicao": lambda: randint(15, 40),
    "cabos_vela": lambda: randint(10, 30),
    # utilidades e suprimentos
    "fita_isolante": lambda: randint(10, 25),
    "fita_adesiva": lambda: randint(10, 25),
    "corda": lambda: randint(15, 30),
    "lanterna_potente": lambda: randint(40, 100),
    "pilha": lambda: randint(5, 20),
    # itens raros/úteis
    "manual_reparos": lambda: 1,
    "kit_reparo_motor": lambda: randint(10, 40),
}

def gerar_oficina():
    oficina_atual = {}

    weights = [
        # peças e consumíveis
        6, 4, 4, 5, 2, 1, 1, 2, 6, 3,
        # ferramentas manuais
        3, 3, 1, 1, 3, 3, 2, 1,
        # ferramentas elétricas
        2, 2, 1, 1,
        # peças eletrônicas e sensores
        2, 1, 2,
        # utilidades e suprimentos
        3, 3, 2, 2, 3,
        # itens raros/úteis
        1, 1
    ]

    itens_sorteados = random.choices(
        list(oficina.keys()),
        weights=weights,
        k=randint(1, 12)
    )

    for item in itens_sorteados:
        if item in oficina_atual:
            oficina_atual[item]["quantidade"] += 1
        else:
            oficina_atual[item] = {
                "quantidade": 1,
                "durabilidade": oficina[item]()
            }

    print("\n--- Inventário da Oficina ---")
    for item, dados in oficina_atual.items():
        print(f"{item:<22} | Quantidade: {dados['quantidade']:<2} | Durabilidade: {dados['durabilidade']}")
    print("--------------------------------\n")

    return oficina_atual

def gerar_loot(local):
    if local == "casa":
        gerar_casa()
    if local == "mercado":
        gerar_mercado()
    if local == "posto":
        gerar_posto()
    if local == "hospital":
        gerar_hospital()
    if local == "delegacia":
        gerar_delegacia()
    if local == "oficina":
        gerar_oficina()

