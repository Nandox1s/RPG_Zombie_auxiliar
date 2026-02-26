import json
import os
from Atributos.atributos import Atributos
from Atributos.habilidades import Habilidades
from Atributos.efeitos import Efeitos


class Personagem(Atributos, Habilidades, Efeitos):
    def __init__(self, nome):
        self.nome = nome
        self.idade = 0
        self.bolsa = 0
        Atributos.__init__(self)
        Habilidades.__init__(self)
        Efeitos.__init__(self)
        self.inventario = {}

    def modificador(self, nome):
        mod = 0
        p1 = Personagem.carregar(f"Salvos/{nome}.json")
        lista = Efeitos()
        
        for efeito, valor in lista.__dict__.items():
            if hasattr(p1, efeito):
                valor_personagem = getattr(p1, efeito)
                if valor_personagem > 0:
                    mod += 1

        mod *= 0.4
        return mod
    
    def checkItem(self, p1, item):
        if "inventario" in p1.__dict__ and item in p1.__dict__["inventario"]:
            print("Munição:", p1.__dict__["inventario"][item])
        else:
            print(f"O item '{item}' não está no inventário.")
    
    def check(self, nome):
        p1 = Personagem.carregar(f"Salvos/{nome}.json")
        lista = Efeitos()

        for efeito, valor in lista.__dict__.items():
            if hasattr(p1, efeito):
                valor_personagem = getattr(p1, efeito)
                if valor_personagem > 0:
                    print(efeito,":",valor_personagem)

    def deletarEfeito(self, atributo):
        try:
            if hasattr(self, atributo):
                delattr(self, atributo)   # remove o atributo do objeto
                self.salvar()             # salva no JSON atualizado
        except:
            print(f"O atributo '{atributo}' não existe.")

    def adicionarEfeito(self, atributo, valor):
        setattr(self, atributo, valor)
        self.salvar()
        
    def aplicarEfeito(self, atributo, valor):
        try:
            if hasattr(self, atributo):
                atual = getattr(self, atributo)
                setattr(self, atributo, atual + valor)
                self.salvar()
        except:
            print(f"Atributo '{atributo}' não existe.")

    def removerEfeito(self, atributo, valor):
        try:
            if hasattr(self, atributo):
                atual = getattr(self, atributo)
                if atual == 0:
                    return "minimo"
                if atual < 0:
                    print("valor negativo")
                setattr(self, atributo, atual - valor)
                self.salvar()
        except:
            print(f"Atributo '{atributo}' não existe.")
        
    def adicionarItem(self, item, valor):
        try:
            if "inventario" in self.__dict__:
                inventario = self.__dict__["inventario"]
                if item in inventario:
                    inventario[item] += valor
                    print("Item adicionado")
                else:
                    inventario[item] = valor
                    print("Item adicionado")
                self.salvar()
        except:
            print("Inventário não existe no personagem.")

    def removerItem(self, item, valor):
        try:
            if "inventario" in self.__dict__ and item in self.__dict__["inventario"]:
                atual = self.__dict__["inventario"][item]
                if atual <= 0:
                    return "minimo"
                novo_valor = max(0, atual - valor)  # evita negativo
                self.__dict__["inventario"][item] = novo_valor
                self.salvar()
        except:
            print(f"O item '{item}' não existe no inventário.")
        
    def deletarItem(self, item):
        try:
            if "inventario" in self.__dict__ and item in self.__dict__["inventario"]:
                del self.__dict__["inventario"][item]  # remove a chave do dicionário
                self.salvar()
                print(f"Item '{item}' removido do inventário.")
        except:
            print(f"O item '{item}' não existe no inventário.")
        
    def salvar(self, pasta="Salvos"):
        os.makedirs(pasta, exist_ok=True)
        arquivo = os.path.join(pasta, f"{self.nome}.json")

        dados = {
            "nome": self.nome,
            "atributos": self.__dict__
        }

        with open(arquivo, "w", encoding="utf-8") as f:
            json.dump(dados, f, ensure_ascii=False, indent=4)

    def atualizar_tempo(self,hora, minuto, dia, personagem):
            # normaliza minutos
            if minuto >= 60:
                hora += minuto // 60
                minuto = minuto % 60

            # normaliza horas
            if hora >= 24:
                dia += hora // 24
                hora = hora % 24
                personagem.aplicarEfeito("DIA", hora // 24)  # aplica efeito proporcional

            return dia, hora, minuto
    
    def transferencia(self, p1, p2, item):
        try:
            if "inventario" in p1.__dict__ and item in p1.__dict__["inventario"]:
                valor = p1.__dict__["inventario"][item]  # pega a quantidade atual
                p1.deletarItem(item)                     # remove do inventário do p1
                p2.adicionarItem(item, valor)            # adiciona no inventário do p2
        except:
            print("Item não encontrado para transferência")

    @classmethod
    def carregar(cls, arquivo):
        with open(arquivo, "r", encoding="utf-8") as f:
            dados = json.load(f)
        personagem = cls(dados["nome"])
        personagem.__dict__.update(dados["atributos"])
        return personagem