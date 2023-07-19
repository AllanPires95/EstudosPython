import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC02d069e9b7b729e3a5b669fa59dd0be8"
# Your Auth Token from twilio.com/console
auth_token = "6a14fd44b14b775546c4e918c1346ff1"

client = Client(account_sid, auth_token)

#pandas - comunicação com excel
#openpxl - comunicação com excel
# twilio - sms
# Passo a passo de solução
# Abrir os arquivos em excel
lista_contas = ['Contas']
tabela_valor = pd.read_excel('Contas.xlsx')
#se fosse para executar várias vezes, utilizaria um tab para identar p dentro
#incluir f formatar a string

#for mes in lista_contas - para cada mês dentro de lista de contas eu executo um código, se eu tivesse feito jan, fev.
#print (mes)
#tabela_valor = pd.read_excel(f'{mes}.xlsx
#print(tabela_valor) #usar tab para incluir dentro do for
if (tabela_valor['Valor'] > 4000).any(): #.any para verificar se algum valor da coluna é maior que o valor
    contas = tabela_valor.loc[tabela_valor['Valor'] > 4000, 'Contas']#.values[0] tira a tabela e trás só a informação
    valor = tabela_valor.loc[tabela_valor['Valor'] > 4000, 'Valor'] #.loc ajuda a localizar a linha da tabela
    print(f' A quantidade de contas do mês é de. Contas: {contas}, Valor {valor}.') #se for para incluir o mes, caso já identado f
    message = client.messages.create(
        to="+13974049540",
        from_="+18789991406",
        body=f' A quantidade de contas do mês é de. Contas: {contas}, Valor {valor}.')

    print(message.sid)




#criar conta no twilio e incluir as informações

# Valor de contas acima de 20 reais

# Se for maior de 4 mil, envia SMS - com o valor, o mês, e as contas.

