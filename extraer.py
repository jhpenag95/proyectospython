import csv
import re

# Solicita la ubicación del archivo de índice
index_file = input("Ingrese la ubicación del archivo index: ")

# Abre el archivo de índice para leer
with open(index_file, 'r') as file:
    # Crea el objeto del lector CSV
    reader = csv.reader(file, delimiter='=')
    
    # Crea el objeto del escritor CSV
    with open('datos.csv', 'w', newline='') as outfile:
        writer = csv.writer(outfile, delimiter=',')
        
        # Escribe la cabecera del archivo CSV
        writer.writerow(['IDENTIFICACION O NOMBRE DE LA CARPETA', 'SERIE', 'CODIGO DE LA SERIE', 'NUMERO DE CAJA', 'OBSERVACIONES'])
        
        # Itera a través de las filas del archivo de índice
        skip_first_row = True # Variable para omitir la primera fila
        for row in reader:
            # Omitir la primera fila
            if skip_first_row:
                skip_first_row = False
                continue
            
            # Si la fila tiene un signo igual, entonces contiene datos
            if len(row) > 0 and '=' in row[0]:
                # Divide la fila en dos partes por el signo igual
                data = row[0].split('=')
                # Busca coincidencias con una expresión regular para extraer el texto entre comillas dobles
                quoted_text = re.findall(r'"([^"]*)"', data[1])
                # Si se encontró texto entre comillas dobles, entonces reemplaza la segunda parte de la fila con el texto encontrado
                if quoted_text:
                    data[1] = quoted_text[0]
                # Escribe los datos en el archivo CSV
                writer.writerow(data[1:])
