## 💻 Desafio de Projeto: Simulando Malwares de Captura de Dados Simples em Python e Aprendendo a se Proteger

Este desafio faz parte do Bootcamp Santander - Cibersegurança 2025, em parceria do Santander com a DIO.

O objetivo é simular, em um ambiente controlado, o comportamento de [*malwares*](https://www.malwarebytes.com/pt-br/malware) que tentam coletar dados da máquina do usuário.

Serão simulados dois tipos de *malware*: um [*ransomware*](https://pt.wikipedia.org/wiki/Ransomware "O que é um ransomware?") e um [*keylogger*](https://www.malwarebytes.com/pt-br/keylogger).

### Ameaça 1: 🔀 *Ransomware*
Primeiramente, iremos realizar, em um ambiente controlado, a encriptação e decriptação de um conjunto de arquivos utilizando Python, simulando o comportamento de um *ransomware*. 

#### 🎯 Ambiente alvo:
O ambiente a ser criptografado será a pasta `test_files` deste repositório, a qual contém arquivos de tipos variados. A criptografia será feita a nível binário, de forma que a encriptação e a decriptação possam ser realizadas com uma única chave de forma semelhante. Assim, não apenas textos serão codificados, mas também imagens, músicas, programas e qualquer outro arquivo.

#### Agente de criptografia:
O processo de criptografia será realizado pelo utilizando o módulo Fernet da biblioteca Python [`cryptography`](https://pypi.org/project/cryptography/).


#### Encriptação
A encriptação é realizada pelo arquivo `ransomware.py`.

O arquivo, inicialmente, cria uma chave de criptografia e a salva no arquivo `chave.key`. Com a chave criada, esta é utilizada para encriptar todos os arquivos da pasta `test_files`, a menos que o arquivo se chame "ransomware.py" ou "chave.key", para evitar a encriptação dos próprios arquivos responsáveis por ela.

⚠️ A chave gerada será diferente cada vez que o código for executado. Caso a encriptação seja feita sem salvar a chave, pode não ser possível reverter o processo.

Por fim, o código gera o arquivo chamado `LEIA_ISTO.txt`, com as instruções para resgate dos dados. O arquivo é deixado automaticamente na máquina alvo.

#### Decriptação
A descriptação dos arquivos encriptados é realizada pelo arquivo `resgatador.py`, que usa a chave salva no arquivo `chave.key` para reverter a criptografia.

⚠️ Se os arquivos não estiverem criptografados e o código do arquivo `resgatador.py` for executado, os arquivos alvo serão encriptados. Para tentar reduzir a chance de criptografar os arquivos por acidente, tanto `ransomware.py` quanto `resgatador.py` verificam o estado da pasta alvo, o qual é gravado no arquivo `estado.txt` e só são executados se o estado permitir.


### Ameaça 2: ⌨️ *Keylogger*
Outra ameaça a ser simulada é o comportamento de um *keylogger*, que captura todas as teclas pressionadas e as envia para o atacante, seja por arquivos salvos localmente ou por *e-mail*.

#### Registro de teclas
O registro das teclas pressionadas é feito pelo arquivo `keylogger.py`, que utiliza a biblioteca Python [`pynput`](https://pypi.org/project/pynput/) e salva no arquivo `key_log.txt` todas as teclas pressionadas durante sua execução.

### Prevenção
Dentre as formas de prevenção contra *malwares*, podemos destacar:
- Uso de antivírus e *firewall* que rastreie o acesso à máquina do usuário;
- Bloqueio de tela quando não estiver utilizando o computador;
- Evitar inserir mídias desconhecidas, como pendrives, HDs externos;
- Evitar baixar conteúdo em sites não confiáveis;
- Evitar clicar em links e responder e-mails suspeitos. 

---
Alan C. Dias, 2025

