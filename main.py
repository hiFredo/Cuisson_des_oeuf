import time
import platform
import winsound
# print("Cuisson en cours",end="",flush=True)
# for i in range(5):  #10s 
#     time.sleep(1) #block 1s
#     print(".",end="",flush=True)

# print("")
# print("Fin programme") 
 
# def afficher_points():
#     for i in range(10):  #10s 
#         time.sleep(1) #block 1s
#         print(".",end="",flush=True)

# def afficher_durre(d: int):
    
#     print("Cuisson en cours",end="",flush=True)
#     afficher_points()
#     d=d-10
#     while not d== 0 :
#         min = d//60 # division entière (pas de virgules)
#         sec = d-min*60        
#         print("")
#         print(f"Durrée restante : {min:02d}:{sec:02d}",end="",flush=True )
#         afficher_points()
#         d = d-10
#     print("") 
#     print("Cuisson terminée")

# print("Cuisson des oeuf ")
# print("_ _ _ _ _ _ _ _ ")
# print("a) Oeuf a la coque (3min) ")
# print("b) Oeuf mollets (6min) ")
# print("c) Oeuf dur (9min) ")
# while True :
#     choix = input("Votre choix est (a , b ou c ) : ")
#     if choix== "a" :
#         durre= 180 #(3min)
#         afficher_durre(durre)
#         break
#     elif choix=="b" :
#         durre= 360 #(6min)
#         afficher_durre(durre)
#         break
#     elif choix=="c" :
#         durre= 540 #(9min)
#         afficher_durre(durre)
#         break
#     else :
#         print("ERREUR : Veuille choisir entre les 3 options(a , b ou c )")

if platform.system() == "Windows":
 
    # Tu peux varier la féquence (aigue -> grave)
    frequency = 500
    duration = 500
    winsound.Beep(frequency, duration)
 
    # # D'autres sons si tu préfères
    # winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
    # winsound.PlaySound("SystemHand", winsound.SND_ALIAS)
 
# Si le script n'est pas exécuté sous windows 
else:
    print("Driiiiiiiiiiiing!!!")
