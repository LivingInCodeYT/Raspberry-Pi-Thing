import RPi.GPIO as GPIO

# setup pin for input
GPIO.setmode(GPIO.BOARD)

GPIO.setup(2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:
    while 1:
        if (GPIO.input(2) == 1):
            print("it works lmao")
except KeyboardInterrupt:
    GPIO.cleanup()
    import poll