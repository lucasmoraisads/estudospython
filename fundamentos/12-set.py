filmesSet = {"Deadpool", "Esquadrão Clasee a", "Nimona", "Como treinar seu dragão", "os simpsons", "hacker"}

print(type(filmesSet))

#1 busca o tamanho 

print(len(filmesSet))

# 2 TRUE E 1 são considerado a mesma coisa

example = {"Nimona", True, 1, 8.9}

print(example)

# 3 adicionar um item de um set em outro set

filmesSet.update(example)

print(filmesSet)

# 4 removendo item no set

filmesSet.remove(True)
filmesSet.remove(8.9)

print(filmesSet)