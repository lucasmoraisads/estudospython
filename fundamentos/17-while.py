# Lista filme
filmesList = ["Titanic", "Nimona", "Deadpool", "Mascara"]

# 1 interando valores no while

index = 0

while index < len(filmesList):
    print(filmesList[index])
    index += 1
    
# 2 quando a condição for atendida, o loop e encerrado

index = 0

while index < len(filmesList):
    if filmesList[index] == "Deadpool":
        break
    print(filmesList[index])
    index += 1
    
# 3 quando a condição for atendida o loop vai para a proxima iteração

index = 0

while index < len(filmesList):
    if filmesList[index] == "Deadpool":
        index += 1
        continue
    print(filmesList[index])
    index += 1
    
# 4 avaliação do filme com while

nomeFilme = input("Digite o nome do filme: ")
notaFilme = int(input("Digite qunatas avaliações que deseja fazer: "))

total = 0
count = 0

while count < notaFilme:
    note = float(input("Digite a nota para o Filme: "))
    total += note
    count += 1 
    
if notaFilme > 0:
    media = total / notaFilme
    
else:
    media = 0

print(f"A media de avaliação do Filme {nomeFilme} é : {notaFilme:.2f}")