import machine
import mpu6050
import utime

def calibrate_gyro(accel, calibration_round=2000):
    offsets = {"x":0,"y":0,"z":0}
    gyro_read = accel.get_values()
    for i in range(calibration_round):
        offsets["x"] += gyro_read["GyX"]
        offsets["y"] += gyro_read["GyY"]
        offsets["z"] += gyro_read["GyZ"]
    offsets["x"]/=calibration_round
    offsets["y"]/=calibration_round
    offsets["z"]/=calibration_round
    return offsets

def update_gyro(last_time, accel, offsets, pitch=0,roll=0,yaw=0):
    current_time = utime.ticks_ms()
    loop_time = current_time-last_time
    hertz = 1000/loop_time
#    hertz = 1
    gyro_read = accel.get_values()
    x_out = (gyro_read["GyX"]-offsets["x"]) / 65.5 / hertz
    y_out = (gyro_read["GyY"]-offsets["y"]) / 65.5 / hertz
    z_out = (gyro_read["GyZ"]-offsets["z"]) / 65.5 / hertz
    pitch+=y_out
    roll+=x_out
    yaw+=z_out

    return current_time, pitch, roll, yaw
#What to do:
#Calibrate Gyro
