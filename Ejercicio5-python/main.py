# Ejercicio 5
# Enunciado: Convierte un Excel a CSV
# Objetivo:
# - Aprender a trabajar con ficheros
# - Usar la librería pandas de Python
# Hacer el CSV leyendo los valores del excel

import pandas as pd
import csv

def main():
    pass

df_file = pd.read_excel('/Users/estefaniaroblesserrano/Documents/example.xlsx', engine='openpyxl', index_col=False, parse_dates=['Date'])
df_file = df_file.drop([0], axis=1)

with open('/Users/estefaniaroblesserrano/Documents/ejemplo3.csv', 'w', encoding='UTF8', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(df_file.columns)
    writer.writerows(df_file.values)

if __name__ == '__main__':
    main()

