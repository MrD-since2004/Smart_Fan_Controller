# sensor.py
import random

def get_temperature():
    """
    Simulates reading a temperature from a sensor.
    Instead of a real sensor, it returns a random value between 20°C and 40°C.
    """
    return random.randint(20, 40)
