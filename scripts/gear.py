# Constants
PI = 3.14159
DP = 3 # no of decimal places

class Gear:
    def __init__(self, name, P=0, p=0, d=0, a=0, b=0, t=0, n=0):
        self.name = name
        self.P = P # Diametral Pitch
        self.p = p # Circular Pitch
        self.d = d # Pitch Diameter
        self.a = a # Addentum
        self.b = b # Dedentum
        self.t = t # Tooth Thickness
        self.n = n # No of teeth
    
    def __str__(self):
        string = f"""{self.name}:
    Diametral Pitch: {self.P}
    Circular Pitch: {self.p}
    Pitch Diameter: {self.d}
    Addentum: {self.a}
    Dedentum: {self.b}
    Tooth thickness: {self.t}
    No of teeth: {self.n}"""
        
        return string

    # Diametral pitch
    def calc_P(self):
        P = self.n / self.d
        self.P = round(P, DP)
    
    # Circular Pitch
    def calc_p(self):
        p = (PI * self.d) / self.n
        self.p = round(p, DP)

    # Addentum
    def calc_a(self):
        a = 1 / self.P
        self.a = round(a, DP)

    # Dedentum
    def calc_b(self):
        b = 1.25 / self.P
        self.b = round(b, DP)

    # Tooth Thickness
    def calc_t(self):
        t = 1.5708 / self.P
        self.t = round(t, 3)