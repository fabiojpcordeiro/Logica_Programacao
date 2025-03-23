# # Exercício 01
# nome = input("Olá caro usuário, por favor digite seu nome...")
# print( f"Seja bem vindo {nome} a nossa plataforma!")

# # Exercício 02
# dec_01 = float(input("Digite dois números com casa decimal: "))
# dec_02 = float(input("Digite o segundo número: "))
# print( f"A soma de {dec_01} e {dec_02} é  {dec_01+dec_02:.2f}")

# # Exercicio 03
# int_01 = int(input("Digite o primeiro numero: "))
# int_02 = int(input("Digite o segundo numero: "))
# operador = input("Digite o tipo de operação: ")
# if(operador == "+"):
#     print( f"O resultado de {int_01}{operador}{int_02} é {int_01+int_02}")
# elif(operador == "-"):
#     print( f"O resultado de {int_01}{operador}{int_02} é {int_01-int_02}")
# elif(operador == "/"):
#     print( f"O resultado de {int_01}{operador}{int_02} é {int_01//int_02}")
# elif(operador == "*"):
#     print( f"O resultado de {int_01}{operador}{int_02} é {int_01*int_02}")

# # Exercicio 04
# # Excluindo anos bissextos e assumindo 1 mês = 30 dias.
# idade_ex04 = int(input("Caso usuário, digite sua idade em anos..."))
# print( f"Você tem {idade_ex04 * 12} meses ou {idade_ex04 * 365} dias de vida!!!")

# # Exercicio 05
# nota_01 = float(input("Digite sua primeira nota: "))
# nota_02 = float(input("Digite sua segunda nota: "))
# nota_03 = float(input("Digite sua terceira nota: "))
# media = (nota_01+nota_02+nota_03)/3
# print( f"A sua média final é: {media:.2f}")

# Exercicio 06

# nota01 = float(input("Digite a nota do primeiro bimestre: "))
# nota02 = float(input("Digite a nota do segundo bimestre: "))
# media_final = (nota01+nota02)/2
# if media_final >=7:
#     print ( f"Sua média é: {media_final} e você está aprovado")
# else:
#     print ( f"Sua média é: {media_final} e você está reprovado")

# # Exercicio 07
# valor_produto = float(input("Digite o valor do produto: "))
# dinheiro_pago = float(input("Digite o dinheiro pago: "))
# if(dinheiro_pago >= valor_produto):
#     print( f"o seu troco é R${dinheiro_pago - valor_produto:.02f}")
# else:
#     print("Dinheiro insuficiente!!!")

# Exercicio 08
num_horas = int(input("Digite o numero de horas: "))
print ( f"{num_horas} horas é equivalente a {num_horas*60} minutos ou {num_horas*3600} segundos")