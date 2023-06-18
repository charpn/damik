from ev3dev2.motor import OUTPUT_A, OUTPUT_B, MoveTank
from ev3dev2.sensor.lego import ColorSensor
from time import sleep

# Renk sensörünü tanımla
color_sensor = ColorSensor()

# Motorları tanımla
tank = MoveTank(OUTPUT_A, OUTPUT_B)

# Hızları ayarla
SPEED = 30
TANK_TURN_SPEED = 10

# Çizgi izleme fonksiyonu
def follow_line():
    while True:
        # Renk sensöründen mevcut renk değerini al
        color = color_sensor.color

        # Sarı çizgiyi takip etmek için
        if color == ColorSensor.COLOR_YELLOW:
            tank.on(SPEED, SPEED)
        # Beyaz yüzeye ulaşıldığında dur
        elif color == ColorSensor.COLOR_WHITE:
            tank.off()
        # Başka bir renge rastlandığında dön
        else:
            tank.on(TANK_TURN_SPEED, -TANK_TURN_SPEED)

        # Çizgi izleme aralığı için biraz bekle
        sleep(0.1)

# Çizgi izleme işlevini çağır
follow_line()

from ev3dev2.motor import OUTPUT_A, OUTPUT_B, MoveTank
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.button import Button

# Motorları tanımla
tank = MoveTank(OUTPUT_A, OUTPUT_B)

# Dokunma sensörlerini tanımla
touch_sensor1 = TouchSensor('in1')
touch_sensor2 = TouchSensor('in2')

# Hızı ve dönüş hızını ayarla
SPEED = 30
TURN_SPEED = 20

# Ana döngü
while True:
    # İlk dokunma sensörüne basılı tutuluyorsa sağa dön
    if touch_sensor1.is_pressed:
        tank.on(TURN_SPEED, -TURN_SPEED)
    # İkinci dokunma sensörüne basılı tutuluyorsa sola dön
    elif touch_sensor2.is_pressed:
        tank.on(-TURN_SPEED, TURN_SPEED)
    # Her iki dokunma sensörüne birden basılı tutuluyorsa düz git
    elif touch_sensor1.is_pressed and touch_sensor2.is_pressed:
        tank.on(SPEED, SPEED)
    # Hiçbir dokunma sensörüne basılmamışsa dur
    else:
        tank.off()

    # Programı sonlandırmak için orta tuşa basıldığında döngüyü kır
    if Button().middle:
        break

