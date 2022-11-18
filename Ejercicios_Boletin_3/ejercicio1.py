import time
import random

NUM_MAX_CUEVAS:int = 5
CONST_PUNTOS:int = 100

exit:bool = False
dragon_maligno:int
cueva:str
puntos:int = 0
opcion_salir:str

cadena:str = '''
       \****__              ____                                              
         |    *****\_      --/ *\-__                                          
         /_          (_    ./ ,/----'                                         
           \__         (_./  /                                                
              \__           \___----^__                                       
               _/   _                  \                                      
        |    _/  __/ )\"\ _____         *\                                    
        |\__/   /    ^ ^       \____      )                                   
         \___--"                    \_____ )                                  
                                          "
'''
while not(exit):
    for i in range(NUM_MAX_CUEVAS):
        if i == 0:
            print("===============================================================")
            print("|                     EL REINO DEL DRAGÓN                     |")
            print("===============================================================")
            print("")
            time.sleep(1)
            print("                       COMIENZA EL JUEGO                       ")
            print("")
            print(cadena)
            print("")
            time.sleep(1)
            print(f"Te encuentras con 2 cuevas, una tiene un dragón bueno que\n"
                  f"te dará un tesoro pero el otro dragón es malo y te matará\n")
            time.sleep(1)

        print(f"Te encuentras en la zona {i + 1} de {NUM_MAX_CUEVAS}\n")

        dragon_maligno = random.getrandbits(1) + 1

        print("Escoja la cueva A o la cueva B")
        cueva = input()

        time.sleep(1)

        if cueva.lower() == "a" or cueva.lower() == "b":
            if (cueva.lower() == "a" and dragon_maligno == 1) or (cueva.lower() == "b" and dragon_maligno == 2):
                print("HAS ENTRADO EN LA CUEVA DEL DRAGÓN MALO\n")
                break
            else:
                print("Has entrado en la cueva del dragón bueno\nHas ganado 100 puntos\n")
                puntos+=CONST_PUNTOS
        else:
            print("Has introducido un caracter erroneo, el dragón te ha fulminado...\n")
            break

    print(f"Has acabado con {puntos} puntos")

    puntos = 0

    if puntos == (NUM_MAX_CUEVAS * CONST_PUNTOS):
        print("HAS GANADO")
    else:
        print("GAME OVER")

    print("¿Quieres volver a jugar? (Si - S, No - N)")
    opcion_salir = input()
    if opcion_salir.lower() == "n":
        exit = True
    elif opcion_salir.lower() != "s" and opcion_salir.lower() != "n":
        print("Caracter erróneo, el juego ha finalizado")
        exit = True
    else:
        print("\n\n\n\n\n\n\n\n\n")

print("\n\n\n\n<=============================================================>")
print("                       GRACIAS POR JUGAR                       ")