'''nome = str(input('Qual é o seu nome?: '))
if nome == 'Allan':
    print('Nome legal!')
elif nome == 'Joao' or nome == 'Maria' or nome == 'José':
    print('Seu nome é bem popular no Brasil! ')
else:
    print('Seu nome é normal!!')
    print('Tenha um bom dia {}! '.format(nome))'''

'''casa = float(input('Valor da casa: R$ '))
salário = float(input('Qual o seu salário: R$ '))
anos = int(input('Em quantos anos deseja pagar o financiamento?: '))
prestação = casa / (anos * 12)
mínimo = salário * 30 / 100
print('Para pagar a casa de R$ {:.2f} em {} anos'.format(casa, anos))
print('A prestação será de R$ {:.2f}'.format(prestação))
if prestação <= mínimo:
    print('Empréstimo pode ser concedido!')
else:2
    print('Empréstimo negado!')'''

'''num = int(input('Digite um número inteiro: '))
print('''#Escolha uma das bases para conversão:
#[ 1 ] converter para Binário
#[ 2 ] converter para Octal
#[ 3 ] converter para Hexadecimal''')
'''opção = int(input('Sua opção: '))
if opção == 1:
    print('{} convertido para binário é igual {} '.format(num, bin(num) [2:]))
elif opção == 2:
    print('{} convertido para octal é igual {} '.format(num,oct(num) [2:]))
elif opção == 3:
    print('{} convertido para Hexadecimal é igual {} '.format(num, hex(num) [2:]))
else:
    print('Digite uma opção válida!')'''

'''num = int(input('Digite um valor inteiro!: '))
num1 = int(input('Digite o segundo valor inteiro!: '))
if num > num1:
    print('O primeiro valor é maior! ')
elif num < num1:
    print('O segundo valor é maior!')
else:
    print('Os valores são iguais!')'''

'''from datetime import date
hoje = date.today().year
ano = int(input('Digite o ano de nascimento: '))
idade = hoje - ano
print('Quem nasceu em {}, tem {} anos em {} '.format(ano, idade, hoje))
if idade == 18:
    print('Você deve se alistar este ano!! ')
elif idade < 18:
    faltam = 18 - idade
    print('Ainda faltam {} anos para o alistamento' .format(faltam))
else:
    passou = idade - 18
    print('Você já deveria ter se alistado há {} anos.'.format(passou))'''

#Mostrar a média do aluno, - 5 = reprovado, 5 e 6,9 recupeção e 7 ou superior aprovado com 2 notas
'''n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
média = (n1 + n2) / 2
if média <5:
    print('Aluno(a) reprovado!, sua média foi de {:.1f} '.format(média))
elif média >= 5 and média <= 7:
    print('Aluno(a) de recuperação!, sua média foi de {:.1f} '.format(média))
else:
    print('Aluno(a) Aprovado!, sua média foi de {:.1f} '.format(média))'''

#Um programa que calcule a idade e mostre a categoria de um atleta. 9 a - Mirim, 14a - Infantil, 19a - Junior
#25a - Senior, +25a - Master
'''from datetime import date
atual = date.today().year
ano = int(input('Digite o ano do seu nascimento: '))
idade = atual - ano
if idade <= 9:
    print('Você tem {} anos e deverá competir no Mirim!'.format(idade))
elif idade >= 9 and idade <= 14:
    print('Você tem {} anos e deverá competir no Infantil!'.format(idade))
elif idade >15 and idade <=25:
    print('Você tem {} anos e deverá competir no Junior!'.format(idade))
else:
    print('Você tem {} anos e deverá competir no Master! '.format(idade))'''

# Construir um programa para definir os tipos de triangulo, sendo Equilátero, Isósceles e Escaleno
'''r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima podem formar um triângulo! ', end='')
    if r1 == r2 == r3:
        print('Equilátero')
    elif r1 != r2 != r3 != r1:
        print('Escaleno')
    else:
        print('Isósceles')

else:
    print('Os segmentos não formam um triângulo! ')'''

# Leitura de IMC, abaixo de 18.5 - peso, entre 18.5 e 25 peso ideal, 25 a 30 sobrepeso, 30 a 40 obesidade, + 40 Obesidade Mórida
'''altura = float(input('Digite sua altura: '))
peso = float(input('Digite o seu peso: '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print('O seu imc é de {:.1f}, Você está abaixo do peso! '.format(imc))
elif 18.5 <= imc < 25:
    print('O seu imc é de {:.1f}, Você está no peso ideal!  '.format(imc))
elif 25 <= imc < 30:
    print('O seu imc é de {:.1f}, Você está no sobrepeso! '.format(imc))
elif 30 <= imc < 40:
    print('O seu imc é de {:.1f}, Você está obeso!'.format(imc))
else:
    print('O seu imc é de {:.1f}, Você está em obesidade mórbida '.format(imc))'''

# Calculo do valor a ser pago por um produto, considerando seu preço, A vista - 10% desconto, cartão 5% de desconto, 2x
# preço normal, 3x ou + 20% de juros.

'''produto = float(input('Digite o valor do produto R$: '))
vista = produto - (produto * 10/100)
cartao = produto - (produto * 5/100)
parc1 = produto + (produto * 20/100)
print('''#Escolha a forma de pagamento
#[ 1 ] Pagamento à vista \ Cheque
#[ 2 ] Pagamento à vista no cartão de débito
#[ 3 ] Pagamento em 2x no cartão crédito
#[ 4 ] Pagamento em 3x ou mais no cartão de crédito''')
'''opcao = int(input('Digite a opção escolhida! '))
if opcao == 1:
    print('Você ganhou um desconto! O valor do seu produto era R$ {:.2f}, agora é de R$ {:.2f} '.format(produto, vista))
elif opcao == 2:
    print('Você ganhou um desconto! O valor do seu produto era R$ {:.2f}, agora é de R$ {:.2f} '.format(produto, cartao))
elif opcao == 3:
    print('O valor da sua compra é de R$ {:.2f} '.format(produto))
elif opcao == 4:
    print('O valor da sua compra era de R$ {:.2f}, agora é dé R$ {:.2f} '.format(produto, parc1))
else:
    print('Por favor, digite uma opção válida no sistema! ')'''

#Construir um game de jokenpo
'''from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''#Suas opções:
#[ 0 ] Pedra
#[ 1 ] Papel
#[ 2 ] Tesoura ''')
#jogador = int(input('Qual a sua jogada? '))
'''print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
print('-=' * 10)
print('Computador jogou {} '.format(itens[computador]))
print('Jogador jogou {} '.format(itens[jogador]))
print('-=' * 10)
if computador == 0: #computador jogou pedra
    if jogador == 0:
        print('Empate')
    elif jogador == 1:
        print('Jogador Vence!')
    elif jogador == 2:
      print('Computador Vence!!')
    else:
      print('Jogada Inválida!!')
elif computador == 1: #computador jogou papel
    if jogador == 0:
        print('Computador Vence!!')
    elif jogador == 1:
             print('Empate!!')
    elif jogador == 2:
         print('Jogador Vence!!')

    else:
        print('Jogada Inválida!!')
elif computador == 2: #computador jogou tesoura
    if jogador == 0:
        print('Jogador Vence!!')
    elif jogador == 1:
        print('Computador Vence!!')
    elif jogador == 2:
         print("Empate")
    else: 
        print('Jogada Inválida!!')'''

