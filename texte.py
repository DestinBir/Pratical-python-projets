import pywhatkit as pw

txt = """La résurrection signifie que nous ne devons pas avoir peur de la mort, car elle nous libérera de cette souffrance. 
Dans les Actes des Apôtres, chapitre 2, versets 22 à 24, il est fait mention de la résurrection de Jésus vainqueur de la mort."""

pw.text_to_handwriting(txt, "texte1.png", [0,0,138])
print("----End----")