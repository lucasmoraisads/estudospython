import statistics

# 1 Aplicando a media 

print(statistics.mean([23, 45, 67, 33, 87, 40]))

# 2 aplicando a mediana 

print(statistics.median([2, 5, 6, 8, 23, 78, 45, 98, 34, 36]))
print(statistics.median([1, 2, 3, 5, 7, 9]))

# 3 aplicando a moda

print(statistics.mode([2, 3, 6, 5, 2,4, 8, 4, 9, 2]))

# 4 desvio padrão

"""
Quanto mais proximo do zero for o desvio pedrão
siguinifica que os dados do conjunto estão menos dispersos
"""

print(statistics.stdev([1, 1.5, 3.5, 3.8, 5.9]))