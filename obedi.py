import pyfirmata as f

try:
    arduino = f.Arduino('COM4')
    i = True
    print('Arduino connecté')
except:
    i = False
    print('Arduino non connecté')
while i:
    try:
        arduino.digital[2].write(1)
        arduino.digital[3].write(1)
    except:
        print('Arduino non connecté')
        break