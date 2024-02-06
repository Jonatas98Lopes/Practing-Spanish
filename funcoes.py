import os


DIRETORIO_CONTEUDOS = os.getcwd() + os.sep + 'contents'



def get_contents():
    os.chdir(DIRETORIO_CONTEUDOS)
    contents = os.listdir()
    os.chdir(os.pardir)
    return contents
    

def open_file(file_name):    
    file_content = []
    with open(f'contents\\{file_name}', 'r', encoding='utf-8') as file:
        for line in file:
            file_content.append(line)
    return file_content


def remove_caractere(string:str, caractere:str) -> str:
    if caractere in string:
        return string.replace(caractere, '')
    

def substitui_caractere_lista(lista:list, caractere:str):
    for index, line in enumerate(lista):
        new_string = remove_caractere(line, '\n')
        lista[index] = new_string

if __name__ == '__main__': 
    content = open_file('hola_I.txt')
    content.pop()
    substitui_caractere_lista(content, '\n')
    
    dict_exercicios = {}
    for value in content:
        portugues, espanhol = value.split(':')

        if espanhol.find(';') != -1: 
            espanhol = espanhol.split(';')

        dict_exercicios[portugues] = espanhol
    
    print()

    
    