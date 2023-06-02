# OLED display SH1106 with temperature sensor DS18B20
from machine import I2C
from time import sleep
from sh1106 import SH1106_I2C
import onewire, ds18x20
import framebuf

ds18x20_pin = machine.Pin(2)
ds18x20_sensor = ds18x20.DS18X20(onewire.OneWire(ds18x20_pin)) # Utworzenie klasy ds18x20_sensor
roms = ds18x20_sensor.scan() # Skanowanie urządzenia ds18b20

WIDTH  = 128    # Szerokość wyświetlacza                                   
HEIGHT = 64     # Wysokość wyświetlacza                                       

i2c = I2C(0)    # Wybranie pinu I2C                                        
print("Konfiguracja i adres I2C : "+ " " + str(i2c)+hex(i2c.scan()[0]).upper() ) # Konfiguracja i adres urządzenia

oled = SH1106_I2C(WIDTH, HEIGHT, i2c) # Określenie oled                 
oled.rotate(True) # Obrócenie ekranu o 180 stopni

# Obrazek termometru
temp = bytearray(b'\x07\xe0\x0f\xf0\x1f\xf8\x1f\xf8\x1f\xf8\x00\xf8\x00\xf8\x1f\xf8\x1f\xf8\x00\xf8\x00\xf8\x1f\xf8\x1f\xf8\x1f\xf8\x1f\xf8\x1c8\x1c8\x1c8\x1c8\x1c8\x1c8<<|>x\x1e\xf0\x0f\xe0\x0f\xe0\x0f\xf0\x0fx\x1e\x7f\xfe?\xfc\x07\xe0') 
fb = framebuf.FrameBuffer(temp,16,32, framebuf.MONO_HLSB)

oled.fill(0) # Wyzerowanie ekranu przed wyświetleniem danych

#oled.contrast(255) Możliwa zmiana jasności ekranu

while True:
  ds18x20_sensor.convert_temp() # Uzyskanie temperatury w celu konwersji jednostek temperatury
  for rom in roms:  # rom - adres urządzenia
    text = ds18x20_sensor.read_temp(rom) # Zwrócenie wartości temperatury urządzenia i przypisanie jej to text 
    oled.text("Temperatura",0,0) # Wyświetlenie nagłówka "Temperatura"
    oled.text(str(text),20,30) # Wyświetlenie temperatury jako konwersji liczby zmiennoprzecinkowej na łańcuch znaków
    oled.blit(fb,100,20) #Wyświetlenie Termometru
    oled.show() # Pokazanie wszystkiego na ekranie
    sleep(1) # Zatrzymanie wyświetlania na 1 sekundę
    oled.fill(0) # Wyzerowanie ekranu i ponowne rozpoczęcie pętli
