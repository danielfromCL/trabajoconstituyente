
import pandas as pd
from openpyxl import load_workbook

#Constituyente que patrocina
iNombre = 0

#Comisiones
iReglamento = 1
iPresupuesto = 2
iEtica = 3
iDDHH = 4
iComunicaciones = 5
iParticipacion = 6
iDescentralizacion = 7
iParticipacionPPOO = 8
iVicepresidencias = 9

NombreReglamento = [iNombre, iReglamento]

fnDatos = r'C:\Users\Joaquin\Desktop\Constituyente\trabajoconstituyente\Datos.xlsx'
fnDatosPrueba = r'C:\Users\Joaquin\Desktop\Constituyente\trabajoconstituyente\DatosPrueba.xlsx'

PatrocinadoresDeComisionReglamento = pd.read_excel(fnDatos, usecols=NombreReglamento)

datoAEscribir = pd.DataFrame({'NOMBRE': ['Hola', 'Chao']})


writer = pd.ExcelWriter(fnDatosPrueba, engine='openpyxl')
book = load_workbook(fnDatosPrueba)
writer.book = book
writer.sheets = dict((ws.title, ws) for ws in book.worksheets)

PatrocinadoresDeComisionReglamento.to_excel(writer,sheet_name='Sheet1',startcol=0, startrow=0)
datoAEscribir.to_excel(writer, startrow=2, startcol=2)

#datoAEscribir.to_excel

writer.save()

reglamentoDF = PatrocinadoresDeComisionReglamento

arrayReglamento = reglamentoDF.to_numpy()

#print(arrayConstituyentes)

def patrocinadoresDe(nombreConstituyente):
    patrocinadores = []
    patrocinador = 0
    patrocinado = 1

    for patrocinio in arrayReglamento:
        if patrocinio[patrocinado] == nombreConstituyente:
            patrocinadores.append(patrocinio[patrocinador])
    
    return patrocinadores

print(patrocinadoresDe('Rosa Catrileo'))

a = patrocinadoresDe('Rosa Catrileo')

print("el numero total de patrocinadores a Rosa Catrileo es "+ str(len(a)))




#CREATEVIRUS(ACAAAA)





