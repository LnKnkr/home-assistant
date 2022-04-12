import math
import matplotlib.pyplot as plt


class Location:
    def __init__(self, x_pos, y_pos, z_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.z_pos = z_pos

    def distance_with(self, point):
        a = (point.x_pos - self.x_pos) ** 2
        b = (point.y_pos - self.y_pos) ** 2
        c = (point.z_pos - self.z_pos) ** 2
        return math.sqrt(a + b + c)


class Sensor:
    sensor_range = 4

    def __init__(self, x_pos, y_pos, z_pos):
        self.position = Location(x_pos, y_pos, z_pos)

    def within_range(self):
        pass


class Room:
    """Class which represents a Room with all sensors and Control-Units"""

    def __init__(self, sensors, length, width, height):
        self.sensors = sensors
        self.length = length
        self.width = width
        self.height = height


def main():
    x = Location(3, 3, 3)
    y = Location(5, 5, 5)
    print(x.distance_with(y))


main()
