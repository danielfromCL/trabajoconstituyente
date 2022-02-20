from numpy import string_
import numpy as np
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

fnDatos = r'DatosOG.xlsx'

#Constituyente que patrocina
iNombre = 0

#Comisiones
iReglamento = 1

NombreReglamento = [iNombre, iReglamento]
PatrocinadoresDeComisionReglamento = pd.read_excel(fnDatos, usecols=NombreReglamento)
reglamentoDF = PatrocinadoresDeComisionReglamento
reglamentoDF.set_index(reglamentoDF['NOMBRE'],inplace=True)
reglamentoDF.drop('NOMBRE',axis=1,inplace=True)
reglamentoDF.columns = ['Reglamento']


def patrocinadoresDe(nombreConstituyente):
    patrocinadores = reglamentoDF[reglamentoDF.iloc[:,0]==(nombreConstituyente)]
    return list(patrocinadores.index)


patrocinados = {}
for nombre in reglamentoDF.iloc[:,0]:
    if nombre not in patrocinados and type(nombre)!=float:
        patrocinados[nombre] = patrocinadoresDe(nombre)
reglamentoDF_ = reglamentoDF.drop_duplicates(subset='Reglamento',keep='first')
reglamentoDF_.sort_values('Reglamento',inplace=True)
reglamentoDF_['Patrocinadores'] = reglamentoDF_.apply(lambda x: patrocinadoresDe(x['Reglamento']) if type(x['Reglamento']==str) else np.nan,axis = 1 )
reglamentoDF_.dropna(inplace=True)
reglamentoDF_.set_index(['Reglamento'],inplace=True)
orderedPatrocinados = reglamentoDF_.to_dict()

def cantidadpatrocinadores(orderedPatrocinados):
    for llave in orderedPatrocinados:
        print("El constituyente "+ llave +" está siendo patrocinado por "+ str(len(orderedPatrocinados[llave])) +" personas: ", end = " ")
        print(*orderedPatrocinados[llave],sep=", ")
        print("")

print(len(patrocinadoresDe("Rosa Catrileo")))