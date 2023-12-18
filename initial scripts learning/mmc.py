#Escreva um programa em Python que leia dois números
#inteiros positivos a partir do teclado e determine
#o mínimo múltiplo comum (mmc) desses números.

def mdc(a, b):
    """
    Função que retorna o máximo divisor comum (MDC) entre dois números inteiros positivos a e b.
    """
    if b == 0:
        return a
    else:
        return mdc(b, a % b)

def mmc(a, b):
    """
    Função que retorna o mínimo múltiplo comum (MMC) entre dois números inteiros positivos a e b.
    """
    return (a * b) // mdc(a, b)

num1 = int(input("Digite o 1° número: "))
num2 = int(input("Digite o 2° número: "))

x = mmc(num1, num2)

if num1 < num2:
 print()
 print("O mmc de (%d,%d) é: %d"%(num1,num2,x))
else:
 print()
 print("O mmc de (%d,%d) é: %d"%(num2,num1,x))