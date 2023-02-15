# Criação de uma lista vazia para armazenar as confirmações de presença
confirmacoes = []

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
    
    # Adiciona a confirmação de presença à lista
    confirmacoes.append((nome, confirmacao))
    
# Exibe a lista de confirmações de presença
print("\nLista de confirmações de presença:")
for nome, confirmacao in confirmacoes:
    print(f"{nome}: {confirmacao}")