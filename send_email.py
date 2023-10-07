import smtplib as s

ob = s.SMTP('smtp.gmail.com', 587)
ob.ehlo()
ob.starttls()
ob.login('biringaninedestin@gmail.com', 'destinbaseme')
subject = 'test python'
body = 'I love python'
message = 'subject:{}\n\n{}'.format(subject, body)
listadd = ['groupe5logiciel@gmail.com',
           'biringaninebaseme@gmail.com']
ob.sendmail('biringaninedestin@gmail.com', listadd, message)
print("message envoyé")
ob.quit()