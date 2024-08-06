from le_arquivo import Leitor

with Leitor() as arquivo:
    conteudo = arquivo.read()
    print(conteudo)