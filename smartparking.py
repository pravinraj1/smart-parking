from gpiozero import DistanceSensor
from time import sleep

# Define GPIO pin numbers for trigger and echo pins
GPIO_TRIGGER1 = 17
GPIO_ECHO1 = 18
GPIO_TRIGGER2 = 23
GPIO_ECHO2 = 24

sensor1 = DistanceSensor(trigger=GPIO_TRIGGER1, echo=GPIO_ECHO1)
sensor2 = DistanceSensor(trigger=GPIO_TRIGGER2, echo=GPIO_ECHO2)
# Add more sensors if needed

def check_parking_spaces(distance1, distance2):
    # You can define your parking space logic here
    # For example, check if a car is within a certain distance threshold
    if distance1 < 0.2:
        print("Parking Space 1 is occupied")
    else:
        print("Parking Space 1 is available")

    if distance2 < 0.2:
        print("Parking Space 2 is occupied")
    else:
        print("Parking Space 2 is available")

while True:
    distance1 = sensor1.distance
    distance2 = sensor2.distance
    # Read distances from more sensors if needed

    # Process distance data and manage parking spaces here
    check_parking_spaces(distance1, distance2)

    sleep(1)  # Delay for better readability

