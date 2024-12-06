# nomeFilme = input("Digite nome do Filme:\n")
# anoLancamento = int(input("Digite ano lançamento:\n"))
# nota = float(input("Digite nota de avaliação do Filme:\n"))

# # verifica se o filme e recomendado

# if nota > 8.0 and anoLancamento > 2015:
#     print(f"O filme {nomeFilme} é muito bom. Recomendo!")
# else:
#     print(f"O Filme {nomeFilme} ainda não atigiu uma boa Nota!")

num1 = float(input("Digite primeiro número \n"))
num2 = float(input("Digite segundo número \n"))
operacao = input("Digite a operação a ser realizada (+ - / *)\n")


if operacao == "+":
    result = num1 + num2
elif operacao == "-":
    result = num1 - num2
elif operacao == "*":
    result = num1 * num2
elif operacao == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        print("Erro: Divisõ por 0 ")
        result = 0
else:
    print("Operação Invalida")
    result = 0

print(f"Resultado da operação é: {result:.2f}")