import csv

# Dados de exemplo (substitua pelos seus próprios dados)
dados = [
    ["Nome", "Idade", "Cidade"],
    ["Pedro", 30, "Sao Paulo"],
    ["Maria", 25, "Rio de Janeiro"],
    # Adicione mais dados aqui...
]

# Nome do arquivo CSV de saída
nome_arquivo_csv = "mushrooms_database.csv"

# Escreva os dados no arquivo CSV
with open(nome_arquivo_csv, mode="w", newline="") as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv)
    for linha in dados:
        escritor_csv.writerow(linha)
