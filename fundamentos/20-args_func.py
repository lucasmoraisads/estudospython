# 1 imprime um nome completo

def nomeCompleto(primeiroNome, sobreNome):
    print(f"Nome é: {primeiroNome} {sobreNome}")

nomeCompleto("Lucas", "Morais")

# 2 função para somar dois numero

def somar(a, b):
    return a + b

print(f"Some é : {somar(23, 6)}")

#3 função com valor default

def endereco(redenção="Redenção"):
    print(f"Eu moro em : {redenção}")

endereco()
endereco("Conceição do Araguia")