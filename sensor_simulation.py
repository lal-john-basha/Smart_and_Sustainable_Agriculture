import random

def read_sensor():
    soil = random.randint(20,80)
    temperature = random.randint(20,40)
    humidity = random.randint(40,90)

    return soil, temperature, humidity