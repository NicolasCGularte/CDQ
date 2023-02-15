import tkinter as tk
import datetime
import webbrowser

class GUI:
    def __init__(self, playlist_url):
        self.confirmacao_presenca = ConfirmacaoPresenca()
        self.playlist = PlaylistSpotify(playlist_url)

        # Cria a janela principal
        self.janela = tk.Tk()
        self.janela.title("Confirmação de Presença")

        # Cria o campo de texto para a data de confirmação
        tk.Label(self.janela, text="Data de confirmação (dd/mm/aaaa):").grid(row=0, column=0)
        self.data_confirmacao_entry = tk.Entry(self.janela)
        self.data_confirmacao_entry.grid(row=0, column=1)

        # Cria o campo de texto para o nome
        tk.Label(self.janela, text="Nome:").grid(row=1, column=0)
        self.nome_entry = tk.Entry(self.janela)
        self.nome_entry.grid(row=1, column=1)

        # Cria o campo de texto para a confirmação de presença
        tk.Label(self.janela, text="Confirmação de presença (sim/não):").grid(row=2, column=0)
        self.confirmacao_entry = tk.Entry(self.janela)
        self.confirmacao_entry.grid(row=2, column=1)

        # Cria o botão para adicionar uma nova confirmação de presença
        tk.Button(self.janela, text="Adicionar", command=self.adicionar_confirmacao).grid(row=3, column=0)

        # Cria o botão para efetuar o pagamento
        tk.Button(self.janela, text="Efetuar pagamento", command=self.efetuar_pagamento).grid(row=4, column=0)

        # Cria o botão para reproduzir a playlist no Spotify
        tk.Button(self.janela, text="Reproduzir playlist", command=self.reproduzir_playlist).grid(row=5, column=0)

    def adicionar_confirmacao(self):
        # Obtém a data de confirmação, nome e confirmação de presença digitados pelo usuário
        data_confirmacao = datetime.datetime.strptime(self.data_confirmacao_entry.get(), "%d/%m/%Y").date()
        nome = self.nome_entry.get()
        confirmacao = self.confirmacao_entry.get()

        # Adiciona a confirmação de presença na classe ConfirmacaoPresenca
        if nome and confirmacao:
            if confirmacao.lower() == "sim":
                self.confirmacao_presenca.confirmacoes.setdefault(nome, {})[data_confirmacao] = confirmacao
            elif confirmacao.lower() == "nao":
                self.confirmacao_presenca.confirmacoes.setdefault(nome, {})[data_confirmacao] = confirmacao
            else:
                print("Confirmação de presença inválida.")
        else:
            print("Por favor, preencha todos os campos.")

    def efetuar_pagamento(self):
        # Obtém o nome e a data de confirmação selecionados pelo usuário
        nome = self.nome_entry.get()
        data_confirmacao = datetime.datetime.strptime(self.data_confirmacao_entry.get(), "%d/%m/%Y").date()

        # Efetua o pagamento via PIX na classe ConfirmacaoPresenca
        if nome:
            self.confirmacao_presenca.efetuar_pagamento(nome, data_confirmacao)        
            print("Por favor, selecione um nome.")
        else:
            print("Por favor, preencha o campo do nome.")

    def reproduzir_playlist(self):
        # Reproduz a playlist no Spotify
        webbrowser.open(self.playlist.url)

    def iniciar(self):
        self.janela.mainloop()


if __name__ == "__main__":
# URL da playlist do Spotify
    playlist_url = "https://open.spotify.com/playlist/37i9dQZF1DWWEJlAGA9gs0"       

    # Cria a instância da classe GUI
    interface = GUI(playlist_url)

    # Inicia a interface gráfica
    interface.iniciar()