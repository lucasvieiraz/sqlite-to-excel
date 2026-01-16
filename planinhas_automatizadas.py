import sqlite3
import pandas as pd

con = sqlite3.connect("controle_2026.db")

#Primeira planinha

df = pd.read_sql("""
SELECT PLACA, SETOR, DATA, VALOR FROM controle WHERE DATA = '09/01/2026'
""", con)

df.to_excel("relatorioAbastecimento09.xlsx", index=False)


#Segundo planinha

df = pd.read_sql("""
SELECT PLACA, SETOR FROM controle
""", con)

df.to_excel("veiculos_abastecidos.xlsx")