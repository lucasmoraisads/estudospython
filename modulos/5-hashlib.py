import hashlib

# 1 veriificar os algoritmo disponiveis

print(hashlib.algorithms_available)

# 2- verificar algoritmos de acordo com o SO

print(hashlib.algorithms_guaranteed)

# 3 utilizando o SHA256

algoritmo = hashlib.sha256()
print(algoritmo.digest())
mensagem = "A melhor forma de prover o futuro é crialo".encode()
algoritmo.update(mensagem)
print(algoritmo.hexdigest())

# 4 utlizando o MD5

md5 = hashlib.md5()
md5.update(mensagem)
print(md5.hexdigest())
