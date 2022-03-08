from msilib.schema import Class
import os
from colorama import Fore, Back, Style

Entomologia=[]

class Orthopera:
    Antenas=""
    Pernas=""
    Tímpano=""
    Pronoto=""
    def __init__(self, ant, timp, perna,pro):
        self.Antenas=ant
        self.Pernas=perna
        self.Tímpano=timp
        self.Pronoto=pro

    def info (self):
        print("Antenas.....:" + self.Antenas)
        print("Pernas......:" + self.Pernas)
        print("Tímpano.....:" + self.Tímpano)
        print("Pronoto......:" + self.Pronoto)

def Menu ():
    os.system ('cls') or None
    print("1 - Chave de Identificação")
    print("2 - Famílias")
    print("3 - Finalizar")
    opc=input("Digite uma opção:")
    return opc

def Antena ():
    os.system('cls')
    n=input("Tipo de Antena.....:" + Fore.YELLOW)
    j=input(Fore.RESET + "Dimensões..........:" + Fore.YELLOW)
    k=input(Fore. RESET + "Infome o tipo de pernas......:" + Fore.YELLOW)
    l=input(Fore. RESET + "Tímpano..........:" + Fore.YELLOW)
    insetos=Orthopera(n, j, k, l)
    Entomologia.append(insetos)
    print(Fore.RESET + "Subordem Caelifera")
    os.system('pause')

def Famílias():
    os.system ('cls')
    n=input("Digite o nome da família: " + Fore.CYAN)
    j=input(Fore.RESET + "Nome do inseto:" + Fore.CYAN)
    k=input(Fore.RESET + "Ocorrência:" + Fore.CYAN)
    l=input(Fore.RESET + "Cor:" )
    inseto=Orthopera(n, j, k, l)
    print(Fore.RESET + "Família catalogada")
    os.system('pause')

ret=Menu()
while ret < "3":
    if ret =="1":
        Antena()
    if ret =="2":
        Famílias()
    ret=Menu()

os.system('cls') or None
print("Catálogo finalizado")



    



    





    


    



