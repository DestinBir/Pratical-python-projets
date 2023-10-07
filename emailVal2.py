import email
import re

email_condition1 = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
email_condition2 = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$+[.]\w{2,3}$"

user_email = input(' Entrer votre adresse mail: ')

if re.search(email_condition1, user_email):
    print(" Adresse mail validé ")
else:
    print(" Adresse mail erronée ")
