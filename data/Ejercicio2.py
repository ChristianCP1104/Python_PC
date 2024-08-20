import pandas as pd
import sqlite3

# Cargar el archivo CSV
df = pd.read_csv('./data/winemag-data-130k-v2.csv', sep=',')

# Renombrar columnas
df.rename(columns={
    'country': 'Country',
    'points': 'Rating',
    'price': 'Price',
    'winery': 'Winery'
}, inplace=True)

# Crear nuevas columnas

# 1. Agregar la columna 'Continent' basada en el país
continent_mapping = {
    'Italy': 'Europe', 'Portugal': 'Europe', 'US': 'North America', 'Spain': 'Europe',
    'France': 'Europe', 'Germany': 'Europe', 'Argentina': 'South America', 'Chile': 'South America',
    'Australia': 'Oceania', 'Austria': 'Europe', 'South Africa': 'Africa', 'New Zealand': 'Oceania',
    'Canada': 'North America', 'Hungary': 'Europe', 'Israel': 'Asia', 'Greece': 'Europe',
    'Romania': 'Europe', 'Mexico': 'North America', 'Turkey': 'Asia', 'Czech Republic': 'Europe',
    'Slovenia': 'Europe', 'Luxembourg': 'Europe', 'Croatia': 'Europe', 'Georgia': 'Asia',
    'Uruguay': 'South America', 'England': 'Europe', 'Lebanon': 'Asia', 'Serbia': 'Europe',
    'Brazil': 'South America', 'Moldova': 'Europe', 'Morocco': 'Africa', 'India': 'Asia',
    'Bulgaria': 'Europe', 'Cyprus': 'Europe', 'Armenia': 'Asia', 'Bosnia and Herzegovina': 'Europe',
    'China': 'Asia', 'Slovakia': 'Europe', 'Ukraine': 'Europe', 'Switzerland': 'Europe'
}

df['Continent'] = df['Country'].map(continent_mapping)

# 2. Categorizar vinos según la puntuación
def categorize_rating(rating):
    if rating >= 95:
        return 'Excellent'
    elif rating >= 90:
        return 'Very Good'
    elif rating >= 85:
        return 'Good'
    else:
        return 'Average'

df['Rating Category'] = df['Rating'].apply(categorize_rating)

# 3. Calcular la relación calidad-precio
df['Price to Rating Ratio'] = df['Price'] / df['Rating']

# Mostrar las primeras filas del DataFrame modificado
df.head()
print(df)

# Reporte 1: Vinos mejor puntuados por continente
df['Rating Category'].to_csv('best_rated_by_continent.csv', index=False)

# Reporte 2: Relacion calidad-precio por país
df['Price to Rating Ratio'].to_excel('price_reviews_by_country.xlsx', index=True)

# Reporte 3
# A SQLite
conn = sqlite3.connect('wine_reports.db')
df['Rating Category'].to_sql('Rating_category', conn, if_exists='replace', index=False)

# Cerrar conexión
conn.close()



