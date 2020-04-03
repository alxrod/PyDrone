import machine 
import mpu6050 
from imu import calibrate_gyro, update_gyro
import utime
import sys

i2c = machine.I2C(scl=machine.Pin(5), sda=machine.Pin(4))
accelerometer = mpu6050.accel(i2c)

print("Calibrating accelerometer...")
utime.sleep(1)
pin = machine.Pin(2, machine.Pin.OUT)
pin.off()
offsets = calibrate_gyro(accelerometer)
pin.on()

print("Starting Loop:")
current_time = utime.ticks_ms()
utime.sleep_ms(4)
last_time, pitch, roll, yaw = update_gyro(current_time, accelerometer, offsets)
count = 0
while True:
    last_time, pitch, roll, yaw = update_gyro(last_time, accelerometer, offsets, pitch, roll, yaw)
    count+=1
    if count == 25:
        count = 0
        sys.stdout.write("\rRoll: " + str(roll) + " Pitch: " + str(pitch) + " Yaw: " + str(yaw))        
#pwm_pin = machine.Pin(12, machine.Pin.OUT)
#motor = machine.PWM(pwm_pin,freq=50)
#motor.duty(50)
#pin.off()


