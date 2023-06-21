#INTRODUCCION A PANDAS - Info2023 - Data Analityc
import pandas as pd
"""
Metodos de lectura y escritura en pandas
 Fuente de datos: base de datos
"""
#LECTURA Y ESCRITURA DE DATOS
#Crea dataframe cargando datos desde una base de datos

#LECTURA con el método de pandas .read_sql_query('SELECT * FROM tabla', engine)
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

#ESCRITURA con el método de pandas .to_csv('archivo.csv', index = False)
# Escritura a una base de datos
df.to_sql('nueva_tabla', engine, 
          if_exists='replace', index=False)

print('se creo nueva_tabla en la base de datos, a partir del df trabajado')
print(' Lo verificamos observando la base de datos en dbeaver')
print('al parecer si la tabla existe, la sobreescribe (requiero ensayar mas para confirmar)')
print('El programa llego a su fin')
