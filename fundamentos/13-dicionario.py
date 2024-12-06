filmes = {
    "title":"Nimona",
    "Ano": 2024,
    "Nota": 8.9,
    "Genero": ["Ação", "Animação"]
}

print(filmes)
print(len(filmes))
print(type(filmes))

# 1 reupera um iten do dicionario

print(filmes["Genero"])
print(filmes.get("Nota"))

# 2 buscar apenas as chave do dicionario

print(filmes.keys())

# 3 apenas os valores

print(filmes.values())

# 4 buscar itens do dicionario com chave e valor

print(filmes.items())


# 5 adionar itens no dicionario

filmes["diretor"] = "Troy Quane"

print(filmes)

# 6 atualiza itens no dicionario

filmes.update({"Nota": 9.0})

print(filmes)

# 7 removendo iten no dicionario

filmes.pop("diretor")
print(filmes)