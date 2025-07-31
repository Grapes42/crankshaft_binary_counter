# Spur gear calculator

# Constants
pi = 3.14159

# Variables
N_g = 16 # No of teeth in gear
N_p = 8 # No of teeth in pinion

D_g = 40 # Pitch diameter of gear
D_p = 20 # Pitch diameter of pinion


# Diametral pitch
def calc_P(N, D):
    P = N / D
    return P

def calc_p(N, D):
    p = (pi * D) / N
    return p

def calc_a(P):
    a = 1 / P
    return a

def calc_b(P):
    d = 1.25 / P
    return d

def calc_t(P):
    t = 1.5708 / P
    return t

P = calc_P(N_g, D_g)
t = calc_t(P)

print(t)