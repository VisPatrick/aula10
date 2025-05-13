# biblioteca para números aleatorios
import random
import os
os.system('cls') # limpa a tela do terminal
# n = random.randint(1, 5) # random.randint(a, b) gera um número inteiro aleatório entre a e b
# m = random.randint(1, 5)
# print("\n", n, m)

# list_numeros = [random.randint(1, 10) for i in range(5)]    # gera uma lista com 5 números aleatórios entre 1 e 10
# print(list_numeros)


# exemplo 2 - função
def gera_numeros(i, f, q):    # dentro dos parênteses estão os parâmetros da função
    list_numeros = [random.randint(i, f) for i in range(q)]    # gera uma lista com 5 números aleatórios entre 1 e 10
    return list_numeros    # retorna a lista de números aleatórios


ini = int(input('Digite o número inicial: '))
fim = int(input('Digite o número final: '))
qnt = int(input('Digite a quantidade de números: '))

numeros = gera_numeros(ini, fim, qnt)    # chama a função gera_numeros e armazena o resultado na variável numeros
print(numeros)