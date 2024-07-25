import pandas as pd

#VENTANA##################################################################
lenght_w = 400
widht_w = 600

lenght_w_ext = lenght_w
widht_w_ext = int(widht_w/3)

ventan_ext = (lenght_w_ext, widht_w_ext)

#IDIOMAS##################################################################
excel_idioma_esp = pd.read_excel("archives/Idiomas.xlsx", sheet_name='main', engine='openpyxl', usecols=['ID', 'ESP'])
excel_idioma_eng = pd.read_excel("archives/Idiomas.xlsx", sheet_name='main', engine='openpyxl', usecols=['ID', 'ENG'])


idioma = excel_idioma_esp