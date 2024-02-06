import PySimpleGUI as sg
from funcoes import get_contents


def pagina_inicial():
    
    layout = [
        [sg.Text('Escolha qual(is) conteúdo(s) deseja praticar:')],
    ]

    contents = get_contents()
    content_options = []
    for content in contents:
        checkbox_content = sg.Checkbox(text=content, key=content.split('.')[0])
        content_options.append(checkbox_content)

    layout.append(content_options)
    layout.append([])
    layout.append([sg.Button('Iniciar'), sg.Button('Cancelar')])

    return sg.Window('Estudo de Espanhol', layout=layout)




if __name__ == '__main__':

    window = pagina_inicial()
    window.read()
