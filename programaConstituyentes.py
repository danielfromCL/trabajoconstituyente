
from numpy import NAN, NaN, nan, string_
import numpy
import pandas as pd
from openpyxl import load_workbook
import math
import sys
import os.path


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))





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


fnDatos = r'Datos.xlsx'

fnDatosPrueba = r'DatosPrueba.xlsx'

PatrocinadoresDeComisionReglamento = pd.read_excel(fnDatos, usecols=NombreReglamento)


#writer = pd.ExcelWriter(fnDatosPrueba, engine='openpyxl')
#book = load_workbook(fnDatosPrueba)
#writer.book = book
#writer.sheets = dict((ws.title, ws) for ws in book.worksheets)


#PatrocinadoresDeComisionReglamento.to_excel(fnDatosPrueba)

#datoAEscribir.to_excel


reglamentoDF = PatrocinadoresDeComisionReglamento

arrayReglamento = reglamentoDF.to_numpy()

#arrayReglamento[1][1] = 'hola'

#newDataFrame = pd.DataFrame(arrayReglamento, index = reglamentoDF.index, columns=reglamentoDF.columns)

#newDataFrame.to_excel(fnDatosPrueba,sheet_name='Sheet1',startcol=0, startrow=0)

#print(arrayConstituyentes)

def patrocinadoresDe(nombreConstituyente):
    patrocinadores = []
    patrocinador = 0
    patrocinado = 1

    for patrocinio in arrayReglamento:
        if patrocinio[patrocinado] == nombreConstituyente:
            patrocinadores.append(patrocinio[patrocinador])
    
    return patrocinadores


        


def aQuienPatrocina(nombreConstituyente):
    patrocinador = 0
    patrocinado = 1
    viejoDF = pd.read_excel(fnDatosPrueba, usecols=[1,2])
    arrayReglamento = viejoDF.to_numpy()

    for patrocinio in arrayReglamento:
        if patrocinio[patrocinador] == nombreConstituyente:
            return patrocinio[patrocinado]

def nombreValidoPatrocinador(nombreConstituyente):
    patrocinador = 0
    viejoDF = pd.read_excel(fnDatosPrueba, usecols=[1,2])
    arrayReglamento = viejoDF.to_numpy()

    var = False

    for patrocinio in arrayReglamento:
        if patrocinio[patrocinador] == nombreConstituyente:
            var = True
    return var

def nombreValidoPatrocinado(nombreConstituyente):
    patrocinado = 1
    viejoDF = pd.read_excel(fnDatosPrueba, usecols=[1,2])
    arrayReglamento = viejoDF.to_numpy()

    var = False

    for patrocinio in arrayReglamento:
        if patrocinio[patrocinado] == nombreConstituyente:
            var = True
    return var



def yaPatrocino(nombreConstituyente):

    if type(aQuienPatrocina(nombreConstituyente))==str:
        return True
    else:
        return False

def IngresarPatrocinio(ConstituyentePatrocinador, ConstituyentePatrocinado):

    if yaPatrocino(ConstituyentePatrocinador):
        print("Este constituyente ya patrocino a alguien")
    
    elif nombreValidoPatrocinador(ConstituyentePatrocinador) == False:
        print("Este patrocinador no existe")

    elif nombreValidoPatrocinador(ConstituyentePatrocinado) == False:
        print("Este patrocinado no existe")

    else:
        viejoDF = pd.read_excel(fnDatosPrueba, usecols=[1,2])
        viejoArr = viejoDF.to_numpy()
        patrocinador = 0
        patrocinado = 1

        for patrocinio in viejoArr:
            if patrocinio[patrocinador] == ConstituyentePatrocinador:
                patrocinio[patrocinado] = ConstituyentePatrocinado

        newDataFrame = pd.DataFrame(viejoArr, index = viejoDF.index, columns=viejoDF.columns)

        newDataFrame.to_excel(fnDatosPrueba,sheet_name='Sheet1',startcol=0, startrow=0)

        print("El patrocinio ha sido ingresado con éxito!")

while(True):

    patrocinadorUsuario = input("Ingrese nombre constituyente patrocinador: ")

    patrocinadoUsuario = input("Ingrese nombre constituyente patrocinado: ")

    IngresarPatrocinio(patrocinadorUsuario, patrocinadoUsuario)




        









