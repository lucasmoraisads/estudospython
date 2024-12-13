import hashlib

# 1 veriificar os algoritmo disponiveis

print(hashlib.algorithms_available)

# 2- verificar algoritmos de acordo com o SO

print(hashlib.algorithms_guaranteed)