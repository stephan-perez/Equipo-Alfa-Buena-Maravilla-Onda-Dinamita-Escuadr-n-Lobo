import openpyxl as ox

datos = []

hoja = ox.load_workbook("nombre.xlsx")

hoja_data = hoja.active

n_datos = 0

for fila in range(1, hoja_data.max_row):
    _fila = []
    n_datos += 1
    for columna in hoja_data.iter_cols(0, hoja_data.max_column):
        _fila.append(columna[fila].value)
    datos.append(_fila)

print(datos)


