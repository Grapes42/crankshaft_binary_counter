# Crankshaft Binary Counter

## Spur gear calculations

Using simple python code I created functions to simplify solving variables for spur gears, based on the equations found [here](https://www.engineersedge.com/gear_formula.htm)
```py
# N = no of teeth
# D = Pitch diameter

def calc_P(N, D): # Calculate diametral pitch
    P = N / D
    return P

def calc_p(N, D): # Calculate circular pitch
    p = (pi * D) / N
    return p

def calc_a(P): # Calculate addendum
    a = 1 / P
    return a

def calc_b(P): # Calculate dedendum
    d = 1.25 / P
    return d

def calc_t(P): # Calculate thickness at pitch line
    t = 1.5708 / P
    return t
```
For the sake of my gears I found:
- Diametral Pitch: 0.4
- Circular Pitch: 7.854
- Addendum: 2.5
- Dedendum: 3.125
- Thickness: 3.927