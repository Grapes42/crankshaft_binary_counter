import math

def calc_b(a, n): # Center distance
    b=a/math.sin(180/n)
    return b

a = 20 # Crank radius
n = 4 # No of slots

b = calc_b(a, n)
print(b)
