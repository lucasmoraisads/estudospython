# função para imprimir uma mensagem

def olar():
    print("Bem Vindo ao Sistema de Filme")

# for i in range(10):
#     olar()

# 2 Função para calcular a media de notas

def calcular():
    numAvalicoes = int(input("Digite quantas avaliações deseja fazer para o filme: "))
    total = 0
    for i in range(numAvalicoes):
        note = float(input("Digite a nota para o filme: "))
        total += note

    if numAvalicoes > 0 :
        media = total / numAvalicoes
    else:
        media = 0

    return media

print(f"A media de avaliações é: {calcular():.2f}")

# 3 função para cadastra um filme

def cadastraFilme():
    nome = input("Digite o nome do Filme:")
    anoLancamento = int(input("Digite o ano de lançamento:"))
    note = float(input("Digite Uma nota:"))