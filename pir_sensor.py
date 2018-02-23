from gpiozero import MotionSensor
furrukh = MotionSensor(14)
while True:
    if furrukh.motion_detected:
        print('zafeer ny ungli krdi')
        
