#interface grafica do projeto
import tkinter as tk
from tkinter import ttk, messagebox
import csv
from datetime import datetime
import os
from core.validacao import validar_data


class AppInterface(): #inicializar e definir a estilizacao da janela principal
    def __init__(self, master):
        self.master = master
        self.master.title("Gerenciador de Documentos")
        self.master.geometry("600x400")

        self.estilo = ttk.Style()
        self.estilo.theme_use("clam")
        self.estilo.configure("Treeview", font=("Arial", 12), rowheight=25)
        self.estilo.configure("Treeview.Heading", font=("Arial", 14, "bold"))

        #Frame é parecido com container, section, div.
        self.frame = ttk.Frame(self.master, padding=20)
        self.frame.pack(fill="both", expand=True)

        #botoes da janela principal
        self.btn_cadastrar = ttk.Button(self.frame, text="Cadastrar Documento", command=self.abrir_cadastro)
        self.btn_cadastrar.pack(pady=5)

        self.btn_buscar = ttk.Button(self.frame, text="Buscar Documento", command=self.abrir_busca)
        self.btn_buscar.pack(pady=5)
        
        self.btn_editar = ttk.Button(self.frame, text="Editar Documento", command=self.editar_cadastro)
        self.btn_editar.pack(pady=5)


    def abrir_cadastro(self): #criando uma nova 'sub-janela'
        janela = tk.Toplevel(self.master)
        janela.title("Cadastrar Novo Documento")
        janela.geometry("500x400")

        frame_cadastro = ttk.Frame(janela, padding=20)
        frame_cadastro.pack(fill="both", expand=True)

        #Destinatário
        ttk.Label(frame_cadastro, text="Destinatário:").pack(anchor="w")
        entry_destinatario = ttk.Entry(frame_cadastro)
        entry_destinatario.pack(fill="x", pady=5)

        #Remetente
        ttk.Label(frame_cadastro, text="Remetente:").pack(anchor="w")
        entry_remetente = ttk.Entry(frame_cadastro)
        entry_remetente.pack(fill="x", pady=5)

        #Nome do Documento
        ttk.Label(frame_cadastro, text="Nome do Documento:").pack(anchor="w")
        entry_nome = ttk.Entry(frame_cadastro)
        entry_nome.pack(fill="x", pady=5)

        #Data de Entrada
        ttk.Label(frame_cadastro, text="Data de Entrada (dd/mm/aaaa):").pack(anchor="w")
        entry_entrada = ttk.Entry(frame_cadastro)
        entry_entrada.pack(fill="x", pady=5)

        #Data de Vencimento
        ttk.Label(frame_cadastro, text="Data de Vencimento (dd/mm/aaaa):").pack(anchor="w")
        entry_vencimento = ttk.Entry(frame_cadastro)
        entry_vencimento.pack(fill="x", pady=5)

        #Obs
        ttk.Label(frame_cadastro, text="OBS:").pack(anchor="w")
        entry_obs = ttk.Entry(frame_cadastro)
        entry_obs.pack(fill="x", pady=5)

        def salvar():

                destinatario = entry_destinatario.get().strip()
                remetente = entry_remetente.get().strip()
                tipo = entry_nome.get().strip()
                data_entrada = entry_entrada.get().strip()
                data_validade = entry_vencimento.get().strip()
                observacao = entry_obs.get().strip()

                #validacoes 
                if not destinatario or not remetente or not tipo or not data_entrada or not data_validade:
                    messagebox.showerror("Erro", "Prencha todos os campos obrigatórios.")
                    return
                
                data_entrada = entry_entrada.get().strip()
                data_validade = entry_vencimento.get().strip()

                entrada_valida = validar_data(data_entrada)
                validade_valida = validar_data(data_validade)

                if not entrada_valida:
                    messagebox.showerror("Erro", "Data de entrada inválida. Use o formato dd/mm/aaaa.")

                if not validade_valida:
                    messagebox.showerror("Erro", "Data de vencimento inválida. Use o formato dd/mm/aaaa.")

        self.btn_salvar = ttk.Button(frame_cadastro, text="Salvar", command=salvar)
        self.btn_salvar.pack(pady=10)

    def abrir_busca(self):
        print("Abrir Busca")

    def editar_cadastro(self):
        print("Editar Cadastro")