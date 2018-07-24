import math

def areas(radius):
    jibu = 1/2*math.pi*math.pow(radius,2)
    print("The Area of your Circle is",jibu )
    return

print("Enter The Radius")
radius = float(input())
areas(radius)