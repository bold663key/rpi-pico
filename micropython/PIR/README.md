
# HC-SR501 PIR Sensor with LED and buzzer

Build a motion detector that will illuminate the LED and turn on the buzzer.


# For this project you need this:
## Software:
picozero.py - A beginner-friendly library to help you use common electronics components with the Raspberry Pi Pico. 
https://github.com/RaspberryPiFoundation/picozero/blob/master/picozero/picozero.py

## Hardware:
1x LED diode

1x 220 Ω resistor

1x Buzzer

1x HC-SR501 PIR Sensor

and of course Raspberry Pi Pico ;-)

# Let's do this !

First you must connect all. Check image how to do this.
![Schemat](https://github.com/bold663key/rpi-pico/blob/main/micropython/ds18b20%20and%20LED/web_server_LED_ds18b20.png)

Download all drivers and libraries. Save them into rpi pico.

Use my `main.py` code. Change WIFI ssid and password. Now you can run it ! 

You should see blinking onboard led. It means that your rpi pico w try connect to internet. 

And the last signal is blink your LED diode on GPIO13. It means that your rpi pico successfully connected and now you can see rpi IP address. Copy it and paste in your web browser. 

It's that moment ! You see your website ! 

Click buttons and check that your LED diode is ON or OFF. 

Refresh website to see actual temperature from your DS18B20 sensor.
## Authors

- [@bold663key](https://www.github.com/bold663key)


## License

[MIT](https://choosealicense.com/licenses/mit/)

