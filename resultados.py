from numpy import string_
import pandas as pd
from openpyxl import load_workbook
import sys
import os.path
from collections import OrderedDict

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import PySimpleGUI as sg

fnDatos = r'Datos.xlsx'

#fnDatos = r'DatosPrueba.xlsx'

#Constituyente que patrocina
iNombre = 1

#Comisiones
iReglamento = 2

NombreReglamento = [iNombre, iReglamento]
PatrocinadoresDeComisionReglamento = pd.read_excel(fnDatos, usecols=NombreReglamento)
reglamentoDF = PatrocinadoresDeComisionReglamento
reglamentoDF.set_index(reglamentoDF['NOMBRE'],inplace=True)
reglamentoDF.drop('NOMBRE',axis=1,inplace=True)


def patrocinadoresDe(nombreConstituyente, arr):
    
    patrocinadores = []
    patrocinador = 0
    patrocinado = 1

    for patrocinio in arr:
        if patrocinio[patrocinado] == nombreConstituyente:
            patrocinadores.append(patrocinio[patrocinador])
    
    return patrocinadores

def patrocinios(nombre,arr):

    a = patrocinadoresDe(nombre,arr)

    respuesta = "El/la constituyente "+ nombre +" está siendo patrocinado por "+ str(len(a)) +" personas: "
    b =0
    for llave in a:
        if b %9 == 0:
            respuesta += '\n ' + llave + ', '
            b+=1
        elif b == len(a)-1:
            respuesta += llave
        else:
            respuesta += llave + ', '
            b+=1

    return respuesta





def hacetodo():
    viejoDF = pd.read_excel(fnDatos, usecols=[1,2])
    arr = viejoDF.to_numpy()
    patrocinados = {}
    for nombre in viejoDF.iloc[:,1]:
        if nombre not in patrocinados and type(nombre)!=float:
         patrocinados[nombre] = patrocinadoresDe(nombre, arr)
    orderedPatrocinados = OrderedDict(sorted(patrocinados.items(), key=lambda x: len(x[1]),reverse= True))
    return orderedPatrocinados

def cantidadpatrocinadores(orderedPatrocinados):
    lista =[]
    for llave in orderedPatrocinados:
        respuesta = "El/la constituyente "+ llave +" está siendo patrocinado por "+ str(len(orderedPatrocinados[llave])) +" personas: "
        b =0
        for llaveB in orderedPatrocinados[llave]:
            if b %9 == 0:
                respuesta += '\n ' + llaveB + ', '
                b+=1
            elif b == len(orderedPatrocinados[llave])-1:
                respuesta += llaveB
            else:
                respuesta += llaveB + ', '
                b+=1

        #if len(orderedPatrocinados[llave]) <9:
          #  lista.append("El/la constituyente "+ llave +" está siendo patrocinado por "+ str(len(orderedPatrocinados[llave])) +" personas: \n" + str(orderedPatrocinados[llave]))
        #else:
         #   result ="El/la constituyente "+ llave +" está siendo patrocinado por "+ str(len(orderedPatrocinados[llave])) +" personas: \n" + str(orderedPatrocinados[llave][:9])
          #  result+= "  \n" + str(orderedPatrocinados[llave][9:])
        lista.append(respuesta)
        #print(llave)
        #print("El constituyente "+ llave +" está siendo patrocinado por "+ str(len(orderedPatrocinados[llave])) +" personas: ")
        #print(*orderedPatrocinados[llave],sep=", ")
        #print("")
    return lista

#cantidadpatrocinadores(orderedPatrocinados)

#print(orderedPatrocinados)

def todospatrocinadores(orderedPatrocinados):
    for llave in orderedPatrocinados:
        #print(orderedPatrocinados[llave][0])
        print("El/la constituyente "+ orderedPatrocinados[llave][0] +" está siendo patrocinado por "+ str(len(orderedPatrocinados[llave])) +" personas: ", end = " ")
        #print(*orderedPatrocinados[llave],sep=", ")
        #print("")

#todospatrocinadores(orderedPatrocinados)

choices = ["Tiare Aguilera", "Victorino Antilef", "Wilfredo Bacián","Alexis Caiguan","Rosa Catrileo","Eric Chinga","Felix Galleguillos","Isabel Godoy","Lidia González","Luis Jiménez",
            "Francisca Linconao","Natividad Llanquileo","Elisa Loncón","Isabella Mamami","Adolfo Millabur","Fernando Tirado","Margarita Vargas"]





#cantidadpatrocinadores(orderedPatrocinados)


def main():
    # The list of choices that are going to be searched
    # In this example, the PySimpleGUI Element names are used
    patrocinador = 0
    patrocinado = 1
    viejoDF = pd.read_excel(fnDatos, usecols=[1,2])
    choicesConstituyentes = []
    arrayReglamento = viejoDF.to_numpy()

    output = None

    nro_escanos_reservados = 5
    nro_no_reservados = 6

    
    escanos_reservados = ["Tiare Aguilera", "Victorino Antilef", "Wilfredo Bacián","Alexis Caiguan","Rosa Catrileo","Eric Chinga","Felix Galleguillos","Isabel Godoy","Lidia González","Luis Jiménez",
            "Francisca Linconao","Natividad Llanquileo","Elisa Loncón","Isabella Mamami","Adolfo Millabur","Fernando Tirado","Margarita Vargas"]


    for patrocinio in arrayReglamento:
        choicesConstituyentes.append(str(patrocinio[patrocinador]))
   
    #choices = ["Tom", "Cebolla", "Poto", "Cholo", "Tomate", "Tetera"] # ACA TIENE QUE IR UNA LISTA CON LOS CONSTITUYENTES
    choices = choicesConstituyentes

    input_width = 75                #El ancho de la caja del input
    num_items_to_show = 6            #Cantidad de valores en el dropdown [predictions]

    output = None
    layout = [
        [sg.Text('Estos son los patrocinios ingresados en la comisión 1: La de reglamento', size=(100, 2))],


        [sg.Text('Seleccione Constituyente Patrocinad@ para revisar sus Patrocinadores:')],
        [sg.Input(size=(input_width, 1), enable_events=True, key='-IN-')],
        [sg.pin(sg.Col([[sg.Listbox(values=[], size=(input_width, num_items_to_show), enable_events=True, key='-BOX-',
                                    select_mode=sg.LISTBOX_SELECT_MODE_SINGLE, no_scrollbar=True)]],
                       key='-BOX-CONTAINER-', pad=(0, 0), visible=False     #La caja donde se muestra dropdown es el BOX CONTAINER
                       )
                       )],

        [sg.Button("Revisar", key = "-SEND-" )],
        
        [sg.Button("Revisar todos los patrocinios de esta comisión", key = "-Todos-" )],

        [sg.pin(sg.Col([[sg.Text('Hola', key = "-output-", justification='left', size=(input_width, 50))]],
                        key='-BOX-CONTAINER-3-', pad=(0, 0), visible=False, scrollable=True)
                       )],        
        ]
        


    orderedPatrocinados = hacetodo()
    largo = cantidadpatrocinadores(orderedPatrocinados)
    re=[]
    '''
    for i in range(len(largo)):
        k1 = "-output-" + str(i) 
        k2 = "-BOX-CONTAINER-3-"  + str(i)
        re += [[sg.pin(sg.Col([[sg.Text('Hola', key = k1, justification='left')]],
                        key=k2, pad=(0, 0), visible=False, scrollable=True)
                       )],]
    layout+=re    
    ''' 
    window = sg.Window('Preoceso de selección de comisiones', layout, return_keyboard_events=True, finalize=True, font= ('Helvetica', 16))

    

    list_element:sg.Listbox = window.Element('-BOX-')      
    prediction_list, input_text, sel_item = [], "", 0




    # IN lo que se esta escribiendo
    # Ignore Case parte en false
    # BOX la cajita negra para seleccionar el nombre
    posicion = 0

    while True:  # Event Loop

        
        event, values = window.read()


        
        if event == sg.WINDOW_CLOSED:
            break
        # pressing down arrow will trigger event -IN- then aftewards event Down:40 
        elif event.startswith('Escape'):
            window['-IN-'].update('')
        # Posible feature? Con escape se borra todos los inpus (1 y 2)


        elif (event == '-BOX-'):
            if len(values['-BOX-']) > 0:
                window['-IN-'].update(value=values['-BOX-'])
                #print("Aca se esta haciendoo el enter")
                output = values['-BOX-']
                #print(output)
                window['-BOX-CONTAINER-'].update(visible=False)


        elif event == '-IN-':
            #print(values)
            text = values['-IN-'].lower()
            if text == input_text:
                continue
            else:
                input_text = text
            prediction_list = []
            if text:
                #if values['-IGNORE CASE-']:
                prediction_list = [item for item in choices if item.lower().startswith(text)]
                #else:
                #    prediction_list = [item for item in choices if item.startswith(text)]

            list_element.update(values=prediction_list)
            sel_item = 0
            list_element.update(set_to_index=sel_item)

            if len(prediction_list) > 0:
                window['-BOX-CONTAINER-'].update(visible=True)
            else:
                window['-BOX-CONTAINER-'].update(visible=False)

        elif event == '-SEND-':
            
            if (output == None):
                print("Falta rellenar al Patrocinado")

            elif (output[0]):
                viejoDF = pd.read_excel(fnDatos, usecols=[1,2])
                arr = viejoDF.to_numpy()
                respuesta = patrocinios(output[0], arr)

                window["-output-"].update(respuesta)                          #se actualiza el texto
                window['-BOX-CONTAINER-3-'].update(visible=True)   
        elif event == "-Todos-":
            orderedPatrocinados = hacetodo()
            respuesta = cantidadpatrocinadores(orderedPatrocinados)
            poto = ''.join(respuesta)
            window["-output-"].update(poto)                   #se actualiza el texto
            window["-BOX-CONTAINER-3-"].update(visible=True)
    window.close()


if __name__ == '__main__':
    main()

