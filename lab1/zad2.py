import random
import math

target = random.randint(50,341)
v=22
h=0
g=9.81 
#angle = int(input("podaj kat strzalu"))

def calculate_hit(target, angle):
    distance = (v * math.sin(angle) + math.sqrt((v**2)*math.sin(angle)**2+2*g*h))*(v*math.cos(angle)/g)
    if target-5 <= distance <= target+5:
        print("hit", distance, target)
        return True
    else:
        print("pudlo", distance, target)
        return False

while True:
    if calculate_hit(random.randint(50,341), math.radians(35)) == True:
        break