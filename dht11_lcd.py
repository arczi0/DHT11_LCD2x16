import RPi.GPIO as GPIO
import dht11
import time
import datetime
import lcddriver


# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# read data using pin 14
instance = dht11.DHT11(pin=17)
display = lcddriver.lcd()


while True:
    result = instance.read()
    if result.is_valid():
        display.lcd_clear()
        print("Przesylanie do wyswietlacza: ")
        display.lcd_display_string("Temp. wew: ",1)
        display.lcd_display_string(str(result.temperature) + " C" ,2)
        time.sleep(5)
        display.lcd_display_string("Wilgotnosc: ",1)
        display.lcd_display_string(str(result.humidity) + " %",2)
        time.sleep(5)
        display.lcd_clear()
        display.lcd_display_string(str(datetime.datetime.now()), 2)
        time.sleep(5)


