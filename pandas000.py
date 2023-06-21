#INTRODUCCION A PANDAS - Info2023 - Data Analityc
import pandas as pd
"""
ESTRUCTURAS DE Pandas: Series y Dataframes
Series: una estructura unidimensional que 
puede contener diferentes tipos de datos.
DataFrame: una estructura tabular bidimensional 
con columnas etiquetadas y filas indexadas.
"""
#CREAR Serie
 # con una lista, y la función pd.Series
data = [10, 20, 30, 40, 50]
serie = pd.Series(data)

# Mostrar la serie
print('Serie en pandas, creado a partir de una lista de Python')
print(serie)
print('')


#CREAR DataFrame
 # con un diccionario
data = {
    'Nombre': ['Juan', 'María', 'Carlos', 'Laura', 'Pedro'],
    'Edad': [28, 34, 29, 42, 36],
    'Ciudad': ['Buenos Aires', 'Madrid', 'Lima', 'Sao Paulo', 'México DF'],
    'Puntuación': [75, 82, 88, 95, 67]
}

df = pd.DataFrame(data)

# Mostrar el DataFrame completo
print('Dataframe en pandas, creado a partir de un diccionario de Python')
print(df) 
print('observamos que en el resultado cada fila esta indexada')
print('y las columnas estan nombradas (indexadas). ')
print('Los datos se muestran de forma tabular')
print('')

#LECTURA Y ESCRITURA DE DATOS
#Crea dataframe cargando datos desde un archivo CSV
df = pd.read_csv('archivo1.csv')
print('Dataframe en pandas, creado a partir de un archivo csv. ')
print(df)
print('')

#Crea un dataframe cargando datos de un archivo de excel
# Extraigo y guardo la ruta del archivo en una variable path: 
path = 'archivo.xlsx'
# Cargar datos desde un archivo Excel mediante pd.read_excel()

df = pd.read_excel(path, 
                   sheet_name='Hoja1')
print('DataFrame cargado desde el archivo Excel')
print('requiere la instalación del mopenpyxl en el entorno')
print(df)
print('')

#Cargar un dataframe desde una base de datos
#(utilizando SQLAlchemy)
# pip install sqlalchemy
# pip install psycopg2
from sqlalchemy import create_engine
import config
# Conexión a la base de datos, instalados sqalchemy y psycopg2
#importados Pandas, salchemy, psycopg2 y config al programa

"""
DESDE OTRO ARCHIVO
connection = psycopg2.connect(
    host="localhost",
    user="postgres",
    password=config.password,
    database="16mayo2023",
    port="5432"
)


"""
usuario = "postgres"
contraseña = config.password
engine = create_engine(f'postgresql://{usuario}:{contraseña}@localhost:5432/16mayo2023')

# Consulta SQL para obtener los datos
query = 'SELECT * FROM agents'
# Cargar datos desde la base de datos
df = pd.read_sql_query(query, engine)
# Mostrar el DataFrame cargado desde la base de datos
print('Dataframe cargada con una llamada desde Base de datos')
print('requiere la instalación de los modulos sqlalchemy y')
print(' psycopg2 en el entorno')
print(df)
print('')

print('El programa llego a su fin')
