import os
RPG=[]

class MMORPG:
    nome=""
    Jogadores=0
    XPTotal=0
    Online=False
    def __init__(self, nome, jog):
        self.nome=nome
        self.Jogadores=jog
        self.XPTotal=int(jog)*8
        self.online=False

    def Ativar(self):
        self.online=True

    def Desativar(self):
        self.online=False

    def info(self):
        print("Nome.........:" + self.nome)
        print("Jogadores....:" + str(self.Jogadores))
        print("XPTotal......:" + str(self.XPTotal))
        print("Online........" + ("Sim" if self.online==True else "Não"))

def Menu():
    os.system('cls') or None
    print("1 - Novo Jogo")
    print("2 - Informações do Jogo")
    print("3 - Excluir jogo")
    print("4 - Realizar tutorial")
    print("5 - Deslogar do jogo")
    print("6 - Listar Jogos")
    print("7 - Sair")
    print("Quantidade de rpgs: "+str(len(RPG)))
    opc=input("Digite uma opção: ")
    return opc

def NovoRpg():
    os.system('cls') or None
    n=input("Nome do Jogo.....: ")
    j=input("Jogadores........: ")
    players=MMORPG(n,j)
    RPG.append(players)
    print("Novo jogo criado")
    os.system("pause")

def informações():
    os.system('cls') or None
    n=input("Informe o número do jogo que deseja ver as informações: ")
    try:
        RPG[int(n)].info()
    except:
        print("Jogo não existe na lista")
    os.system("pause")

def ExcluirJogo():
    os.system('cls') or None
    n=input("Informe o número do jogo que deseja Excluir: ")
    print("Jogo excluído")
    try:
        del RPG[int(n)]
    except:
        print("Jogo não existe na lista")
    os.system("pause")

def ativarJogo():
    os.system('cls') or None
    n=input("Informe o número do jogo que deseja logar: ")
    try:
        RPG[int(n)].Ativar()
        print("Jogo ativado")
    except:
        print("Jogo não existe na lista")
    os.system("pause")

def desativarJogo():
    os.system('cls') or None
    n=input("Informe o número do jogo que deseja deslogar: ")
    try:
        RPG[int(n)].Desativar()
        print("Jogo offline")
    except:
        print("Jogo não existe na lista")
    os.system("pause")

def listarJogos():
    os.system('cls') or None
    p=0
    for c in RPG:
        print(str(p)+ " - " + c.nome)
        p=p+1
    os.system("pause")

ret=Menu()
while ret < "7":
    if ret=="1":
        NovoRpg()
    elif ret=="2":
        informações()
    elif ret=="3":
        ExcluirJogo()
    elif ret=="4":
        ativarJogo()
    elif ret=="5":
        desativarJogo()
    elif ret=="6":
        listarJogos()
    ret=Menu()

os.system('cls') or None
print("Programa finalizado")







        
    

    


