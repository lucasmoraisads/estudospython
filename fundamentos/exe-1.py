#exer 1
"""
primeiroNome = input("digite um Nome:")
segundoNome = input("digite o sobrenome:")

nomeformatado = f"{segundoNome} {primeiroNome}"

print(nomeformatado)
print(f"Nome: {primeiroNome}  Sobrenome: {segundoNome}")


#exe2

texto = "Python é Muito interessante!"
palavra = texto.split()
textoIverntido = " ".join(palavra[::-1])
print(textoIverntido)

"""

texto1 = "arara"
texto2 = "Lucas"

#remove espaços e deixa em minusculo
texto1Formatado = texto1.lower().replace(" ", "")
texto2Formatado = texto2.lower().replace(" ", "")

#verifica se o texto original e igual ao seu reverso
palindromo1 = texto1Formatado == texto1[::-1]
palindromo2 = texto2Formatado == texto2[::-1]

print(palindromo1)
print(palindromo2)