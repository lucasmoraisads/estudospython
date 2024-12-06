import pprint

filmesDic = {
    "DeadPool":{
    "ano": 2018,
    "nota": 8.9,
    "genero": ["Ação", "Comedia"]},

    "Nimona": {
    "ano": 2023,
    "nota": 8.0,
    "genero": ["Ação", "Animação"]},

    "Mr.Rbot":{
    "ano": 2018,
    "nota": 8.9,
    "genero": ["Ação", "Drama", "Suspense"]}

}
pp = pprint.PrettyPrinter(depth=4)
pp.pprint(filmesDic)

# 1 - buscar uma informação em um dicionario aninhado

print(filmesDic["Mr.Rbot"]["genero"])

# 2 - adicionar novo item

filmesDic["Nimona"]["direto"] = "Troy Quane"

print(filmesDic["Nimona"])

# 3 - excluir 