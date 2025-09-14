from datetime import datetime
from tkinter import messagebox, ttk

#verificando datas, campos vazios. validacoes

def validar_data(data_str):
    try:
        data = datetime.strptime(data_str, "%d/%m/%Y")
        return data
    except ValueError:
        return None
    
def validar_campos_vazios(dados):
    campos_vazios = [campo for campo, valor in dados.items() if not valor.strip()]
    return campos_vazios

def validar_data_vencimento(data_str):
    try: 
        data = datetime.strptime(data_str, "%d/%m/%Y")
        if data.date() < datetime.today().date():
            return False, "Data de vencimento expirada."
        return True, ""
    except ValueError:
        return False, "Data inválida. Use o formato dd/mm/aaaa."
    
def validar_documento(dados):
    erros = []

    campos_vazios = validar_campos_vazios(dados)
    if campos_vazios:
        erros.append(f"Campos obrigatórios nao preenchidos: {', '.join(campos_vazios)}")

    ok, msg = validar_data_vencimento(dados.get("vencimento", ""))
    if not ok:
        erros.append(msg)

    entrada = dados.get("entrada", "")
    if not validar_data(entrada):
        erros.append("Data de entrada inválida. Use o formato dd/mm/aaaa.")

    return erros