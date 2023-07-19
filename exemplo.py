'''tempo = int(input('Quantos anos tem seu carro? '))
print('Seu carro é novo' if tempo<=3 else ' Seu carro é velho')
print('---FIM--')'''

'''nome = str(input('Qual é o seu nome? '))
if nome == 'Allan':
    print('Qur nome lindo você tem!')
else: print('Ainda da tempo de trocar de nome {} '.format(nome))
print('Bom dia {}!'.format(nome))'''

'''nm = str(input('Digite o seu nome: '))
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2)/2
print('A sua média foi {:.1f}'.format(m))
if m >= 6.0:
    print('Sua média foi boa {}!'.format(nm))
else: print('Precisa estudar mais {}!'.format(nm))'''

'''from random import randint
from time import sleep
computador = randint(0, 5) #FAZ O COMPUTADOR SORTEAR
print('-=-' * 10)
print('Vou pensar em algum número entre 0 e 5. Tente adivinhar...')
print('-=-' * 10)
jogador = int(input('Em qual número eu pensei? ')) #Para o jogador adivinhar
print("Aguarde....")
sleep(3)
if jogador == computador:
    print('Você ganhou! Parabéns!!! ')
else:
    print("Eu ganhei HAHAHHAHAHAHA, Eu pensei no número {} e não no {}! ".format(computador, jogador))'''

'''carro = float(input('Qual a velocidade do carro? '))
print('-=-' * 10)
km = (carro - 80) * 7
if carro > 80:
    print('Você será multado!, Deverá pagar uma multa de R$ {} '.format(km))
else:
    print('Você está dentro do limite da via! ')'''

'''from time import sleep
numero = int(input('Digite um número qualquer: '))
resultado = numero % 2
print("Wait....")
sleep(2)
if resultado == 0:
    print('O numero {} é PAR!' .format(numero))
else:
    print('O número {} é IMPAR!! '.format(numero))'''

'''distância = float(input('Qual a distância da sua viagem? '))
print('Você irá fazer uma viagem de {}Km'.format(distância))
if distância <= 200:
    preço = distância * 0.50
else:
    preço = distância * 0.45
print('O preço da sua passagem será de R${:.2f} '.format(preço))'''

'''from datetime import date
ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year #pega o ano atual configurado na máquina
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0: #and e or equivalente a e/ou.
    print('O ano {} é bissexto'.format(ano))
else:
    print('O ano {} não é bissexto'.format(ano))'''

'''a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
c = int(input('Digite o terceiro valor: '))
#Verificando quem é o maior
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
#Verificando quem é o maior
maior = a
if b>a and b>c:
    maior = b
if c>b and c>a:
    maior = c
print('O menor valor digitado foi o {} '.format(menor))
print('O maior valor digitado foi de {} '.format(maior))'''

'''salario = float(input('Digite o valor do seu salário: R$ '))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print('Seu salário era de R$ {:.2f} e agora é de R$ {:.2f}!.'.format(salario, novo))'''

'''us = float(input('Digite o comprimento da primeira reta: '))
us1 = float(input('Digite o comprimento da segunda reta: '))            
us3 = float(input('Digite o comprimento da terceira reta: '))
if us < us1 + us3 and us1 < us + us3 and us3 < us + us1:
    print('Os comprimentos podem formar triângulo: ')
else:
    print('Os comprimentos não podem formam um triângulo: ')'''
