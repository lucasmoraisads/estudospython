import random

# 1 seleciona um valor aleatorio de uma lista

liste1 = [1,5,4,7,5,87,8,6,3,2,32,234,34,6,7,879,7,6,34,23,23,12,1,23,3,5,64,7,8]
print(random.choice(liste1))

# 2 gera um numero aletario entre um intervalo

r1 = random.randint(5,50)
print(r1)

# 3 selecionar um caractere de uma string

nome = "Curso de python"
r2 = random.choice(nome)
print(r2)

# 4 seleciona mais de um valor aleatorio
# random.sample(sequencia, tamanho)

print(random.sample(liste1, 2))
print(random.sample(liste1, 3))


s = "Óla Mundo"
print(random.sample(s, 2))

# 5 programa de sorteio 

done = False
while not done:
    print("O que deseja fazer?")
    print("1. Adivinha um Número:")
    print("2. Sair")

    choice = input(">")

    if choice == "1":
        print("============ Adivinhe um número de 1 a 10 ==========")
        numero = int(input("Digite um número de 1 a 10:"))
        resultado = random.randint(1, 10)
        if numero == resultado:
            print("Parabêns Você acertou ")
        else:
            print(f"Tente novamente. O número sorteado foi: {resultado}")
    elif choice == "2":
        done = True 
    else:
        print("Opção inválida. escolha a opção 1 ou 2")1
        