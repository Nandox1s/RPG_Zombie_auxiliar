import random

distancia = ["perto", "média distância", "longe"]

tipos = {
    "comum": {"FIS": 2, "raridade": 50, "descricao": "Pessoa comum infectada"},
    "policial": {"FIS": 2, "raridade": 20, "descricao": "Usa colete, mais resistente"},
    "podre": {"FIS": 1, "raridade": 15, "descricao": "Corpo deteriorado"},
    "fresco": {"FIS": 3, "raridade": 10, "descricao": "Recém-transformado, ágil"},
    "cão_infernal": {"FIS": 3, "raridade": 5, "descricao": "Cão infectado, rápido"},
    "pombo_infernal": {"FIS": 1, "raridade": 5, "descricao": "Pássaro infectado, transmite infecção"},
    "mutante": {"FIS": 4, "raridade": 3, "descricao": "Aberração mutada"},
    "ghoul": {"FIS": 5, "raridade": 2, "descricao": "Quase humano, usa armas e equipamentos"},
}

class Local:
    def __init__(self, nome, max_zumbis):
        self.nome = nome
        self.max_zumbis = max_zumbis
        self.restantes = max_zumbis

    def encontro(self):
        if self.restantes <= 0:
            print(f"Não há mais zumbis no {self.nome}.")
            return []

        # chance de não aparecer nenhum zumbi
        if random.random() < 0.3:  # 30% de chance
            print(f"No {self.nome}, você não encontrou nenhum zumbi desta vez. Restam {self.restantes}.")
            return []

        # apenas mostra os zumbis, sem reduzir automaticamente
        max_por_encontro = min(self.restantes, 5)
        encontrados = random.randint(1, max_por_encontro)

        tipos_lista = list(tipos.keys())
        pesos = [tipos[t]["raridade"] for t in tipos_lista]

        zumbis_encontrados = []
        for _ in range(encontrados):
            tipo = random.choices(tipos_lista, weights=pesos, k=1)[0]
            pos = random.choice(distancia)
            zumbis_encontrados.append({
                "tipo": tipo,
                "FIS": tipos[tipo]["FIS"],
                "posicao": pos,
                "descricao": tipos[tipo]["descricao"]
            })

        print(f"No {self.nome}, apareceram {encontrados} zumbis. Restam {self.restantes}.")
        for z in zumbis_encontrados:
            print(f"- {z['tipo']} (FIS {z['FIS']}) | posição: {z['posicao']}")

        return zumbis_encontrados

    def remover_zumbi(self, quantidade=1):
        """Remove zumbis manualmente do local"""
        if self.restantes <= 0:
            print(f"Não há mais zumbis no {self.nome}.")
            return
        self.restantes = max(0, self.restantes - quantidade)
        print(f"Foram removidos {quantidade} zumbi(s). Restam {self.restantes} no {self.nome}.")

def gerar_zombies(nome, max_zumbi):
    return Local(nome, max_zumbi)

def gerar_aleatorio(p1):
    chance = max(0, 0.1 - (p1.furtividade * 0.0001))
    if random.random() < chance:
        print("Encontrou zumbi")

def max_zombie(local):
    if local == "casa":
        return random.randint(0, 6)         
    if local == "mercado":
        return random.randint(8, 20)   
    if local == "posto":
        return random.randint(8, 16)   
    if local == "hospital":
        return random.randint(25, 50)   
    if local == "delegacia":
        return random.randint(25, 50)   
    if local == "oficina":
        return random.randint(4, 12)
