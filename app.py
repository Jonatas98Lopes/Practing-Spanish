from interfaces import *
import PySimpleGUI as sg
from funcoes import gerando_dicionario

window = pagina_inicial()
event, values = window.read()

if event == 'Iniciar':

    window.close()

    contents = []
    for key, value in values.items():
        if value:
            contents.append(f'{key}.txt')
    
    for content in contents:
        dict_exercicios = gerando_dicionario(content)

        for exercicio, answer in dict_exercicios.items():

            window = pergunta(exercicio)
            while True:
                event, values = window.read()
                
                if event == sg.WINDOW_CLOSED:
                    window.close() 
                    break

                elif event == 'Enviar':
                    if values['answer'].strip() in answer:
                        window.close()
                        break
                    else:
                        window['answer'].update('')
                        window['invalid_answer'].update('Incorreto, tente novamente.')
                
                elif event == 'Limpar':
                    window['answer'].update('')


else:
    window.close()