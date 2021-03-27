from socket import *
from datetime import datetime

def Buscador(arquivo):
    dt = DataLog()
    #input de ip e portas que deseja vascular
    ip = str(input("IP do servidor: "))
    start = int(input("Porta inicial: "))
    end=int(input("Porta final: "))

    #Escrevendo logs
    arquivo.write("{} IP do servidor: {}\n".format(dt,ip))
    arquivo.write("{} Porta inicial: {}\n".format(dt,start))
    arquivo.write("{} Porta final: {}\n".format(dt,end))
    print("Scan IP {}".format(ip))
    for port in range(start,end):
        print("Teste Porta"+str(port)+"....")
        s=socket(AF_INET, SOCK_STREAM)
        s.settimeout(5)
        if(s.connect_ex((ip,port))==0):
            print("porta", port, "aberta")
            dt1 = DataLog()
            arquivo.write("{} Porta aberta {}\n".format(dt1,port))
        s.close()

#função para escrever log
def WriteLog():
    msg="Scanneamento terminou, realizado com sucesso"
    try:
        arquivo = open("ScannerPort.log","w")
        Buscador(arquivo)
        arquivo.close()
    except:
        msg="Erro. Verifique que você digitou informações ou se o servidor está on-line"
    finally:
        print(msg)

#função para gerar data dos eventos
def DataLog():
    data = datetime.now()
    tamanho = len(str(data)) - 7
    data2 = str(data)
    
    return data2[0:tamanho]

def Letreiro():
    print("<---------------------------------->")
    print("Scanner de porta")
    print("<---------------------------------->")

Letreiro()
WriteLog()
