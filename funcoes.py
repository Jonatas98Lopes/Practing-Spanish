import os
from random import choice
import json


DIRETORIO_CONTEUDOS = os.getcwd() + os.sep + 'contents'

with open('random_data.json', 'r', encoding='utf-8') as file:
    DADOS_ARBITRARIOS = json.load(file)


def escolher_dado_json(key:str):
    if key == "nomes":
        nome = choice(DADOS_ARBITRARIOS["nomes"])
        return nome
    
    elif key == 'paises':
        paises = DADOS_ARBITRARIOS["country_data"]["paises"]
        nacionalidades_br = DADOS_ARBITRARIOS["country_data"]["nacionalidades_br"]
        nacionalidades_es = DADOS_ARBITRARIOS["country_data"]["nacionalidades_es"]

        pais = choice(paises)
        pais_index = paises.index(pais)

        nacionalidade_br = nacionalidades_br[pais_index]
        nacionalidade_es = nacionalidades_es[pais_index]


        return pais, nacionalidade_br, nacionalidade_es
    
    elif key == 'cidades':
        cidade = choice(DADOS_ARBITRARIOS["cidades"])
        return cidade


def get_contents():
    os.chdir(DIRETORIO_CONTEUDOS)
    contents = os.listdir()
    os.chdir(os.pardir)
    return contents

    
def abre_arquivo(file_name):    
    file_content = []
    with open(f'contents\\{file_name}', 'r', encoding='utf-8', newline='') as file:
        file_content = file.readlines()
    return file_content


def remove_caractere(string:str, caractere:str) -> str:
    if caractere in string:
        return string.replace(caractere, '')
    

def substitui_caractere_lista(lista:list, caractere:str):
    for index, line in enumerate(lista):
        new_string = remove_caractere(line, '\n')
        lista[index] = new_string


def get_palavras_portugues(file):
    file_content = abre_arquivo(file)
    words_portuguese = []
    for content in file_content:
        filtered_content = content.split(':')[0].strip()
        if filtered_content == '\r\n': continue
        words_portuguese.append(filtered_content)
    return words_portuguese


def escolhe_palavra_portugues_aleatorio(file):
    lista = get_palavras_portugues(file)
    while True:
        random_result = choice(lista)
        if random_result not in('', ' ', '\r', '\n', '\r\n'):
            return choice(lista)


def encontra_correspodencia_espanhol(palavra_ptBr, file):
    file_content = abre_arquivo(file)
    for content in file_content:
        if content.split(':')[0] == palavra_ptBr:
            return content.split(':')[1].strip()

def adiciona_valor_valido(string:str):
    if string.find('[NOME]') != -1: 
        nome = choice(DADOS_ARBITRARIOS["nomes"])
        new_string = string.replace('[NOME]', nome)

    elif string.find('[NACIONALIDADEBR]') != -1: 
        nacionalidade_br = choice(DADOS_ARBITRARIOS["nacionalidades-pt"])
        new_string = string.replace('[NACIONALIDADEBR]', nacionalidade_br)

    elif string.find('[PAÍS]') != -1: 
        nacionalidade_br = choice(DADOS_ARBITRARIOS["paises"])
        new_string = string.replace('[PAÍS]', nacionalidade_br)
    
    elif string.find('[NACIONALIDADEES]') != -1: 
        nacionalidade_es = choice(DADOS_ARBITRARIOS["nacionalidades-es"])
        new_string = string.replace('[NACIONALIDADEES]', nacionalidade_es)

    elif string.find('[CIDADE]') != -1: 
        cidade = choice(DADOS_ARBITRARIOS["cidades"])
        new_string = string.replace('[CIDADE]', cidade)

    return new_string


def gerando_dicionario(file):
    content = abre_arquivo(file)
   
    substitui_caractere_lista(content, '\n')
    
    dict_exercicios = {}
    for value in content:
        
        value = value.replace('\n','').replace('\r','')
    
        if value.find('[NOME]') != -1:
            nome = escolher_dado_json("nomes")
            value = value.replace('[NOME]', nome)

        elif value.find('[PAÍS]') != -1:
            pais, nacionalidade_br, nacionalidade_es = escolher_dado_json("paises")
            value = value.replace('[PAÍS]', pais).replace('[NACIONALIDADEBR]', nacionalidade_br)\
                .replace('[NACIONALIDADEES]', nacionalidade_es)

        elif value.find('[CIDADE]') != -1:
            cidade = escolher_dado_json("cidades")
            value = value.replace('[CIDADE]', cidade)

        elif value.find('[PROFISSÃO]') != -1:
            random_profissao = escolhe_palavra_portugues_aleatorio('profesiones.txt')
            correspondencia = encontra_correspodencia_espanhol(random_profissao, 'profesiones.txt')
            value = value.replace('[PROFISSÃO]', random_profissao)
            value = value.replace('[PROFISION]', correspondencia)
        
        portugues, espanhol = value.split(':')

        if espanhol.find(";") != -1:
            espanhol = espanhol.split(';')
        dict_exercicios[portugues] = espanhol

    
    return dict_exercicios 