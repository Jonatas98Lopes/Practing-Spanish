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

        fechar_janela = False

        for exercicio, answer in dict_exercicios.items():

            window = pergunta(exercicio)
            while True:
                event, values = window.read()
                
                if event == sg.WINDOW_CLOSED:
                    fechar_janela = True
                    window.close() 
                    break

                elif event == 'Enviar':
                    
                    if type(answer) == list: 
                        lower_answer = []
                        [lower_answer.append(sentence.lower().strip()) for sentence in answer]

                        if values['answer'].lower().strip() in lower_answer:
                            window.close()
                            break
                        else:
                            window['answer'].update('')
                            window['invalid_answer'].update('Incorreto, tente novamente.')
                    else: 
                        if values['answer'].lower().strip() in answer.lower():
                            window.close()
                            break
                        else:
                            window['answer'].update('')
                            window['invalid_answer'].update('Incorreto, tente novamente.')
                
                elif event == 'Limpar':
                    window['answer'].update('')

            if fechar_janela: break

else:
    window.close()
    