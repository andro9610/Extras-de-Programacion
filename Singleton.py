#Esta es la estructura del Singleton como tal
def Singleton(amorAGatito,yaHayAmor):
    if (amorAGatito == True):
            if(yaHayAmor == True):
                #Si el amor a gatito ya existe sabes que ya estas amando a gatito
                print("Ya estas amando a gatito")
            else:
                #Si todavia no amas a gatito pues te enamoras y entonces ya hay amor
                print("Enamorandote...")
                yaHayAmor = True

#Clase principal
def main():
    #Aqui se supone que el amor a gatito todavia no existe
    yaHayAmor = False
    #Para que el programa corra eternamente y pregunte cada vez si amas a gatito
    while(True):
        print("Amar a gatito?")
        print("1.Si 2.No")
        amorAGatito = bool(input())
        Singleton(amorAGatito,yaHayAmor)
          
#Esto hace que el programa corra            
if __name__ == "__main__":
    main()