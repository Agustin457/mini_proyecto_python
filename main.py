# Importe de librerias

import pandas as pd
import seaborn as sns

sns.set_theme(style="darkgrid")  # instead of plt.style.use("seaborn-darkgrid")
pd.set_option("display.max_rows", None)

# Esto es para jupiter pero tambien funciona en otros entornos
"""%matplotlib inline
matplotlib.rcParams['figure.figsize'] (12,8)"""

# Leer la informaicon (data freame o df usando Pandas)

df = pd.read_csv(r"/Users/agustin/Documents/Dev/mini_proyecto_python/data/movies.csv")

# Mostrar las primeras 5 filas del data frame
"""print(df.head())"""

# Revisando si falta informacion
# Tecnica 1 con for loop

"""
for col in df.columns:
    pct_missing = np.mean(df[col].isnull())
    print('{} - {}%'.format(col, pct_missing))
"""
# Este codigo revisa si hay valores nulos en cada columna y calcula el porcentaje de valores nulos.
# No encontre valores Nulos

# Data types for our colums

"""print(df.dtypes)"""  # Revisando los tipos de datos en cada columna

# Convierte budget y gross a numero para una mejor visualisacion.
# Interpreta todos los valores no convertibles como NaN
# ( revisar si dentro no hay valores como $1,00)
"""df[['budget', 'gross']] = df[['budget', 'gross']].apply(pd.to_numeric, errors='coerce').astype('Int64')"""

# Este print lo utilizo para checker la conversion
"""print(df[['budget', 'gross']].head(20))"""

# Arreglando utilizando unicamente el release y pais como columnas separadas
if "released" in df.columns:
    df["country"] = df["released"].str.extract(r"\(([^()]*)\)\s*$")
    df["released"] = df["released"].str.replace(r"\s*\([^()]*\)\s*$", "", regex=True)

# Extraer el año de la columna 'released' para la utilizacion correcta de año
df["released_year"] = df["released"].str[-4:]
# Chequeo rápido
print(df[["released_year"]].head(40))

# Ordenando el data frame por la columna gross
df.sort_values(by=["gross"], inplace=False, ascending=False)

# Eliminar duplicados
