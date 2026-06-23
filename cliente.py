class Cliente:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone
        self.pontos = 0

    def adicionar_pontos(self, quantidade):
        self.pontos += quantidade

    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Telefone: {self.telefone}")
        print(f"Pontos: {self.pontos}")
