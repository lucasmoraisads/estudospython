filme = "Esquadrão classe a"
descricaoFilme = """
 deadpool, filme muito zueiro,
 com um cara muito, filho da puta
"""

print(filme.upper())# tudo maiúsculo
print(filme.lower())# tudo minusculo
print(filme.capitalize())#retorna a primeira maiuscula
print(filme.title()) #retorna a primeira maiuscula
print(filme.center(5, "-")) # retorna a string centralizada com caracter de preenciemnto
print(filme.find("e"))# retorna possição de um determinado caracterer
print(filme.find("s"))# Conta caractere
print(filme.replace("classe", "suicida")) #altera um elemento por outro
print(descricaoFilme.split(","))