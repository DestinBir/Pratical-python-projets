from time import *
import random as r


def mistake(paratest, usertest):
    error = 0
    for i in range(len(paratest)):
        try:
            if paratest[i] != usertest[i]:
                error += 1
        except:
            error += 1
    return error


def speed_time(time_s, time_e, userinput):
    time_delay = time_e - time_s
    time_r = round(time_delay, 2)
    speed = len(userinput)/time_r
    return round(speed)


if __name__ == '__main__':
    while True:
        ck = input(" .....Es-tu prêt à jouer : /n yes / no : ......")
        if ck == "yes":
            test = [
                "Facere repudiandae eius, odio rerum consequatur sed optio nisi aspernatur, aperiam quibusdam veritatis",
                "mon nom est Destin Baseme", "bienvenu sur ce logiciel cool"]

            test1 = r.choice(test)

            print("***** Verifions maintenant votre vitesse de saisi *****")
            print(test1)
            print()
            print()
            time_1 = time()
            testinput = input(" Mettre : ")
            time_2 = time()

            print("La vitesse de saisi est de : ", speed_time(time_1,time_2, testinput), " mot/sec")
            print("Erreur : ", mistake(test1, testinput))
        elif ck == "no":
            print(" .....Nous vous remercions..... ")
            break
        else:
            print(" .....Entrée non valide.....")