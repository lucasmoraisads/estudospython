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

# 4 função para avaaliar filme

def avaliarFilme(avaliacaoFilme, nomeFilme):
    total = 0
    for i in range(avaliacaoFilme):
        nota = float(input("Digite a nota do filme: "))
        total += nota

    if avaliacaoFilme > 0:
        media = total / nota
    else:
        nota = 0

    print(f"Média de avaliação do filme: {nomeFilme} é : {media:.2f}")

avaliarFilme(2, "Sonic")