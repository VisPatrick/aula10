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


num1 = random.randint(1, 100)
num2 = random.randint(1, 100)
print(30*"=")

somar = soma(num1, num2)
print(f"Soma: {somar}")

sub = subtracao(num1, num2)
print(f"Subtração: {sub}")

mult = multiplicacao(num1, num2)
print(f"Multiflicação: {mult}")

div = divisao(num1, num2)
print(f"Divisão: {div}")