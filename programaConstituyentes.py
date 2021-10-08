from numpy import string_
import numpy
import pandas as pd
from openpyxl import load_workbook
import math
import sys
import os.path


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import PySimpleGUI as sg


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

        


def aQuienPatrocina(nombreConstituyente):
    patrocinador = 0
    patrocinado = 1
    viejoDF = pd.read_excel(fnDatos, usecols=[1,2])
    arrayReglamento = viejoDF.to_numpy()

    for patrocinio in arrayReglamento:
        if patrocinio[patrocinador] == nombreConstituyente:
            return patrocinio[patrocinado]

def nombreValidoPatrocinador(nombreConstituyente):
    patrocinador = 0
    viejoDF = pd.read_excel(fnDatos, usecols=[1,2])
    arrayReglamento = viejoDF.to_numpy()

    var = False

    for patrocinio in arrayReglamento:
        if patrocinio[patrocinador] == nombreConstituyente:
            var = True
    return var

def nombreValidoPatrocinado(nombreConstituyente):
    patrocinado = 1
    viejoDF = pd.read_excel(fnDatos, usecols=[1,2])
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

#Modifica el patrocinio de un constituyente patrocinador
def modificarPatrocinio(ConstituyentePatrocinador, ConstituyentePatrocinado):

    
    viejoDF = pd.read_excel(fnDatos, usecols=[1,2])
    viejoArr = viejoDF.to_numpy()
    patrocinador = 0
    patrocinado = 1
    
    
    for patrocinio in viejoArr:
        if patrocinio[patrocinador] == ConstituyentePatrocinador:
            patrocinio[patrocinado] = ConstituyentePatrocinado

    newDataFrame = pd.DataFrame(viejoArr, index = viejoDF.index, columns=viejoDF.columns)

    newDataFrame.to_excel(fnDatos,sheet_name='Sheet1',startcol=0, startrow=0)

    return "El patrocinio de " + ConstituyentePatrocinador + " a " + ConstituyentePatrocinado +" ha sido modificado con éxito!"



def IngresarPatrocinio(ConstituyentePatrocinador, ConstituyentePatrocinado):
    if yaPatrocino(ConstituyentePatrocinador):
        respuesta = "El patrocinio de " + ConstituyentePatrocinador+ " a " + ConstituyentePatrocinado + " NO se registro, ya que " + ConstituyentePatrocinador + " se encuentra patrocinando a alguien"
        return respuesta
    
    elif nombreValidoPatrocinador(ConstituyentePatrocinador) == False:
        return "Esta ingresando mal al patrocinador, revise de nuevo, ya que " + ConstituyentePatrocinador + " no está registrad@"

    elif nombreValidoPatrocinador(ConstituyentePatrocinado) == False:
        return "Esta ingresando mal al constituyente patrocinado, revise de nuevo, ya que " + ConstituyentePatrocinador + " no está registrad@"

    else:
        viejoDF = pd.read_excel(fnDatos, usecols=[1,2])
        viejoArr = viejoDF.to_numpy()
        patrocinador = 0
        patrocinado = 1

        for patrocinio in viejoArr:
            if patrocinio[patrocinador] == ConstituyentePatrocinador:
                patrocinio[patrocinado] = ConstituyentePatrocinado

        newDataFrame = pd.DataFrame(viejoArr, index = viejoDF.index, columns=viejoDF.columns)

        newDataFrame.to_excel(fnDatos,sheet_name='Sheet1',startcol=0, startrow=0)

        return "El patrocinio de " + ConstituyentePatrocinador + " a " + ConstituyentePatrocinado +" ha sido ingresado con éxito!"


#while(True):

 #   patrocinadorUsuario = input("Ingrese nombre constituyente patrocinador: ")

  #  patrocinadoUsuario = input("Ingrese nombre constituyente patrocinado: ")

   # IngresarPatrocinio(patrocinadorUsuario, patrocinadoUsuario)


#Aqui se agregan las funciones para las funcionalidades de chequeo de cantidad de patrocinadores



def patrocinadoresDe(nombreConstituyente, arr):
    
    patrocinadores = []
    patrocinador = 0
    patrocinado = 1

    for patrocinio in arr:
        if patrocinio[patrocinado] == nombreConstituyente:
            patrocinadores.append(patrocinio[patrocinador])
    
    return patrocinadores


def Chequeo(patrocinado, nro_patrocinadores, escanos_reservados, nro_escanos_reservados, nro_no_reservados):
    if patrocinado in escanos_reservados:
        if nro_patrocinadores > nro_escanos_reservados:
            respuesta = "OJO, "+patrocinado+" tiene "+str(nro_patrocinadores)+" patrocinadores, solo eran necesarios "+str(nro_escanos_reservados)+" patrocinios en esta comisión."
            return respuesta 
        else: 
            respuesta = "Por ahora " + patrocinado + " tiene " + str(nro_patrocinadores) + " patrocinadores, en esta comisión le corresponden "+str(nro_escanos_reservados)+" patrocinadores."
            return respuesta
    else:
        if nro_patrocinadores > nro_no_reservados:
            respuesta = "OJO, " + patrocinado + " tiene " + str(nro_patrocinadores) + " patrocinadores, solo eran necesarios "+str(nro_no_reservados)+" patrocinios en esta comisión."
            return respuesta 
        else: 
            respuesta = "Por ahora " + patrocinado + " tiene " + str(nro_patrocinadores) + " patrocinadores, en esta comisión le corresponden "+str(nro_no_reservados)+" patrocinadores."
            return respuesta



"""
    Autocomplete input
    Thank you to GitHub user bonklers for supplying to basis for this demo!
    There are 3 keyboard characters to be aware of:
    * Arrow up - Change selected item in list
    * Arrow down - Change selected item in list
    * Escape - Erase the input and start over
    * Return/Enter - use the current item selected from the list
    You can easily remove the ignore case option by searching for the "Irnore Case" Check box key:
        '-IGNORE CASE-'
    The variable "choices" holds the list of strings your program will match against.
    Even though the listbox of choices doesn't have a scrollbar visible, the list is longer than shown
        and using your keyboard more of it will br shown as you scroll down with the arrow keys
    The selection wraps around from the end to the start (and vicea versa). You can change this behavior to
        make it stay at the beignning or the end
    Copyright 2021 PySimpleGUI


    - Autocompletado onput listo
    TODO:
    Almacenar el input ya autocompletado  en un variable. Primero un enter para confirmar el valir del dropdown y un enter despues para almacnera el valro en una varibale
    verificar si el valor cumple las restricciones
    
    """


def main():
    # The list of choices that are going to be searched
    # In this example, the PySimpleGUI Element names are used
    patrocinador = 0
    patrocinado = 1
    viejoDF = pd.read_excel(fnDatos, usecols=[1,2])
    choicesConstituyentes = []
    arrayReglamento = viejoDF.to_numpy()



    nro_escanos_reservados = 5
    nro_no_reservados = 6

    
    escanos_reservados = ["Tiare Aguilera", "Victorino Antilef", "Wilfredo Bacián","Alexis Caiguan","Rosa Catrileo","Eric Chinga","Felix Galleguillos","Isabel Godoy","Lidia González","Luis Jiménez",
            "Francisca Linconao","Natividad Llanquileo","Elisa Loncón","Isabella Mamami","Adolfo Millabur","Fernando Tirado","Margarita Vargas"]


    for patrocinio in arrayReglamento:
        choicesConstituyentes.append(str(patrocinio[patrocinador]))
   
    #choices = ["Tom", "Cebolla", "Poto", "Cholo", "Tomate", "Tetera"] # ACA TIENE QUE IR UNA LISTA CON LOS CONSTITUYENTES
    choices = choicesConstituyentes

    input_width = 100                #El ancho de la caja del input
    num_items_to_show = 6            #Cantidad de valores en el dropdown [predictions]

    output = None
    output_2 = None
    layout = [
        [sg.Text('Usted está trabajando en la comisión 1: La de reglamento', size=(100, 2))],

        [sg.Text('OJO, solo chequea esta caja cuando estés seguro que es necesario cambiar un patrocinio')],

        [sg.Checkbox(  
            #["Ingresar un patrocinio nuevo","Sobre-escribir un Patrocinio existente"],key='Modo', size=(100, 2))],
            "Chequea esta caja si quieres la opción de sobre-escribir patrocinios ya ingresados", key='Modo', default=False)],

        [sg.Text('Seleccione Constituyente Patrocinad@:')],
        [sg.Input(size=(input_width, 1), enable_events=True, key='-IN-')],

        [sg.pin(sg.Col([[sg.Listbox(values=[], size=(input_width, num_items_to_show), enable_events=True, key='-BOX-',
                                    select_mode=sg.LISTBOX_SELECT_MODE_SINGLE, no_scrollbar=True)]],
                       key='-BOX-CONTAINER-', pad=(0, 0), visible=False     #La caja donde se muestra dropdown es el BOX CONTAINER
                       )
                       )],

        [sg.Text('Seleccione Constituyente Patrocinador:')],
        [sg.Input(size=(input_width, 1), enable_events=True, key='-IN-2-')],

        [sg.pin(sg.Col([[sg.Listbox(values=[], size=(input_width, num_items_to_show), enable_events=True, key='-BOX-2-',
                                    select_mode=sg.LISTBOX_SELECT_MODE_SINGLE, no_scrollbar=True)]],
                       key='-BOX-CONTAINER-2-', pad=(0, 0), visible=False     #La caja donde se muestra dropdown es el BOX CONTAINER
                       )
                       )],
        

        #La caja donde se muestra dropdown es el BOX CONTAINER
        



        [sg.Button("Enviar", key = "-SEND-" )],


        [sg.pin(sg.Col([[sg.Text('Hola', key = "-output-", justification='center')]],
                        key='-BOX-CONTAINER-3-', pad=(0, 0), visible=False)
                       )],

        [sg.pin(sg.Col([[sg.Text('Hola', key = "-chequeo-", justification='center')]],
                        key='-BOX-CONTAINER-4-', pad=(0, 0), visible=False)
                       )]
        ]
        

    window = sg.Window('Preoceso de selección de comisiones', layout, return_keyboard_events=True, finalize=True, font= ('Helvetica', 16))

    list_element:sg.Listbox = window.Element('-BOX-')           # store listbox element for easier access and to get to docstrings
    list_element_2:sg.Listbox = window.Element('-BOX-2-') 
    prediction_list, input_text, sel_item = [], "", 0





    # IN lo que se esta escribiendo
    # Ignore Case parte en false
    # BOX la cajita negra para seleccionar el nombre

    while True:  # Event Loop
        event, values = window.read()


        
        if event == sg.WINDOW_CLOSED:
            break
        # pressing down arrow will trigger event -IN- then aftewards event Down:40 
        elif event.startswith('Escape'):
            window['-IN-'].update('')        
            window['-BOX-CONTAINER-'].update(visible=False)
            window['-IN-2-'].update('')        
            window['-BOX-CONTAINER-2-'].update(visible=False)
        # Posible feature? Con escape se borra todos los inpus (1 y 2)


            
        elif event.startswith('Down') and len(prediction_list):
            sel_item = (sel_item + 1) % len(prediction_list)
            list_element.update(set_to_index=sel_item, scroll_to_index=sel_item)
            list_element_2.update(set_to_index=sel_item, scroll_to_index=sel_item)
        # Revisar!!!

        
        elif event.startswith('Up') and len(prediction_list):
            sel_item = (sel_item + (len(prediction_list) - 1)) % len(prediction_list)
            list_element.update(set_to_index=sel_item, scroll_to_index=sel_item)
            list_element_2.update(set_to_index=sel_item, scroll_to_index=sel_item)
        # Revisar !!!


        # Borramos evento   event == '\r'    de enter para evitar bugs
        elif (event == '-BOX-'):
            if len(values['-BOX-']) > 0:
                window['-IN-'].update(value=values['-BOX-'])
                #print("Aca se esta haciendoo el enter")
                output = values['-BOX-']
                #print(output)
                window['-BOX-CONTAINER-'].update(visible=False)
        #output 

        elif (event == '-BOX-2-'):
            if len(values['-BOX-2-']) > 0:

                window['-IN-2-'].update(value=values['-BOX-2-'])
                #print("Aca se esta haciendoo el enter2")
                output_2 = values['-BOX-2-']
                #print(output_2)
                window['-BOX-CONTAINER-2-'].update(visible=False)


                
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

        elif event == '-IN-2-':
            #print(values)
            text = values['-IN-2-'].lower()
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

            list_element_2.update(values=prediction_list)
            sel_item = 0
            list_element_2.update(set_to_index=sel_item)

            if len(prediction_list) > 0:
                window['-BOX-CONTAINER-2-'].update(visible=True)
            else:
                window['-BOX-CONTAINER-2-'].update(visible=False)

        elif event == '-SEND-':
            
            if (output == None):
                print("Falta rellenar al Patrocinado")

            if (output_2==None):
                print("Falta rellenar al Patrocinador")

            elif (output[0] and output_2[0] ):

                modo = window.find_element('Modo')

                if (modo.Get()==False):
                    respuesta = IngresarPatrocinio(output_2[0], output[0])         #Texto que indica el cambio en el excel

                else:
                    respuesta = modificarPatrocinio(output_2[0], output[0])


                #respuesta2 =  output[0] + " esta siendo patrocinada por " + str(len(patrocinadoresDe(output[0]))) + " personas"               #Texto que indica los patrocinios totales                  
                viejoDF = pd.read_excel(fnDatos, usecols=[1,2])
                viejoArr = viejoDF.to_numpy()

                nro_patrocinadores = len(patrocinadoresDe(output[0], viejoArr))

                respuesta2 = Chequeo(output[0], nro_patrocinadores, escanos_reservados, nro_escanos_reservados, nro_no_reservados)

                window["-output-"].update(respuesta)                          #se actualiza el texto
                window['-BOX-CONTAINER-3-'].update(visible=True)              #la caja que contiene el texto se hace visible

                window["-chequeo-"].update(respuesta2)                         #se actualiza el texto de chequo
                window['-BOX-CONTAINER-4-'].update(visible=True)           #la caja que contiene el texto de chequo se hace visible

            #AQUI CHEQUEAR Y ENVIAR DATOS

                window['-IN-'].update('')        
                window['-IN-2-'].update('')     
                window['-BOX-'].update('')   
                window['-BOX-2-'].update('')   
            #elif (output[0] == 'Tom'):
            #    print("Falta ASASA")
            #elif CONDICION DEL MODELO
                

        
    window.close()


if __name__ == '__main__':
    main()





        









