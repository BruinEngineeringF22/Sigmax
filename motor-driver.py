import RPi.GPIO as GPIO
from time import sleep

# h-bridge #1
in1 = 23
in2 = 24
in3 = 27
in4 = 17

en_a = 25
en_b = 16

# h-bridge #2
in5 = 26
in6 = 13
in7 = 6
in8 = 5

en_c = 11
en_d = 9

temp1=1

GPIO.setmode(GPIO.BCM)

# For h-bridge 1
#########################
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)

GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)

GPIO.setup(en_a,GPIO.OUT)
GPIO.setup(en_b, GPIO.OUT)

# For h-bridge 2
##############################
GPIO.setup(in5,GPIO.OUT)
GPIO.setup(in6,GPIO.OUT)
GPIO.setup(in7,GPIO.OUT)
GPIO.setup(in8,GPIO.OUT)

GPIO.output(in5,GPIO.LOW)
GPIO.output(in6,GPIO.LOW)
GPIO.output(in7,GPIO.LOW)
GPIO.output(in8,GPIO.LOW)

GPIO.setup(en_c, GPIO.OUT)
GPIO.setup(en_d, GPIO.OUT)
#############################

#p1 / p2 == in1 - in4
#p3 / p4 == in5 - in8
#############################
p1=GPIO.PWM(en_a,1000)
p2=GPIO.PWM(en_b,1000)
p3=GPIO.PWM(en_c, 1000)
p4=GPIO.PWM(en_d,1000)

#start p1-p4
p1.start(50)
p2.start(50)
p3.start(50)
p4.start(50)

def adjustSpeed(increaseOrDecrease, currentSpeed):
    
    speedToChange = 0
    
    if(increaseOrDecrease == 'increase'):
        speedToChange = currentSpeed + 50
        print("Speed to " + increaseOrDecrease + ': ' + str(speedToChange))
    elif(increaseOrDecrease == 'decrease'):
        speedToChange = currentSpeed - 50
        print("Speed to " + increaseOrDecrease + ': ' + str(speedToChange))

    currentSpeed = speedToChange
    p1.ChangeDutyCycle(speedToChange)
    p2.ChangeDutyCycle(speedToChange)
    p3.ChangeDutyCycle(speedToChange)
    p4.ChangeDutyCycle(speedToChange)

    return currentSpeed

def resetToCurrentSpeed(currentSpeed):
    p1.ChangeDutyCycle(currentSpeed)
    p2.ChangeDutyCycle(currentSpeed)
    p3.ChangeDutyCycle(currentSpeed)
    p4.ChangeDutyCycle(currentSpeed)
    
def main():
    # current speed of motor
    currentSpeed = 50
    
    while(1):
        x = input("Enter a commmand: ")
        
        if(x=='f'):
            print("Moving forward")
            GPIO.output(in1,GPIO.HIGH)
            GPIO.output(in2,GPIO.LOW)
            GPIO.output(in3,GPIO.HIGH)
            GPIO.output(in4,GPIO.LOW)
                         
            # second h-bridge
            GPIO.output(in5,GPIO.HIGH)
            GPIO.output(in6,GPIO.LOW)
            GPIO.output(in7,GPIO.HIGH)
            GPIO.output(in8,GPIO.LOW)
            
            print("forward")
        elif(x=='b'):
            #first h-bridge
            GPIO.output(in1,GPIO.LOW)
            GPIO.output(in2,GPIO.HIGH)
            GPIO.output(in3,GPIO.LOW)
            GPIO.output(in4,GPIO.HIGH)
            
            # second h-bridge
            GPIO.output(in5,GPIO.LOW)
            GPIO.output(in6,GPIO.HIGH)
            GPIO.output(in7,GPIO.LOW)
            GPIO.output(in8,GPIO.HIGH)
            print("backward")
        elif(x=='r'):    # turn right
            print("Turning right")
            p1.ChangeDutyCycle(40);
            p2.ChangeDutyCycle(40);
            p3.ChangeDutyCycle(40);
            p4.ChangeDutyCycle(40);
            # front right wheel
            GPIO.output(in1,GPIO.HIGH)
            GPIO.output(in2,GPIO.HIGH)
            # front left wheel
            GPIO.output(in3,GPIO.LOW)
            GPIO.output(in4,GPIO.LOW)
            
            # back right wheel
            GPIO.output(in5,GPIO.HIGH)
            GPIO.output(in6,GPIO.HIGH)
            # back left wheel
            GPIO.output(in7,GPIO.LOW)
            GPIO.output(in8,GPIO.LOW)
            
            resetToCurrentSpeed(currentSpeed)
        elif(x=='l'):
            print("Turning left")
            p1.ChangeDutyCycle(40);
            p2.ChangeDutyCycle(40);
            p3.ChangeDutyCycle(40);
            p4.ChangeDutyCycle(40);
            # front right wheel
            GPIO.output(in1,GPIO.LOW)
            GPIO.output(in2,GPIO.LOW)
            # front left wheel
            GPIO.output(in3,GPIO.HIGH)
            GPIO.output(in4,GPIO.HIGH)
            
            # back right wheel
            GPIO.output(in5,GPIO.LOW)
            GPIO.output(in6,GPIO.LOW)
            # back left wheel
            GPIO.output(in7,GPIO.HIGH)
            GPIO.output(in8,GPIO.HIGH)
            
            resetToCurrentSpeed(currentSpeed)     
            
        elif(x == 'i'):
            returnedCurrentSpeed = adjustSpeed('increase', currentSpeed)
            currentSpeed = returnedCurrentSpeed
            print("-- Current speed in increase speed : " + str(currentSpeed))
            x='z'
        elif(x=='d'):
            returnedCurrentSpeed = adjustSpeed('decrease', currentSpeed)
            currentSpeed = returnedCurrentSpeed
            print("-- Current speed in decrease speed : " + str(currentSpeed))
        elif(x=='s'):
            print("stop")
            GPIO.output(in1,GPIO.LOW)
            GPIO.output(in2,GPIO.LOW)
            GPIO.output(in3,GPIO.LOW)
            GPIO.output(in4,GPIO.LOW)
        elif(x=='e'):
            print("Cleaning up pins")
            GPIO.cleanup()
            break
        
        else:
            print("Incorrect input. Please try again")

if __name__ == "__main__":
    main()

