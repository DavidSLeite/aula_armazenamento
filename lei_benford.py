import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


dados_entrada_contas = pd.read_csv('./base/lei_benford_contas_partido_v2.csv')

print(dados_entrada_contas.head())

# Recebe os dados da planilha como matriz, da coluna 1 até a 1
primeiro_digito = dados_entrada_contas.iloc[:, 0].astype(str).str[0]
mtrz_contas <- as.matrix(dados_entrada_contas[,1:1])
