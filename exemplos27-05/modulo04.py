import time

#Função que possui muitas atribuições
def somar():
    n1 = int(input("Digite o primeiro numero da adição: "))
    n2 = int(input("Digite o segundo numero da adição: "))
    print(n1 + n2)


somar()

#Função exclusiva de soma de dois numeros
def somar2(n1, n2):
    soma = n1 + n2
    return soma

print("Soma 2:", somar2(22, 20))

#Terceiro exemplo de função
def somar3(n1, n2):
    return n1 + n2
# numero1 = float(input("Digite um numero: "))
# numero2 = float(input("Digite outro numero: "))

# #chamada de função
# print(somar3(numero1, numero2))

print(somar3(n2 = 12, n1 = 5))

#Função com parametros default (padrão)
def somar4(n1 = 0, n2 = 0):
    return n1 + n2

# print(somar4(50, 25))
# print(somar4())

#Função com apenas alguns valores default
def somar5(n1, n2=0):
    return n1 + n2

print(somar5(50, 25))
# print(somar5())
print(somar5(10))
print(somar5(n2 = 51, n1 = 12))

def somar6(n1, n2):
    if n1 == 1:
        return True

print(somar6 (1,3))
print(somar6 (13,3))

print(somar6(1, 2) + 10)
print(somar6(2, 2) + 10)


time.sleep(3)