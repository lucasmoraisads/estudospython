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
<<<<<<< Updated upstream
    
    
# 4 avaliação do filme

nomeFilme = input("Digite o nome do filme: ")
notaFilme = int(input("Digite qunatas avaliações que deseja fazer: "))

total = 0

for i in range(notaFilme):
    nota = float(input("Digite a nota para o filme: "))
    total += nota
    
    
if notaFilme > 0:
    media = total / notaFilme
    
else:
    media = 0

print(f"A media de avaliação do Filme {nomeFilme} é : {notaFilme:.2f}")
     
=======


# 4 avaliação do filme

nomeFilme = input("Digite o nome do filme: ")
notaFilme = float(input("Digite quantas avaliações deseja fazer: "))

toral = 0

for i in range(notaFilme):
    note = float(input("Digite a nota para o filme:"))
    toral += note

>>>>>>> Stashed changes
