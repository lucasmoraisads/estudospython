"""
* args - utilizamos quendo não sabemos quantos argumento queremos em uma função
- 0s argumentos são pasados com uma tupla
** alem dos valores podemos passar tambem as respectivas chave para cada argumento
- Os argumento são pasado como um dicionario
"""

def sum (*num):
    sum_total = 0
    for n in num:
        sum_total += n
    print(f"Some é : {sum_total}")


sum(7)
sum(3,56, 67, 88)

# 2 Apresentação de cursos

def presentacao(**data):
    for key, value in data.items():
        print(f"{key} - {value}")

print("Lista de Cursos")
presentacao(nome="Python", Categoria="Beck-end", nivel="Iniciante")
presentacao(nome="JavaScript", Categoria="Beck-end", nivel="Médio")
presentacao(nome="Rede de Computadores", Categoria="TI", nivel="Avançado")