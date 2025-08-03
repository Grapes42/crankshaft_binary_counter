from gear import Gear

print("0 is undefined")

# P and p require n and d
# a, b and t require P

gear = Gear("Gear", d=28.28, n=12)
gear.calc_P()
gear.calc_a()
gear.calc_b()
gear.calc_t()

print(gear)