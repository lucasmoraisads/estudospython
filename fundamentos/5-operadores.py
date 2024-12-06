num1 = int(input("Digite primeiro número: \n"))
num2 = int(input("Digite segundo número: \n"))

# operador aritimeticos

soma = num1 + num2
subtra = num1 - num2
div = num1 / num2
mult = num1 * num2
mod = num1 % num2
exp = num1 ** num2


# comparação

maiorque = num1 > num2
menorque = num1 < num2
igualdade = num1 == num2
diferent = num1 != num2
maiorigual = num1 >= num2
menorigual = num1 <= num2

#tribuição

num1 += 1
num1 -= 1
num1 *= 1
num1 /= 1

print(f"Os números {num1} e {num2} são iguais {igualdade}")
print(f"Os números {num1} e maior ou igual a {num2} ? {maiorigual}")
print(f"Os números {num1} e menor ou igual a {num2} ? {menorigual}")
