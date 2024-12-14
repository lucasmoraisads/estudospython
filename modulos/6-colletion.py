from collections import Counter, namedtuple, deque
from operator import itemgetter

# 1 lista de frutas (Contagem)
frutas = ["Maça", "Pêra", "Banana", "Uva", "Melão", "Morango", "Manga", "Laranja", "Maça-verde", "Maça", "Pêra", "Banana", "abacaxi",
          "Tangerina", "Pocan"]



print(frutas) 
print(Counter(frutas))

# 2 - utilizar uma tupla nomeada

game = namedtuple('gane', ['name', 'preco', 'nota'])
g1 = game("fifa 23", 90.56, 8.5)
g2 = game("Resident evil ", 100.00, 9.0)
print(g1)
print(g2)

# 3 Ordenando dicionarios

estudantes = {"Pedro": 23, "Lucas": 28, "João": 32, "Beatriz": 19, "Carlos": 40, "Davila": 26, "Geovana":26, "Debora": 26}
a = sorted(estudantes.items(), key=itemgetter(0))
print(a)

# 4 utilizando uma fila em ambas as extremidades 

