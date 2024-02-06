import PySimpleGUI as sg
from funcoes import get_contents


def pagina_inicial():
    
    layout = [
        [sg.Text('Escolha qual(is) conteúdo(s) deseja praticar:')],
    ]

    contents = get_contents()
    content_options = []
    for i, content in enumerate(contents):
        if i == 0:
            checkbox_content = sg.Checkbox(text=content, key=content.split('.')[0], default=True)
        else:
            checkbox_content = sg.Checkbox(text=content, key=content.split('.')[0])
        content_options.append(checkbox_content)

    layout.append(content_options)
    layout.append([])
    layout.append([sg.Button('Iniciar'), sg.Button('Cancelar')])

    return sg.Window('Estudo de Espanhol', layout=layout)



def pergunta(portugues):
    layout = [
        [sg.Text(f'Como dizer "{portugues}" em espanhol?')],
        [sg.Input(key='answer')],
        [sg.Text(key='invalid_answer', text_color='red')],
        [sg.Button('Enviar'), sg.Button('Limpar')]
    ]

    return sg.Window(title=portugues, layout=layout)



if __name__ == '__main__':

    window = pergunta('qual é o seu nome?')
    window.read()
