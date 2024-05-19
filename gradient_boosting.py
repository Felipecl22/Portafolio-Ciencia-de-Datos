# -*- coding: utf-8 -*-
"""Gradient Boosting.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1raTHGkoBAYdmgKUYAPH7lHQqxkPqx0oR

# **Gradient Boosting**
"""

from google.colab import drive
drive.mount('/content/drive')
# Montando el drive para acceder a los archivos, ya que tengo los csv en mi Drive, esto no es necesario si ustedes tienen el archivo en su escritorio.

import pandas as pd

# Ruta del archivo CSV en Google Drive.
potencial_csv = '/content/drive/My Drive/Colab Notebooks/Módulo 5/potencial.xlsx'

# Importando la data y transformandola a objeto Dataframe.
# En este poner el path correspondiente del archivo como parametro de pd.read_csv.
df_potencial = pd.read_excel(potencial_csv)

# Imprimir la información del DataFrame consolidado
print(df_potencial)

"""Me parece que utilizar las columnas Income, CCavg y Mortgage para predecir si un cliente tomará un Personal loan.

"CCAvg" representa el gasto promedio en tarjeta de crédito.

"Mortgage" representa el saldo pendiente del préstamo hipotecario en el conjunto de datos dado.
"""

# Verificar por variables categóricas

categoricas = []

for var in df_potencial:
    if df_potencial[var].dtype == 'O':
        categoricas.append(var)

print(f'Hay {len(categoricas)} variables categóricas en la dataframe')
print(f'Estas son: {categoricas}')

# Verificar por variables categóricas

numericas = []

for var in df_potencial:
    if df_potencial[var].dtype != 'O':
        numericas.append(var)

print(f'Hay {len(numericas)} variables categóricas en la dataframe')
print(f'Estas son: {numericas}')

# Verificamos por valores únicos
df_potencial['Personal Loan'].unique()

"""Con lo anterior, estamos listos para crear un Gradient Boosting regresivo."""

# Creando variables predictorias y variable objetivo.
X = df_potencial[['Income', 'CCAvg', 'Mortgage']]
y = df_potencial['Personal Loan']

X.isnull().sum()

y.isnull().sum()

"""Normalizar datos"""

from sklearn.preprocessing import StandardScaler

# Guarda los nombres de las columnas antes de la transformación
original_columns = X.columns.tolist()

# Inicializa y ajusta el scaler a tus datos
scaler = StandardScaler()
scaler.fit(X)

# Transforma tus datos utilizando el scaler ajustado
X_scaled = scaler.transform(X)

# Convierte la matriz transformada en un DataFrame de pandas manteniendo los nombres de las columnas originales
X_df = pd.DataFrame(X_scaled, columns=original_columns)

X_df

y.unique()

from sklearn.model_selection import train_test_split
# División de los datos en conjunto de entrenamiento y prueba en una proporción de 5:1
X_train, X_test, y_train, y_test = train_test_split(X_df, y, test_size=0.2, random_state=42)

from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import mean_squared_error

# Inicializar el modelo de Gradient Boosting para regresión
gb_regressor = GradientBoostingRegressor()

# Entrenar el modelo utilizando el conjunto de entrenamiento
gb_regressor.fit(X_train, y_train)

# Realizar predicciones en el conjunto de prueba
predictions = gb_regressor.predict(X_test)

# Calcular el error cuadrático medio (MSE) en el conjunto de prueba
mse = mean_squared_error(y_test, predictions)
print("Mean Squared Error:", mse)

# Realizar validación cruzada para obtener una evaluación más robusta del modelo
cv_scores = cross_val_score(gb_regressor, X, y, cv=5, scoring='neg_mean_squared_error')
cv_mse = -cv_scores.mean()  # Negamos el MSE para obtener el valor real
print("Cross-Validated Mean Squared Error:", cv_mse)

# También puedes evaluar otras métricas de rendimiento según tus necesidades

# Si deseas obtener una interpretación del modelo, puedes examinar la importancia de las características
feature_importances = gb_regressor.feature_importances_
print("Feature Importances:", feature_importances)

"""El error cuadrático medio (MSE) obtenido en el conjunto de prueba es aproximadamente 0.0514. Esto indica que, en promedio, las predicciones del modelo están a una distancia de 0.0514 unidades al cuadrado de las etiquetas reales del conjunto de prueba. En general, cuanto más bajo sea el valor del MSE, mejor será el rendimiento del modelo.

Las importancias de las características. Estas son las ponderaciones que el modelo asigna a cada característica para hacer predicciones. En este caso, se tienen tres características y las importancias son aproximadamente 0.6474, 0.2886 y 0.0640 para la primera, segunda y tercera característica respectivamente.

Estas importancias indican qué características son más influyentes en las predicciones del modelo. Una importancia más alta significa que la característica tiene un mayor impacto en las predicciones del modelo. Esto puede ser útil para comprender qué características son más relevantes para el problema en cuestión y para realizar selección de características si es necesario.

El "Cross-Validated Mean Squared Error" (Error Cuadrático Medio Validado Cruzadamente) es una medida del rendimiento del modelo de regresión después de aplicar la validación cruzada. Es el promedio del error cuadrático medio (MSE) obtenido en todas las particiones del conjunto de datos durante la validación cruzada.

En términos simples, representa cuán cerca están las predicciones del modelo de los valores reales en promedio, después de tener en cuenta la variabilidad en los datos que puede surgir de diferentes divisiones del conjunto de datos en conjuntos de entrenamiento y prueba.

En tu caso, un "Cross-Validated Mean Squared Error" de 0.052 indica que, en promedio, el modelo predice el cuadrado de la diferencia entre las predicciones y los valores reales de la variable objetivo (en este caso, probablemente el préstamo personal). Un valor de MSE más bajo indica un mejor rendimiento del modelo, ya que implica que las predicciones están más cerca de los valores reales. Por lo tanto, un MSE de 0.052 es bastante bajo y sugiere que el modelo tiene un buen rendimiento en la predicción de la variable objetivo.
"""

# Suponiendo que 'X_test' es tu conjunto de características de prueba

# Realiza predicciones en el conjunto de prueba
predictions = gb_regressor.predict(X_test)

# Muestra las predicciones
print("Predicciones:", predictions)

"""La predicción para la primera fila es aproximadamente 0.0008. Esto significa que el modelo estima que hay una probabilidad muy baja, alrededor del 0.08%, de que el cliente correspondiente en la primera fila acepte un préstamo personal."""

# Crear un nuevo cliente con características específicas en un DataFrame
nuevo_cliente = pd.DataFrame({'Income': [-0.7], 'CCAvg': [0.2], 'Mortgage': [-0.3]})

# Realizar la predicción utilizando el modelo entrenado
prediccion = gb_regressor.predict(nuevo_cliente)

# Imprimir la predicción
print("Personal Loan Probability:", prediccion)