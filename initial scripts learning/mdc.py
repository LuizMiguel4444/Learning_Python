#Escreva um programa em Python que leia dois números 
#inteiros positivos a partir do teclado e determine
#o máximo divisor comum (mdc) desses números.

def mdc(a, b):
    """
    Função que retorna o máximo divisor comum (MDC) entre dois números inteiros positivos a e b, usando recursão.
    """
    if b == 0:
        return a
    else:
        return mdc(b, a % b)

num1 = int(input("Digite o 1° número: "))
num2 = int(input("Digite o 2° número: "))

x = mdc(num1, num2)

if num1 < num2:
 print()
 print("O mdc de (%d,%d) é: %d"%(num1,num2,x))
else: 
 print()
 print("O mdc de (%d,%d) é: %d"%(num2,num1,x))