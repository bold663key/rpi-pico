# DS18B20 with OLED SH1106

Build a simple weather station using RPI Pico, OLED SH1106 and DS18B20 sensor.


# For this project you need this:
## Software:
sh1106.py - Driver for the SH1106 display

https://github.com/robert-hh/SH1106

ds18x20.py - Driver for your temperature sensor

https://github.com/micropython/micropython-infineon/blob/master/drivers/onewire/ds18x20.py

onewire.py - Next driver for your ds18x20 sensor

https://github.com/micropython/micropython-infineon/blob/master/drivers/onewire/onewire.py

## Hardware:

1x Oled display SH1106

1x 4,7 kΩ resistor

1x DS18B20 temperature sensor

and of course Raspberry Pi Pico ;-)

# Let's do this !

First you must connect all. Check image how to do this.
![Schemat](https://github.com/bold663key/rpi-pico/blob/main/micropython/ds18b20_oled/ds18b20_oled.png)

Download all drivers and libraries. Save them into rpi pico.

Use my `ds18b20_oled.py` code. Now you can run it ! 

You should see thermometer picture, inscription and temperature. 

## Authors

- [@bold663key](https://www.github.com/bold663key)


## License

[MIT](https://choosealicense.com/licenses/mit/)
