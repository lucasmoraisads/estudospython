
filmesLista = ["Deadpool", "Esquadrão Clasee a", "Nimona", "Como treinar seu dragão", "os simpsons", "hacker"]

# 1 tamanho lista
print(len(filmesLista))

# 2 recupera o item de lista pelo o indece

print(filmesLista.index("Nimona"))

# 3 adicionar o item ao final da lista

filmesLista.append("transcendente")
print(filmesLista)

# 4 Ordena a lista

filmesLista.sort()
print(filmesLista)

# 5 copia os itens de uma lista para outra

filmesCopy = filmesLista.copy()
filmesCopy.remove("hacker")
print(filmesCopy)

# 6 rmove todos os itens da lista

filmesLista.clear()
print(filmesLista)