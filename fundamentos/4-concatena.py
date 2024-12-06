name = input("Digite o nome do Filme:")
anoLancamento = int(input("Digite o ano de lançamento:"))
note = float(input("Digite Uma nota:"))

print("Dados Do Filme")
print("========")
#primeira alternativa

print("Nome do Filme:", name)
print("Ano de Lançamento:", anoLancamento)
print("Nota do Filme:", note)

#alternativa 2

print("Nome do Filme: ", name, "\nLançamento: ", anoLancamento, "\nNota: ", note)

#alternativa 3

print(f"Nome do Filme: {name}\n"
      f"Ano lançamento: {anoLancamento}\n"
      f"Nota: {note}")