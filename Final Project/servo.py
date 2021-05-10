import RPi.GPIO as GPIO
import time

DUTY = 0.5
MIN_DUTY=2.5+DUTY
MAX_DUTY=12.5+DUTY


def setup():
    global P
    mode = GPIO.getmode()
    print("Current mode: " + str(mode))
    if mode == GPIO.BCM:
        servo = 18
        GPIO.setup(servo,GPIO.OUT)
        GPIO.output(servo,GPIO.LOW)
    else:
        servo = 12
        GPIO.setmode(GPIO.BOARD)        
        GPIO.setup(servo,GPIO.OUT)
        GPIO.output(servo,GPIO.LOW)

    P = GPIO.PWM(servo,50)
    P.start(0)

def map( value, fromLow, fromHigh, toLow, toHigh):
    return (toHigh-toLow)*(value-fromLow) / (fromHigh-fromLow) + toLow

def servoWrite(a):  # make the servo rotate to specific angle (0-180 degrees) 
    if(a<0):
        a=0
    elif(a>180):
        a=180
    P.ChangeDutyCycle(map(a,0,180,MIN_DUTY,MAX_DUTY))   #map the angle to duty cycle and output it

def loop():
    while True:
        for i in range(0,181,1):
            servoWrite(i)
            time.sleep(0.01)
        time.sleep(0.5)
        for i in range (180,-1,-1):
            servoWrite(i)
            time.sleep(0.01)
        time.sleep(0.5)

def oneturn():
    P.start(0)
    print("Turn left ...")
    for i in range(0,181,1):
        servoWrite(i)
        time.sleep(0.01)
    time.sleep(0.5)
    
    print("Turn right ...")
    for i in range (180,-1,-1):
        servoWrite(i)
        time.sleep(0.01)
    time.sleep(0.5)
    P.stop()

def destroy():
    P.stop()
    GPIO.cleanup()

if __name__ == '__main__':     #Program start from here
    print("starting...")
    setup()
    oneturn()
    destroy()
    #try:
    #    loop()
    #except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
    #        destroy()
