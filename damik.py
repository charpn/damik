from ev3dev2.motor import OUTPUT_B, OUTPUT_C, MoveTank
from ev3dev2.sensor.lego import ColorSensor
from time import sleep

def follow_yellow_line():
    tank_drive = MoveTank(OUTPUT_B, OUTPUT_C)
    color_sensor = ColorSensor()

    try:
        while True:
            if color_sensor.color_name == 'Yellow':
                tank_drive.on(30, 30)  # İleri hareket
            else:
                tank_drive.on(-10, 10)  # Sola dönme
            sleep(0.1)
    except KeyboardInterrupt:
        tank_drive.off()  # Program durdurulduğunda motorları kapatın

if __name__ == '__main__':
    follow_yellow_line()
