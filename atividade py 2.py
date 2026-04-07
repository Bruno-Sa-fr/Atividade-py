#número inteiro positivo ou negativo
a = int(input("Digite o número:"))
if(a >= 0):
    print("positivo")
else:
    print("negativo")

#converter para inteiro e dobrar o valor
a = (input("Digite o número:"))
a = int(a)
print(2 * a)

#ler valor de entrada e tipo
a = (input("Digite o número"))
print("O valor de a é", a, type(a))

#ler número par ou ímpar
a = float(input("Digite o número"))
if (a % 2 == 0):
    print("par")
else:
    print("ímpar")

#converter para inteiro e triplicar o valor
a = (input("Digite o número:"))
a = int(a)
print(3 * a)

#ler dois números e saber qual é o maior
a = float(input("Digite o primeiro número:"))
b = float(input("Digite o segundo número:"))
if( a > b):
    print("a é maior que b")
else:
    print("b é maior que a")

#verificar se um número é maior, menor ou igual a 10
a = float(input("Digite o número"))
if(a > 10):
    print("Maior que 10")
else:
    print("Menor ou igual a 10")

#raiz de número positivo
a = float(input("Digite o número:"))
if(a >= 0):
    print(a ** 0,5)
else:
    print("Número inválido")

#converter para float e mostrar a metade
a = (input("Digite o número:"))
a = float(a)
print(a / 2)

#informar se o número está entre 0 e 10 ou não
a = float(input("Digite o número:"))
if(0 < a < 10):
    print("Dentro do intervalo")
else:
    print("Fora do intervalo")

#par positivo, negativo e ímpar
a = float(input("Digite o número:"))
if(a > 0) and (a % 2 == 0):
    print("Par positivo")
elif(a < 0) and (a % 2 != 0):
    print("Par negativo")
else:
    print("Ímpar")

#somar dois números e mostrar qual é o maior ou se são iguais
a = float(input("Digite o primeiro número:"))
b = float(input("Digite o segundo número:"))
print(a + b)
if(a > b):
    print("a é maior que b")
elif(a < b):
    print("b é maior que a")
else:
    print("a e b são iguais")

#se o número for maior que 100 mostrar metade, se não, o dobro
a = float(input("Digite o número:"))
if(a > 100):
    print(a / 2)
else:
    print(a * 2)

#se o número é múltiplo de 3 ou não
a = (input("Digite o número:"))
a = int(a)
if(a % 3 == 0):
    print("Múltiplo de 3")
else:
    print("Não é múltiplo")

#se o número estiver entre 10 e 20 ou não
a = float(input("Digite o número:"))
if(10 < a < 20):
    print("Dentro")
else:
    print("Fora")

#se o tipo do número for numérico, mostrar o quadrado
a = float(input("Digite o número:"))
print(type(a))
if(type(a) == float) or (type(a) == int):
    print(a ** 2)

#se á menor de idade, adulto ou idoso
a = int(input("Digite a idade:"))
if(a < 18):
    print("Menor de idade")
elif(18 < a <59):
    print("Adulto")
else:
    print("Idoso")

#se é par positivo ou negativo, ímpar positivo ou negativo ou neutro
a = float(input("Digite o número:"))
if(a % 2 == 0) and (a > 0):
    print("Par positivo")
elif(a % 2 == 0) and (a < 0):
    print("Par negativo")
elif(a % 2 != 0) and (a > 0):
    print("Ímpar positivo")
elif(a % 2 == 0) and (a < 0):
    print("Ímpar negativo")
else:
    print("Neutro")

#se são iguais ou diferentes, e se diferentes mostrar a diferença
a = float(input("Digite o primeiro número:"))
b = float(input("Digite o segundo número:"))
if(a == b):
    print("a e b são iguais")
else:
    print("a e b são diferentes", abs(a - b))

#se o número está entre 0 e 100, se não, mostrar na tela
a = float(input("Digite o número:"))
if(a < 0) or (a > 100):
    print(a)
    
