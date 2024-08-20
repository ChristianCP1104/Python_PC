import pandas as pd

# Cargar el archivo CSV
df = pd.read_csv('./data/airbnb.csv', sep=',')

# Filtrar apartamentos con más de 10 críticas y puntuación mayor a 4
filtered_df = df[(df['reviews'] > 10) & (df['overall_satisfaction'] > 4)]

# Ordenar por puntuación de mayor a menor yoverall_satisfaction, en caso de empate, por número de críticas de mayor a menor
sorted_df = filtered_df.sort_values(by=['overall_satisfaction', 'reviews'], ascending=[False, False])

# Seleccionar las 3 mejores alternativas
top_3_alternatives = sorted_df.head(3)

# Mostrar las 3 mejores alternativas
print("Las 3 mejores alternativas para Alicia son:")
print(top_3_alternatives[['room_id', 'overall_satisfaction', 'reviews', 'neighborhood']])