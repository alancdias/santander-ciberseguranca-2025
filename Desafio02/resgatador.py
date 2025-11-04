import os
from cryptography.fernet import Fernet

#Primeira Etapa: Carregar a chave salva:
def carrega_chave():
    with open('chave.key', 'rb') as key_file:
        chave = key_file.read()
    return chave


#Segunda Etapa: Descriptografar um arquivo:
def descriptografa_arquivo(arquivo, chave):
    f = Fernet(chave)
    with open(arquivo, 'rb') as old_file:
        dados_encriptados = f.decrypt(old_file.read())
    with open(arquivo, 'wb') as new_file:
        new_file.write(dados_encriptados)


#Terceira Etapa: Listar os arquivos do diretório:
def listar_arquivos(diretorio):
    lista = [os.path.join(raiz, arquivo)
             for raiz, _, arquivos in os.walk(diretorio)
             for arquivo in arquivos
             if (arquivo != 'ransomware.py') and (not arquivo.endswith('.key'))]
    return lista


#Quarta Etapa: Descriptografar todos os arquivos de um diretório e subdiretórios:
def descriptografa_tudo(diretorio, chave):
    for arquivo in listar_arquivos(diretorio):
        descriptografa_arquivo(arquivo, chave)


#Quinta Etapa: Execução do resgate:
if __name__ == '__main__':
    diretorio = 'test_files'
    with open('estado.txt', 'r') as status_file:
        status = status_file.read()
    if status == 'criptografado':
        descriptografa_tudo(diretorio, carrega_chave())
        with open('estado.txt', 'w') as status_file:
            status_file.write('descriptografado')
    print('Os arquivos estão descriptografados')