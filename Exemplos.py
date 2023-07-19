'''s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n
print('O somátorio de todos os valores foi {} '.format(s))'''

#Contagem regressiva de 10 até 0, com uma pausa de 1 segundo entre eles

'''from time import sleep
for c in range(10, -1, -1): # para realizar contagem regressiva incluir -1, -1
    print(c)
    sleep(1)
print('BUM!')'''

#Mostrar na tela todos os números pares que estão no intervalo de 1 a 50.
'''for pares in range(1, 51): #se quiser reduzir o n de laços, retira o if e inclui (2, 51, 2):
    if pares % 2== 0:
        print(pares, end=' ')
print('FIM')'''

#Calcule a soma entre os números múltiplos de três no intervalo 1 até 500
'''soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1
        soma = soma + c
print('A soma de todos os valores é de {} e a quantidade de valores encontrados foi de {}'.format(soma, cont))'''

#Refaça a calculadora utilizando o laço for.
'''num = int(input('Digite um número para ver sua tabuada: '))
for c in range(1, 11):
    print('{} x {:2} = {} '.format(num, c, num*c))'''

# Ler 6 números inteiros e mostre a soma apenas dos pares. Se o valor digitado for impar desconsidere.
'''soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite o {}° número: '.format(c)))
    if num % 2 == 0:
        soma = soma + num
        cont += 1
print('Você informou {} números pares e a soma foi {} '.format(cont, soma))'''

#Ler o primeiro termo e a razão de uma Progressão Aritimética. Mostre os 10 primeiros termos da PA
'''primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
décimo = primeiro + (10 - 1) * razão
for c in range(primeiro, décimo, razão):
    print('{} '.format(c), end='=> ')
print('FIM')'''

# Ler um número inteiro e dizer se ele é ou não um número primo
#número primo é dividido por 1 e por ele mesmo
'''num = int(input('Digite um número: '))
tot = 0
for c in range(1, num + 1):
   if num % c == 0:
       print('\033[34m', end='')
       tot += 1
   else:
        print('\033[33m', end='')
        print('{} '.format(c),end='')
print('O número  {} foi dívisivel {} vezes'.format(num, tot))
if tot == 2:
    print('Ele é primo!')
else:
    print('Ele não é primo!')'''

#Ler uma frase e dizer se ela é um palíndromo
'''frase = str(input('Digite uma frase: ')).strip().upper()
plrv = frase.split()
jnt = ''.join(plrv)
invr = ''
for letra in range(len(jnt) - 1, -1, -1):
    invr += jnt[letra]
if invr == jnt:
    print('Temos um palindromo!')
else:
    print('A frase digitada não é um palíndromo')'''
#Ler o ano de nascimento de sete pessoas e dizer quantas pessoas já sao + e quantas são - de idade.
'''from datetime import date
tot = 0
cont = 0
for ano in range(1, 8):
    nasc = int(input('Em qual ano a {}º pessoa nasceu '.format(ano)))
    atual = date.today().year
    idade = atual - nasc
    if idade <= 18:
        tot += 1
    else:
        cont += 1
print('No total existem {} pessoas maiores de idade e {} pessoas menores de idade '.format(cont, tot))'''

#Ler o peso de 5 pessoas e no final mostrar qual foi o menor e o maior peso lido.
'''maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi de {}Kg '.format(maior))
print('O menor peso lido foi de {}Kg '.format(menor))'''
# Ler o nome, idade e sexo de 4 pessoas, mostrar a média de idade, qual o nome do homem mais velho e quantas mulheres tem - de 20 anos.
from datetime import date
masculino = 0
feminino = 0
id = 0
for g in range(1, 5):
    nome = str(input('Digite o seu nome: '))
    sexo = str(input('Digite seu sexo: '))
    idade = int(input('Qual a sua idade: '))
    if sexo == masculino:
        nome = masculino + 1
    if sexo == feminino:
        nome = feminino + 1
print('O total de homens é de {} '.format(masculino))
print('O total de mulheres é de {} '.format(feminino))

