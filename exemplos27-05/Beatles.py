import time

beatles = [] #Variavel dos beatles
    
beatles.append(" Paul McCartney")
beatles.append("George Har")
beatles.append("John Lennon")
beatles.append("Pete Best ")
beatles.append("Stu Sutcliffe")



for i in range(1):  #Solicitando ao usuario os novos integrantes
    Novos_Integrantes = input("Digite o nome de um membro novo dos Beatles: ")
   #Digite  Stu Sutcliffe ou Pete Best  
    beatles.append(Novos_Integrantes)
    
del beatles[3:] 


for i in range(1):  #Solicitando ao usuario os novos integrantes
    Novos_Integrantes1 = input("Digite o nome de um membro novo dos Beatles: ")
   #Digite  Stu Sutcliffe ou Pete Best  
    


beatles.insert(0, Novos_Integrantes)
beatles.insert(0, Novos_Integrantes1)


# Exibindo a lista atualizada
print("Lista atualizada dos Beatles:", beatles)


time.sleep(3)