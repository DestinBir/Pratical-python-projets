from curses import*

email = input(" Entrer votre adresse email: ")
a = 0
b = 0
c = 0
if len(email) >= 6:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@") == 1):
            if (email[-4] == ".") ^ (email[-3] == "."):
                for i in email:
                    if i == i.isspace():
                        a = 1
                    elif i.isalpha():
                        if i == i.upper():
                            b = 1
                    elif i.isdigit():
                        continue
                    elif i in ["_", ".", "@"]:
                        continue
                    else:
                        c = 1
                if a == 1 or b == 1 or c == 1:
                    print(" Adresse mail erroné, code 5")
                else:
                    print(" Adresse mail valide")
            else:
                print(" Adresse mail erroné, code 4")
        else:
            print(" Adresse mail erroné, code 3")
    else:
        print(" Adresse mail erroné, code 2")
else:
    print(" Adresse mail erroné, code 1")