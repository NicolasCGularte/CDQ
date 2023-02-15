import datetime
import webbrowser

class ConfirmacaoPresenca:
    
    def __init__(self):
        self.confirmacoes = {}

    def coletar_confirmacoes(self):
        data_confirmacao = self._solicitar_data_confirmacao()

        while True:
            nome = input("Por favor, digite o seu nome (ou 'sair' para encerrar o programa): ")
            
            if nome.lower() == 'sair':
                break
            
            confirmacao = input("Você estará presente? (sim/não): ")
            
            while confirmacao.lower() not in ['sim', 'não']:
                confirmacao = input("Resposta inválida. Por favor, digite 'sim' ou 'não': ")
            
            if nome not in self.confirmacoes:
                self.confirmacoes[nome] = {}
            self.confirmacoes[nome][data_confirmacao] = confirmacao

        self._exibir_confirmacoes(data_confirmacao)

    def _solicitar_data_confirmacao(self):
        data_confirmacao = input("Por favor, digite a data de confirmação (no formato dd/mm/aaaa): ")
        dia, mes, ano = map(int, data_confirmacao.split("/"))
        return datetime.date(ano, mes, dia)

    def _exibir_confirmacoes(self, data_confirmacao):
        print(f"\nLista de confirmações de presença para {data_confirmacao.strftime('%d/%m/%Y')}:")
        for nome, confirmacoes_na_data in self.confirmacoes.items():
            if data_confirmacao in confirmacoes_na_data:
                confirmacao = confirmacoes_na_data[data_confirmacao]
                print(f"{nome}: {confirmacao}")

    def efetuar_pagamento(self, nome, data_confirmacao):
        pagamento = input("Deseja efetuar um pagamento via PIX? (sim/não): ")
        if pagamento.lower() == 'sim':
            valor_pix = 0.0
            descricao_pix = input("Por favor, informe ao que se refere o pagamento do PIX (ex: churrasco, mensalidade, etc.): ")
            if descricao_pix.lower() == "churrasco do dia":
                if nome in self.confirmacoes and self.confirmacoes[nome][data_confirmacao].lower() == 'sim':
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

    class PlaylistSpotify:
    
        def __init__(self, playlist_url):
            self.playlist_url = playlist_url

        def reproduzir(self):
            webbrowser.open(self.playlist_url)

            # playlist_url = "https://open.spotify.com/playlist/7bhbEcTzyIMlX9fPP5n7V5"
            # playlist = PlaylistSpotify(playlist_url)
            # playlist.reproduzir()