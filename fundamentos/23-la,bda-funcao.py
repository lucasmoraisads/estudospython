# função pontencia de um numero

power = lambda num: num ** 2

# 2 função que verifica se o numero e par

par = lambda x: x % 2 == 0

#  Função que divide um numero por outro

divide = lambda x, y: x / y

# função que inverte uma string 

inverter = lambda s: s[::-1]


print(power(5))
print(power(8))
print()
print(par(23))
print(par(20))
print()
print(divide(10, 3))
print(divide(100, 5))
print()
print(inverter("Lucas"))



# funcionalidades relacionadas a filmes

filmeList = ["Mascara", "Nimona", "Esquadrão Classe A", "Os Simpsons", "Como treinar seu dragão", "trancendente"]
notaFilme = {
    "Mascara" : [7.8, 5.7, 8.9],
    "Nimona" : [8.8, 7.7, 8.9],
    "Esquadrão Classe A" : [9.8, 8.7, 10],
    "Os Simpsons" : [9.0, 8.9, 8.9],
    "Como treinar seu dragão" : [7.8, 9.7, 8.9],
    "trancendente" : [6.8, 8.7, 9.9],
}

# função para calcular a media de avaliação de um filme

mediaAvalicao = lambda nomeFilme: sum(notaFilme[nomeFilme]) / len(notaFilme)

# função que verifica se o filme esta na lista

filmeNaLista = lambda nomeFilme: nomeFilme in filmeList

# função que recomenda filme com base na avaliação media

recomendacaoFilme = lambda nomeFilme: f"Comendo Assistir {nomeFilme} com média {mediaAvalicao(nomeFilme):.2f}"

print(f"Média de Avaliação do filme Mascara: {mediaAvalicao("Mascara")}")
print(f"Nimona está n alista : {filmeNaLista("Nimona")}")
print(f"{recomendacaoFilme("Como treinar seu dragão")}")