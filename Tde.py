# =========================================
# Questão 1 — Importação das bibliotecas
# =========================================
import pandas as pd
import numpy as np


# =========================================
# Questão 2 — Leitura dos dados
# =========================================
df = pd.read_csv('vendas_brasil_aula4_kpis.csv')

df.head()


# =========================================
# Questão 4 — Exploração inicial
# =========================================
df.shape
df.dtypes
df.info()


# =========================================
# Questão 5 — KPIs Globais
# =========================================
receita_total = df['receita'].sum()
lucro_total = df['lucro'].sum()
ticket_medio = df['receita'].mean()
margem = (lucro_total / receita_total) * 100

receita_total, lucro_total, ticket_medio, margem


# =========================================
# Questão 7 — Métricas derivadas
# =========================================
df['margem_percentual'] = (df['lucro'] / df['receita']) * 100
df['ticket_medio_pedido'] = df['receita'] / df['quantidade']


# =========================================
# Questão 8 — Análise por canal
# =========================================
canal = df.groupby('canal_venda').agg({
    'receita': 'sum',
    'lucro': 'sum',
    'pedido_id': 'count'
}).rename(columns={'pedido_id': 'qtd_pedidos'})

canal['ticket_medio'] = canal['receita'] / canal['qtd_pedidos']
canal['margem'] = (canal['lucro'] / canal['receita']) * 100

canal.sort_values(by='receita', ascending=False)


# =========================================
# Questão 10 — Análise por categoria
# =========================================
categoria = df.groupby('categoria').agg({
    'receita': 'sum',
    'lucro': 'sum',
    'pedido_id': 'count'
}).rename(columns={'pedido_id': 'qtd_pedidos'})

categoria['margem'] = (categoria['lucro'] / categoria['receita']) * 100

categoria.sort_values(by='lucro', ascending=False)


# =========================================
# Questão 12 — Análise por UF
# =========================================
uf = df.groupby('uf').agg({
    'receita': 'sum',
    'lucro': 'sum'
})

uf['participacao_%'] = (uf['receita'] / receita_total) * 100

uf.sort_values(by='receita', ascending=False)


# =========================================
# Questão 14 — Top produtos
# =========================================
top_lucro = df.groupby('produto')['lucro'].sum().sort_values(ascending=False).head(10)
top_receita = df.groupby('produto')['receita'].sum().sort_values(ascending=False).head(10)
piores = df.groupby('produto')['lucro'].sum().sort_values().head(5)

top_lucro
top_receita
piores


# =========================================
# Questão 16 — Análise temporal
# =========================================
df['data_venda'] = pd.to_datetime(df['data_venda'])

df['ano'] = df['data_venda'].dt.year
df['mes'] = df['data_venda'].dt.month

tempo = df.groupby(['ano', 'mes']).agg({
    'receita': 'sum',
    'lucro': 'sum'
}).reset_index()

tempo.sort_values(['ano', 'mes'])