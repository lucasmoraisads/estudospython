"""
* args - utilizamos quendo não sabemos quantos argumento queremos em uma função
* 0s argumentos são pasados com uma tupla
"""

def sum (*num):
    sum_total = 0
    for n in num:
        sum_total += n
    print(f"Some é : {sum_total}")


sum(7)
sum(3,56, 67, 88)