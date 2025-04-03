# Exercicio 1
print("Digite 3 numeros para testarmos qual é o maior...")
numero_1 = int(input())
numero_2 = int(input())
numero_3 = int(input())
if numero_1 > numero_2 and numero_1> numero_3:
    print( f"O maior numero é {numero_1}")
elif numero_2 > numero_3:
    print( f"O maior numero é {numero_2}")
else:
    print( f"O maior numero é {numero_3}")

# Exercicio 2
num_dia = int(input("Digite um numero de 1 a 7..."))
if num_dia == 1: print( f"O numero {num_dia} corresponde a Segunda-feira.")
if num_dia == 2: print( f"O numero {num_dia} corresponde a Terça-feira.")
if num_dia == 3: print( f"O numero {num_dia} corresponde a Quarta-feira.")
if num_dia == 4: print( f"O numero {num_dia} corresponde a Quinta-feira.")
if num_dia == 5: print( f"O numero {num_dia} corresponde a Sexta-feira.")
if num_dia == 6: print( f"O numero {num_dia} corresponde a Sábado.")
if num_dia == 7: print( f"O numero {num_dia} corresponde a Domingo.")

# Exercicio 3
dividendo = int(input("Digite o dividendo..."))
divisor = int(input("Digite o divisor..."))
if divisor != 0:
    print( f"{dividendo} dividido por {divisor} é: ", dividendo/divisor)
else:
    print("Não existe divisão por 0.")

# Exercicio 4
print("Digite o valor dos três lados do triangulo...")
lado_1 = int(input("Lado 1:"))
lado_2 = int(input("Lado 2:"))
lado_3 = int(input("Lado 3:"))
if lado_1 == lado_2 and lado_1==lado_3:
    print("Esse é um triangulo Equilátero")
elif lado_1 == lado_2 or lado_1==lado_3 or lado_2 == lado_3:
    print("Esse é um triangulo Isosceles")
else:
    print("Esse é um triangulo Escaleno")

# Exercicio 5
salario_usuario = float(input("Olá, digite seu salário: "))
imposto = 0
if salario_usuario > 3000:
    imposto = salario_usuario * 0.2
else:
    imposto = salario_usuario * 0.1
print( f"O seu imposto a pagar é R${imposto:.2f}.")

# Exercicio 6
for numero in range(1,11):
    print(numero)

# Exercicio 7
soma = 0
for i in range(1,101):
    soma += i
print( f" A soma dos numeros de 1 a 100 é: {soma}")

# Exercicio 8
numero_tabuada = int(input("Digite um numero e te darei a tabuada de 1 a 10..."))
for i in range(1,11):
    print( f"{numero_tabuada} X {i} = ", numero_tabuada*i)

# Exercicio 9
string = input("Digite uma palavra ou frase...")
contador = 0
for letra in string:
    if letra == 'a' or letra == 'A':
        contador +=1
print( f"A sua palavra/frase contem {contador} letras 'A'")

# Exercicio 10
soma =0
for i in range(5):
    soma += int(input("Digite um numero para somar: "))
print( f"A soma dos numeros digitados é {soma}.")