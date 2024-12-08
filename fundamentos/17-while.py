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