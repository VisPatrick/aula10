# criar uma calculadora que soma, subtrai, multiplica e divide dois números inteiros
# criar uma função para cada operação
# biblioteca para números aleatorios
# função soma
import os
os.system('cls')
import random


def soma(n1, n2):
    return n1 + n2


# função subtração
def subtracao(n1, n2):
    return n1 - n2


# função multiplicação
def multiplicacao(n1, n2):
    return n1 * n2


# função divisão
def divisao(n1, n2):
    return n1/n2

usuario_escolhe  = input('\nEscolha uma operação: ')
num1 = int(input('\nDigite o primeiro número: '))
num2 = int(input("Digite o segundo número: "))

match usuario_escolhe:
    case "soma":
        print(f"Soma: {soma(num1, num2)}")
    case "subtracao":
        print(f"Subtração: {subtracao(num1, num2)}")
    case "multiplicacao":
        print(f"Multiplicação: {multiplicacao(num1, num2)}")
    case "divisao":
        print(f"Divisão: {divisao(num1, num2)}")

# somar = soma(num1, num2)
# print(f"Soma: {somar}")

# sub = subtracao(num1, num2)
# print(f"Subtração: {sub}")

# mult = multiplicacao(num1, num2)
# print(f"Multiflicação: {mult}")

# div = divisao(num1, num2)
# print(f"Divisão: {div}")