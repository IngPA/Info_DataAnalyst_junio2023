#INTRODUCCION A PANDAS - Info2023 - Data Analityc
import pandas as pd
"""
Metodos de lectura y escritura en pandas
 Fuente de datos: archivo excel (xlsx)
"""
#LECTURA Y ESCRITURA DE DATOS 
#Crea un dataframe cargando datos de un archivo de excel
# Extraigo y guardo la ruta del archivo en una variable path: 
path = 'archivo.xlsx'
# LECTURA datos desde un archivo Excel mediante pd.read_excel()

df = pd.read_excel(path, 
                   sheet_name='Hoja1')
print('DataFrame cargado desde el archivo Excel')
print('requiere la instalación del mopenpyxl en el entorno')
print(df)
print('')

# ESCRITURA a una fuente de datos en excel
#utilizando el método to_excel(...)
df.to_excel('nuevo_archivo.xlsx', 
            sheet_name='Hoja1', 
            index=False)
print('Se ha creado un nuevo_archivo.xlsx de excel con el dataframe generado. ')
print('si el archivo existe, lo sobreescribe (parece, hacer mas pruebas)')
print('')
print('El programa llego a su fin')

