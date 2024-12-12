import math

#  acessar o PI

print(math.pi)
print(f"{math.pi:.2f}")

# 2 acessar o numero de euler

print(math.e)
print(f"{math.e:.2f}")

# 3 arredondamento de numero tanto para cima quanto para baixo

num = 10.6
print(math.ceil(num))
print(math.floor(num)) 

# 4 fatorial de um numero

num2 = int(input("Digite um número: "))
print(math.factorial(num2))