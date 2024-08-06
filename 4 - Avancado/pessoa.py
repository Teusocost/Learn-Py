class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"oi, meu nome é {self.nome} e tenho {self.idade} anos")

    def envelhecer(self, anos=1):
        self.idade += anos
        print(f"agora tenho {self.idade} anos")
