# Importa a biblioteca datetime para manipular datas
import datetime

# Criação de um dicionário vazio para armazenar as confirmações de presença
confirmacoes = {}

# Solicita a data de confirmação
data_confirmacao = input("Por favor, digite a data de confirmação (no formato dd/mm/aaaa): ")
dia, mes, ano = map(int, data_confirmacao.split("/"))
data_confirmacao = datetime.date(ano, mes, dia)

# Loop para coletar as confirmações de presença
while True:
    nome = input("Por favor, digite o seu nome (ou 'sair' para encerrar o programa): ")
    
    # Verifica se o usuário deseja sair
    if nome.lower() == 'sair':
        break
    
    confirmacao = input("Você estará presente? (sim/não): ")
    
    # Verifica se a resposta é válida
    while confirmacao.lower() not in ['sim', 'não']:
        confirmacao = input("Resposta inválida. Por favor, digite 'sim' ou 'não': ")
    
    # Adiciona a confirmação de presença ao dicionário
    if nome not in confirmacoes:
        confirmacoes[nome] = {}
    confirmacoes[nome][data_confirmacao] = confirmacao
    
# Exibe a lista de confirmações de presença para a data selecionada
print(f"\nLista de confirmações de presença para {data_confirmacao.strftime('%d/%m/%Y')}:")
for nome, confirmacoes_na_data in confirmacoes.items():
    if data_confirmacao in confirmacoes_na_data:
        confirmacao = confirmacoes_na_data[data_confirmacao]
        print(f"{nome}: {confirmacao}")
        
# Pergunta ao usuário se ele deseja efetuar um pagamento via PIX
pagamento = input("Deseja efetuar um pagamento via PIX? (sim/não): ")
if pagamento.lower() == 'sim':
    # Insira aqui o código para efetuar o pagamento via PIX
    print("Pagamento via PIX efetuado com sucesso!")
else:
    print("Obrigado pela confirmação de presença!")