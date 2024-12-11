import os

# 1 retorna a pasta atual
print(os.getcwd())

# 2 listar arquivos e pastas 

print(os.listdir())

# 3 versão do sistema

os.system('ver')

# 4 tras as configurações da maquina

os.system('systeminfo')

# 5 limpar a tela do terminal

os.system('cls')

# 6 desligar o computador

# os.system('shutdown /s')
# os.system('shutdown /s /t 0') desliga imediatamente
# os.system('shutdown /a')

def delisgarPC():
    os.system('shutdown /s /t 3600')

def delisgarMeiaH():
    os.system('shutdown /s /t 1800')

def cancelarDelisgamento():
    os.system('shutdown /a')