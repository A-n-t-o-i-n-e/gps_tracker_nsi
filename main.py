# Ce code envoie un signal gps lorsque le capteur est dépalcé

from microbit import uart, button_a, button_b, accelerometer

# init gps
microbit.uart.init(baudrate=9600, bits=8, parity=None, stop=1, tx=None, rx=None)

while True:
    
    if button_b.is_pressed():
        pass
        
    elif button_a.was_pressed():
        if accelerometer.was_gesture('shake'):
            uart.read([8])
