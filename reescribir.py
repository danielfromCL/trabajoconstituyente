from numpy import string_
import numpy
import pandas as pd
from openpyxl import load_workbook
import math
import sys
import os.path


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import PySimpleGUI as sg

import PySimpleGUI as psg


from numpy import string_
import pandas as pd
from openpyxl import load_workbook
import sys
import os.path
from collections import OrderedDict

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import PySimpleGUI as sg

fnDatos = r'Datos.xlsx'

#Constituyente que patrocina
iNombre = 0

#Comisiones
iReglamento = 1

NombreReglamento = [iNombre, iReglamento]
PatrocinadoresDeComisionReglamento = pd.read_excel(fnDatos, usecols=NombreReglamento)
reglamentoDF = PatrocinadoresDeComisionReglamento
reglamentoDF.set_index(reglamentoDF['NOMBRE'],inplace=True)
reglamentoDF.drop('NOMBRE',axis=1,inplace=True)


def patrocinadoresDe(nombreConstituyente):
    patrocinadores = reglamentoDF[reglamentoDF.iloc[:,0]==(nombreConstituyente)]
    return list(patrocinadores.index)


patrocinados = {}
for nombre in reglamentoDF.iloc[:,0]:
    if nombre not in patrocinados and type(nombre)!=float:
        patrocinados[nombre] = patrocinadoresDe(nombre)



orderedPatrocinados = OrderedDict(sorted(patrocinados.items(), key=lambda x: len(x[1]),reverse= True))

def cantidadpatrocinadores(orderedPatrocinados):
    for llave in orderedPatrocinados:
        print("El constituyente "+ llave +" está siendo patrocinado por "+ str(len(orderedPatrocinados[llave])) +" personas: ", end = " ")
        print(*orderedPatrocinados[llave],sep=", ")
        print("")

print(len(patrocinadoresDe("Rosa Catrileo")))