import datetime
import webbrowser
import tkinter as tk
from tkinter import messagebox

class ConfirmacaoPresencaGUI:

    def __init__(self, master):
        self.master = master
        master.title("Confirmação de Presença")

        self.confirmacoes = {}

        # Label e Entry para a data de confirmação
        self.data_confirmacao_label = tk.Label(master, text="Data de confirmação (dd/mm/aaaa):")
        self.data_confirmacao_label.grid(row=0, column=0, padx=10, pady=10)
        self.data_confirmacao_entry = tk.Entry(master)
        self.data_confirmacao_entry.grid(row=0, column=1, padx=10, pady=10)

        # Botão para coletar as confirmações
        self.coletar_button = tk.Button(master, text="Coletar Confirmações", command=self.coletar_confirmacoes)
        self.coletar_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        # Label para exibir as confirmações
        self.confirmacoes_label = tk.Label(master, text="")
        self.confirmacoes_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        # Botão para efetuar o pagamento
        self.efetuar_pagamento_button = tk.Button(master, text="Efetuar Pagamento", command=self.efetuar_pagamento)
        self.efetuar_pagamento_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        # Botão para reproduzir a playlist do Spotify
        self.playlist_button = tk.Button(master, text="Reproduzir Playlist do Spotify", command=self.reproduzir_playlist)
        self.playlist_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    def coletar_confirmacoes(self):
        data_confirmacao_str = self.data_confirmacao_entry.get()
        if not data_confirmacao_str:
            tk.messagebox.showerror("Erro", "Por favor, informe a data de confirmação.")
            return

        try:
            dia, mes, ano = map(int, data_confirmacao_str.split("/"))
            data_confirmacao = datetime.date(ano, mes, dia)
        except:
            tk.messagebox.showerror("Erro", "Data de confirmação inválida. Por favor, informe no formato dd/mm/aaaa.")
            return

        self.confirmacoes = {}

        # Janela para coletar as confirmações
        self.coletar_window = tk.Toplevel(self.master)
        self.coletar_window.title("Coletar Confirmações")

        self.nome_label = tk.Label(self.coletar_window, text="Nome:")
        self.nome_label.grid(row=0, column=0, padx=10, pady=10)
        self.nome_entry = tk.Entry(self.coletar_window)
        self.nome_entry.grid(row=0, column=1, padx=10, pady=10)

        self.confirmacao_label = tk.Label(self.coletar_window, text="Confirmação:")
        self.confirmacao_label.grid(row=1, column=0, padx=10, pady=10)
        self.confirmacao_var = tk.StringVar()
        self.confirmacao_var.set("Não")
        self.confirmacao_sim_radio = tk.Radiobutton(self.coletar_window, text="Sim", variable=self.confirmacao_var, value="Sim")
        self.confirmacao_sim_radio.grid(row=1, column=1, padx=10, pady=10)
        self.confirmacao_nao_radio = tk.Radiobutton(self.coletar_window, text="Não", variable=self.confirmacao_var, value="Não")
        self.confirmacao_nao_radio.grid(row=1, column=2, padx=10, pady=10)
        self.adicionar_button = tk.Button(self.coletar_window, text="Adicionar", command=self.adicionar_confirmacao)
        self.adicionar_button.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

        self.confirmacoes_label = tk.Label(self.coletar_window, text="")
        self.confirmacoes_label.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

    def adicionar_confirmacao(self):
        nome = self.nome_entry.get()
        confirmacao = self.confirmacao_var.get()

        if nome and confirmacao:
            self.confirmacoes[nome] = confirmacao
            self.confirmacoes_label.config(text=str(self.confirmacoes))
            self.nome_entry.delete(0, tk.END)
            self.confirmacao_var.set("Não")

    def efetuar_pagamento(self):
        # Implementação para efetuar o pagamento
        messagebox.showinfo("Pagamento", "Pagamento efetuado com sucesso!")

    def reproduzir_playlist(self):
        # URL da playlist do Spotify
        playlist_url = "https://open.spotify.com/playlist/37i9dQZF1DX6uhsAfngva3"

        # Abrir a URL no navegador padrão do usuário
        webbrowser.open_new_tab(playlist_url)     



root = tk.Tk()
app = ConfirmacaoPresencaGUI(root)
root.mainloop()                                       