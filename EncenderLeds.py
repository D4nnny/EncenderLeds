import pyfirmata
import time
ard = pyfirmata.Arduino('COM3')
print("Conectado")

Led1 = ard.digital[2]
Led2 = ard.digital[3]
Led3 = ard.digital[4]
Led4 = ard.digital[5]
Led5 = ard.digital[6]
Led6 = ard.digital[7]


def asc():
    Led1.write(1)
    time.sleep(.2)
    Led2.write(1)
    time.sleep(.2)
    Led3.write(1)
    time.sleep(.2)
    Led4.write(1)
    time.sleep(.2)
    Led5.write(1)
    time.sleep(.2)
    Led6.write(1)
    time.sleep(.2)
    Led1.write(0)
    Led2.write(0)
    Led3.write(0)
    Led4.write(0)
    Led5.write(0)
    Led6.write(0)


def desc():
    Led6.write(1)
    time.sleep(.2)
    Led5.write(1)
    time.sleep(.2)
    Led4.write(1)
    time.sleep(.2)
    Led3.write(1)
    time.sleep(.2)
    Led2.write(1)
    time.sleep(.2)
    Led1.write(1)
    time.sleep(.2)
    Led6.write(0)
    Led5.write(0)
    Led4.write(0)
    Led3.write(0)
    Led2.write(0)
    Led1.write(0)

def op():
    leds = input("Menu\nSeleccione '1' para encender de manera ascendente\nSeleccione '2' para encender de manera descendente \n").upper()
    if leds == '1':
        while True:
            asc()
            break
    elif leds == '2':
        while True:
            desc()
            break
    
while True:
    op()