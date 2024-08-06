from pessoa import Pessoa

def main():
    pessoa1 = Pessoa(nome='João',idade = 20)
    pessoa2 = Pessoa(nome='Maria', idade = 25)

    pessoa1.apresentar()
    pessoa1.envelhecer(20)
    pessoa1.apresentar()

    pessoa2.apresentar()
    pessoa2.envelhecer()
    pessoa2.apresentar()

if __name__ == '__main__':
    main()