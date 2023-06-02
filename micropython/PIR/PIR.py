from machine import Pin
from picozero import LED, Speaker
from time import sleep
 
pir = Pin(22, Pin.IN, Pin.PULL_DOWN)
led = LED(15)
speaker = Speaker(5)
n = 0
 
print('Włączam moduł PIR')
sleep(1)
print('Gotowy')
 
while True:
     if pir.value() == 1:
          n = n+1
          print('WYKRYTO RUCH ',n)
          led.on()
          speaker.play(262, 0.1) # 262 = note C4, 0.1 seconds
          sleep(0.1)
          speaker.play(262, 0.1) # 262 = note C4, 0.1 seconds
     sleep(1)
     led.off()