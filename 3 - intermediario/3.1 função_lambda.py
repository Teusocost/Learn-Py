quadrado = lambda x: x**2
print("função quadrado de 5 = ", quadrado(5))

verifica_par = lambda x: x % 2 == 0

print("o numero 5 é par? ", verifica_par(5))

dicionario = {
    'a' : 5,
    'b' : 10,
    'c' : 15,
    'd' : 20
}

filtrar_pares = lambda d: {chave: valor for chave, valor in d.items() if valor % 2 == 0}
resultado = filtrar_pares(dicionario)
print(resultado)

lista = [5,10,15,20,30]
filtrar_pares_lista = lambda l: {valor for valor in l if valor % 2 == 0}
resultado_lista = filtrar_pares_lista(lista)
print(resultado_lista)

#colocar tudo em uma linha
print((lambda l: {valor for valor in l if valor % 2 == 0})(lista)) #atenção aos parenteses de lambda
#para retornar uma lista em vez de dicionario: troque as chaves por colchetes
print((lambda l: [valor for valor in l if valor % 2 == 0])(lista)) 