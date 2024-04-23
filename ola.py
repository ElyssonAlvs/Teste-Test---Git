from cmath import log10


def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplocacao(a, b):
    return a * b

def divisao(a, b):
    return a / b

def potencia(a, b):
    return a ** b

def raiz(a):
    return a ** 0.5

def media(a, b):
    return (a + b) / 2  

def media_ponderada(a, b, c):
    return (a + 2*b + 3*c) / 6  

def media_harmonica(a, b):  
    return 2 / (1/a + 1/b) 

def media_geometrica(a, b):  
    return (a * b) ** 0.5

def media_quadratica(a, b): 
    return ((a ** 2 + b ** 2) / 2) ** 0.5  

def media_cubica(a, b): 
    return ((a ** 3 + b ** 3) / 2) ** (1/3)

def media_logaritmica(a, b): 
    return 10 ** ((log10(a) + log10(b)) / 2)

def media_exponencial(a, b): 
    return (a * b) ** 0.5 

a = input("Digite o primeiro número: ")
b = input("Digite o segundo número: ")
c = input("Digite o terceiro número: ")
opcao = input("""Digite a opção desejada: 
              1 - Somar
              2 - Subtrair
              3 - Multiplicar
              4 - Dividir
              5 - Potência
              6 - Raiz
              7 - Média
              8 - Média Ponderada
              9 - Média Harmônica
              10 - Média Geométrica
              11 - Média Quadrática
              12 - Média Cúbica
              13 - Média Logarítmica
              14 - Média Exponencial
              15 - Sair
              """)
if opcao == "1":
    print("A soma é: ", soma(a, b))
elif opcao == "2":
    print("A subtração é: ", subtracao(a, b))
elif opcao == "3":
    print("A multiplicação é: ", multiplocacao(a, b))
elif opcao == "4":
    print("A divisão é: ", divisao(a, b))
elif opcao == "5":
    print("A potência é: ", potencia(a, b))
elif opcao == "6":
    print("A raiz é: ", raiz(a))
elif opcao == "7":
    print("A média é: ", media(a, b))
elif opcao == "8":
    print("A média ponderada é: ", media_ponderada(a, b, c))
elif opcao == "9":
    print("A média harmônica é: ", media_harmonica(a, b))
elif opcao == "10":
    print("A média geométrica é: ", media_geometrica(a, b))
elif opcao == "11":
    print("A média quadrática é: ", media_quadratica(a, b))
elif opcao == "12":
    print("A média cúbica é: ", media_cubica(a, b))
elif opcao == "13":
    print("A média logarítmica é: ", media_logaritmica(a, b))
elif opcao == "14":
    print("A média exponencial é: ", media_exponencial(a, b))
elif opcao == "15":
    print("Saindo...")
else:
    print("Opção inválida")
    
# Para executar o código, basta digitar no terminal: python ola.py


