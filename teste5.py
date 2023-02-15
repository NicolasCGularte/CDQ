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
    valor_pix = 0.0
    descricao_pix = input("Por favor, informe ao que se refere o pagamento do PIX (ex: churrasco, mensalidade, etc.): ")
    if descricao_pix.lower() == "churrasco do dia":
        if nome in confirmacoes and confirmacoes[nome][data_confirmacao].lower() == 'sim':
            valor_pix = 20.0
        else:
            valor_pix = 25.0
    elif descricao_pix.lower() == "mensalidade":
        num_meses = int(input("Por favor, digite o número de meses para pagar a mensalidade: "))
        valor_pix = 10.0 * num_meses
    
    if valor_pix > 0.0:
        numero_pix = "(xx)9-1234-5678"
        print(f"Por favor, efetue o pagamento via PIX no número {numero_pix} no valor de R${valor_pix:.2f} com a descrição '{descricao_pix}'.")
    else:
        print("Não foi possível identificar o valor do PIX a ser pago com a descrição informada.")
else:
    print("Obrigado pela confirmação de presença!")