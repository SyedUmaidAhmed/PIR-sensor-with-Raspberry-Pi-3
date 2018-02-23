from gpiozero import MotionSensor
pir = MotionSensor(14)
while True:
    if pir.motion_detected:
        print('Intruder is here')
        
