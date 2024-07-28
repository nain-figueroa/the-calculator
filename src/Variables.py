import pandas as pd

#VENTANA##################################################################
lenght_w = 0
widht_w = 0

#IDIOMAS##################################################################
excel_idioma_esp = pd.read_excel("archives/Idiomas.xlsx", sheet_name='main', engine='openpyxl', usecols=['ID', 'ESP'])
excel_idioma_eng = pd.read_excel("archives/Idiomas.xlsx", sheet_name='main', engine='openpyxl', usecols=['ID', 'ENG'])


idioma = excel_idioma_esp