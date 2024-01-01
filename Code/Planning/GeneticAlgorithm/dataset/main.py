import pandas as pd

# Supondo que seu arquivo CSV seja "Dataset_planning.csv"
nome_do_arquivo = "Dataset_planning.csv"

# Carregando o conjunto de dados
dados = pd.read_csv(nome_do_arquivo)

# Selecionando as colunas para criar variáveis dummy
colunas_dummy = ['State', 'Crop']

# Criando variáveis dummy
dados_dummy = pd.get_dummies(dados, columns=colunas_dummy)

# Convertendo valores booleanos para inteiros (0 e 1)
dados_dummy = dados_dummy.astype(int)

# Removendo as colunas originais 'State' e 'Crop', se existirem
dados_dummy = dados_dummy.drop(['State', 'Crop'], axis=1, errors='ignore')

# Salvando o novo conjunto de dados como "Dataset_planning.csv"
dados_dummy.to_csv("Dataset.csv", index=False)

# Exibindo as primeiras linhas do novo conjunto de dados com as variáveis dummy
print(dados_dummy.head())
