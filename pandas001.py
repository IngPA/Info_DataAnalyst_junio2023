#INTRODUCCION A PANDAS - Info2023 - Data Analityc
import pandas as pd
"""
Metodos de lectura y escritura en pandas
 Fuente de datos: archivo csv
"""
#LECTURA Y ESCRITURA DE DATOS
#Crea dataframe cargando datos desde un archivo CSV
#LECTURA con el método de pandas .read_csv('archivo.csv')
df = pd.read_csv('archivo1.csv')
print('Dataframe en pandas, creado a partir de un archivo csv. ')
print(df)
print('')

#ESCRITURA a un archivo CSV
# con el método de pandas .to_csv('archivo.csv', index = False)

df.to_csv('nuevo_archivo.csv', index=False)
print('se ha escrito \'nuevo_archivo.csv\' con el dataframe generado')
print('')

print('El programa llego a su fin')
