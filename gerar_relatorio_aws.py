import pandas as pd

# Dados simulados
dados = {
    "Serviço AWS": ["EC2 Auto Scaling", "S3 Intelligent-Tiering", "AWS Lambda"],
    "Custo Mensal Antes (USD)": [2000, 1500, 800],
    "Custo Mensal Depois (USD)": [1200, 900, 200],
}

# Criar DataFrame
df = pd.DataFrame(dados)

# Calcular economias
df["Economia Mensal (USD)"] = df["Custo Mensal Antes (USD)"] - df["Custo Mensal Depois (USD)"]
df["Economia Anual (USD)"] = df["Economia Mensal (USD)"] * 12

# Linha de totais
totais = {
    "Serviço AWS": "Total",
    "Custo Mensal Antes (USD)": df["Custo Mensal Antes (USD)"].sum(),
    "Custo Mensal Depois (USD)": df["Custo Mensal Depois (USD)"].sum(),
    "Economia Mensal (USD)": df["Economia Mensal (USD)"].sum(),
    "Economia Anual (USD)": df["Economia Anual (USD)"].sum(),
}

df = pd.concat([df, pd.DataFrame([totais])], ignore_index=True)

# Salvar como Excel
arquivo_excel = "relatorio_aws_economia.xlsx"
df.to_excel(arquivo_excel, index=False)

print(f"Arquivo Excel gerado com sucesso: {arquivo_excel}")
