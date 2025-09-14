from core.validacao import validar_documento

# 1. Tudo certo
dados_ok = {
    "destinatario": "João",
    "remetente": "Maria",
    "nome": "Contrato",
    "entrada": "10/09/2025",
    "vencimento": "20/09/2025",
    "observacao": "Urgente"
}
print("Teste 1:", validar_documento(dados_ok))  
# Esperado: []

# 2. Campos vazios
dados_vazios = {
    "destinatario": "",
    "remetente": "Maria",
    "nome": "",
    "entrada": "10/09/2025",
    "vencimento": "20/09/2025",
    "observacao": ""
}
print("Teste 2:", validar_documento(dados_vazios))  
# Esperado: mensagem sobre campos obrigatórios

# 3. Data de vencimento já passou
dados_vencido = {
    "destinatario": "João",
    "remetente": "Maria",
    "nome": "Contrato",
    "entrada": "10/09/2024",
    "vencimento": "01/01/2023",
    "observacao": "Fora do prazo"
}
print("Teste 3:", validar_documento(dados_vencido))  
# Esperado: ["Data de vencimento já passou."]

# 4. Data inválida
dados_invalidos = {
    "destinatario": "João",
    "remetente": "Maria",
    "nome": "Contrato",
    "entrada": "31/02/2025",  # não existe
    "vencimento": "20/09/2025",
    "observacao": "Data inválida"
}
print("Teste 4:", validar_documento(dados_invalidos))  
# Esperado: ["Data de entrada inválida. Use o formato dd/mm/aaaa."]
