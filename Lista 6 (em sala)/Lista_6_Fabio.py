#Ex 01
num = 1
while num <= 15:
    if num%3 == 0:
        print(num)
    num += 1 

#Ex 02
num = 1
while num <= 5:
    print("Python")
    num += 1

#Ex 03
num = 2
while num <= 62:
    if num % 2 == 0:
        print(num)
    num +=1

num = 2
while num <=62:
    print(num)
    num += 2

#Ex 04
counter = 0
while counter <=5:
    print(counter)
    if counter == 3:
        break
    counter += 1

#EX 05
counter = 1
while counter <= 3:
    print("Contando...")
    counter += 1
print("Fim!")

#Ex 06
contador = 500
while contador >= 1:
    print(contador)
    contador -= 1

# Ex 07
num = 1
while num <= 5:
    if num == 3:
        num += 1
        continue
    print(num)
    num += 1

#Ex 08
contador = 1
soma = 0
while contador <= 50:
    soma += contador
    contador += 1
print(soma)

#Ex 09
counter = 1
while counter <= 30:
    print(counter)
    counter += 1

#Ex 10
while True:
    num = int(input("Digite numeros inteiros ou 10 para parar..."))
    if num == 10:
        break
    print( f"Você digitou {num}.")