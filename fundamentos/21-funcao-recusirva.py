"""
1 -> 1 * 1
2 -> 2 * 1
3 -> 3 * 2 * 1
"""

# 1 fatorial de numero

def fatorial(num):
    if num == 1:
        return 1
    else:
        return (num * fatorial(num -1))
    
numero = int(input("Digite um numero para o fatorial: "))
print(f"O fatorial de {numero} é {fatorial(numero)}")

# soma total de um número

def totalNumero(num):
    if num == 1:
        return 1
    else:
        return (num + totalNumero(num - 1))

num = int(input("Digite um numero para a soma: "))
print(f"A soma total de {num} é {totalNumero(num)}")