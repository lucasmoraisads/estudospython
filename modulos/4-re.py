import re

text = "Udemy - uma plantaforma com muitos cursos"
# 1 - mapear indice inicial e indice final
# o r significa uma raw string (string bruta)

match = re.search(r'uma plantaforma', text)   
print(f"Indice inicial: {match.start()}")
print(f"Indice final: {match.end()}")

# 2 - Buscando o índice que possui ponto

site = 'https://udemy.com.br'
match = re.search(r'\.', site)
print(match)

# 3 - Buscar uma lista de caracteres dentro de uma frase 

pattern = "[g-m]"
resultado = re.findall(pattern, text)
print(resultado)

# 4 - verificando o início de uma string
