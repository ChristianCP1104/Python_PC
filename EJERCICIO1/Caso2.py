import pandas as pd

# Cargar el archivo CSV
df = pd.read_csv('./data/airbnb.csv', sep=',')

# IDs de las casas de Roberto y Clara
roberto_id = 97503
clara_id = 90387

# Filtrar las propiedades de Roberto y Clara
roberto_df = df[df['room_id'] == roberto_id]
clara_df = df[df['room_id'] == clara_id]

# Concatenar ambos DataFrames en uno solo
combined_df = pd.concat([roberto_df, clara_df], ignore_index=True)

# Guardar el DataFrame combinado en un archivo Excel
combined_df.to_excel('roberto.xlsx', index=False)

# Mostrar el DataFrame combinado (opcional)
print("DataFrame combinado con las propiedades de Roberto y Clara:")
print(combined_df[['room_id', 'host_id', 'reviews', 'neighborhood']])