from datetime import datetime
from tkinter import messagebox, ttk

#verificando datas, campos vazios. validacoes

def validar_data(data_str):
    try:
        data = datetime.strptime(data_str, "%d/%m/%Y")
        return data
    except ValueError:
        return None