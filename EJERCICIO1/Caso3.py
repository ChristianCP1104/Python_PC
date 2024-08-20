import pandas as pd

# Cargar el archivo CSV
df = pd.read_csv('./data/airbnb.csv', sep=',')

# Filtrar las propiedades con precio menor o igual a 50€
filtered_df = df[df['price'] <= 50]

# Damos preferencia a las habitaciones compartidas (room_type == 'Shared room')
shared_room_df = filtered_df[filtered_df['room_type'] == 'Shared room']

# Ordenar por puntuación (de mayor a menor) y luego por precio (de menor a mayor)
sorted_df = shared_room_df.sort_values(by=['overall_satisfaction', 'price'], ascending=[False, True])

# Seleccionar las 10 propiedades más baratas
top_10_properties = sorted_df.head(10)

# Mostrar las 10 propiedades más baratas
print("Las 10 propiedades más baratas para Diana en Lisboa son:")
print(top_10_properties[['room_id', 'price', 'overall_satisfaction', 'neighborhood', 'room_type']])