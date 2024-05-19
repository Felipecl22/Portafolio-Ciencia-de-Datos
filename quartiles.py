# -*- coding: utf-8 -*-
"""quartiles.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1bAobsFwe8INlf1afJPD4Rx5jelOvO0Dp
"""

import pandas as pd
# Creamos una lista con los datos
datos = [200, 140, 200, 300, 370, 400, 600, 700, 760, 500, 300, 200]

# Creamos una lista de nombres de los meses
meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
         "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

# Creamos el DataFrame
df = pd.DataFrame({'Ventas': datos}, index=meses)

# Mostramos el DataFrame
# print(df)

df_sorted = df.sort_values(by='Ventas', ascending=True)

# Calculamos el primer cuartil (Q1)
Q1 = df_sorted['Ventas'].quantile(0.25)

# Calculamos el segundo cuartil (Q2), que es equivalente a la mediana
Q2 = df_sorted['Ventas'].quantile(0.5)

# Calculamos el tercer cuartil (Q3)
Q3 = df_sorted['Ventas'].quantile(0.75)

print("Primer cuartil (Q1):", Q1)
print("Segundo cuartil (Q2):", Q2)
print("Tercer cuartil (Q3):", Q3)