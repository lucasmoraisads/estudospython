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