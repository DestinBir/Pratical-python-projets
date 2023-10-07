b = int(input('Entrez la borne inférieure: '))
a = int(input('Entrez la borne supérieure: '))
nombres = []

def estpremier(x):
    if x <=1:
        return False
    else:
        for i in range(2, x):
            if x % i == 0:
                return False
    return True


if b > a or (a and b <= 3):
    print("Veuillez borner correctement votre intervalle. \nCe message s'affiche soit: \n =====> la borne inférieure est inférieure ou égale à 3 \n =====> la borne inférieure est inférieur à la supérieure ")
else:
    for i in range (a+1):
        if estpremier(i):
            nombres.append(i)
    for i in range (b,a+1):
        
        if i % 2 == 0:
            for j in nombres:
                for k in nombres:
                    if j + k == i:
                        print("==> ("+str(j)+", "+str(k)+") = "+str(i))

                            
                        
            
print('\n\nVoila la conjecture de Goldbach \nMerci et à bientôt')