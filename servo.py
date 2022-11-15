import RPi.GPIO as GPIO
from time import sleep

def setAngle(p, servoPin, angle):
    print("servo pin: ", servoPin)
    print("p: ", p)
    duty = angle / 18 / 2 - 2.5
    GPIO.output(servoPin, True)
    p.ChangeDutyCycle(duty)
    sleep(1.5)
    GPIO.output(servoPin, False)
    p.ChangeDutyCycle(0)

# initializing pwm pins
servoPin1 = 12
servoPin2 = 16
servoPin3 = 20

################################
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPin1, GPIO.OUT)
GPIO.setup(servoPin2,GPIO.OUT)
GPIO.setup(servoPin3,GPIO.OUT)
################################

# initializing frequency of pwm pins
p1 = GPIO.PWM(servoPin1, 50)
p2 = GPIO.PWM(servoPin2, 50)
p3 = GPIO.PWM(servoPin3, 50)

# setting start position of servo
p1.start(0)     #initialize
p2.start(0)     #initialize
p3.start(0)     #initialize

try:
#     while True:
#         p.ChangeDutyCycle(5)
#         sleep(0.5)
#         p.ChangeDutyCycle(7.5)
#         sleep(0.5)
#         p.ChangeDutyCycle(10)
#         sleep(0.5)
#         p.ChangeDutyCycle(12.5)
#         sleep(0.5)
#         p.ChangeDutyCycle(0)
#         p.ChangeDutyCycle(22)
#         sleep(0.5)
    
        
    itemSelector=input("Enter a commmand: ")
    
    if(itemSelector == '1'):
        setAngle(p1, servoPin1, 180)
 
    if(itemSelector =='2'):
        setAngle(p2, servoPin2, 180)
 
    if(itemSelector =='3'):
        setAngle(p3, servoPin3, 180)
        
        
    ######
#     setAngle(p1, servoPin1, 180)
#     setAngle(p2, servoPin2, 180)
#     setAngle(p3, servoPin3, 180)
######
    


    
except KeyboardInterrupt:
    p1.stop()
    p2.stop()
    p3.stop()
    GPIO.cleanup()