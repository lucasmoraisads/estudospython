# 1 listando numeros menores que 4 de 0 a 10

listaNumero = [ i for i in range(10) if i < 4]

print(listaNumero)

# lista filme

filmesList = ["Titanic", "Nimona", "Deadpool", "Mascara"]

# 2 filtrando por letra 

filtro_letra = [filme for filme in filmesList if 'i' in filme.lower() ]

print(filtro_letra)

# 3 filmes que eu assisti 

filmeAssisti = [ filme for filme in filmesList if filme != "Mascara"] 

print(filmeAssisti)

# 4 encontrando o filme pole nome

while True:
    buscarFilme = input("Digite o nome do filme para busca na lista ( ou sair para encerrar ): \n")
    if buscarFilme.lower() == "sair":
        print("Programa encerrado") 
        break

    encontraFilme = [ filme for filme in filmesList if buscarFilme.lower() in filme.lower()]
    if encontraFilme:
        print(f"Filme(s) encontrado(s) com o nome: {buscarFilme}")
        for encontraFilme in encontraFilme:
            print(encontraFilme)
    else:
        print(f"Nenhum filme encontrado com o nome {buscarFilme}. Tente Novamente")