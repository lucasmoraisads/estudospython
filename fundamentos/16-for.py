# 0 lista de filmes
filmesList = ["Titanic", "Nimona", "Deadpool", "Mascara"]
numeros = [10, 20, 30, 40, 50, 60 ,70, 80 ,90, 100]

# 1 iterando valores da lista

for filme in filmesList:
    print(filme)


# 2 Quando a condição for atendida ele encerra o loop for
for filme in filmesList:
    if filme == "Deadpool":
        break
    print(filme)

# 3 quando a condição for e atendida, o loop vai para proxima  iteração
print("\n")
for filme in filmesList:
    if filme == "Deadpool":
        continue
    print(filme)