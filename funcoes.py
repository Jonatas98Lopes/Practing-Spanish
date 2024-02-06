import os


DIRETORIO_CONTEUDOS = os.getcwd() + os.sep + 'contents'

def get_contents():
    os.chdir(DIRETORIO_CONTEUDOS)
    contents = os.listdir()
    os.chdir(os.pardir)
    return contents
    

    

if __name__ == '__main__': 
    get_contents()
    #with open('cotents\\hola_')