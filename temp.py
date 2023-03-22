# Teste para impressora Dematech MP-4200

from serial import Serial

ser  = Serial('/dev/tty.usbmodem141401', 19200, timeout=1)

ser.write(b"Katia:\nVoce e o Amor...\nDa minha vida :)\n----\n----\n----\n----\n")
ser.close()