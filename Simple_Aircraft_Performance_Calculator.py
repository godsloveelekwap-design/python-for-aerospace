# aircraft_performance.py
# Simple Aircraft Performance Calculator

def thrust_to_weight_ratio(thrust, weight):
    return thrust / weight

def wing_loading(weight, wing_area):
    return weight / wing_area

# Example values (you can change these!)
thrust = 20000   # Newtons
weight = 18000   # Newtons
wing_area = 30   # square meters

print("Thrust-to-Weight Ratio:", thrust_to_weight_ratio(thrust, weight))
print("Wing Loading:", wing_loading(weight, wing_area), "N/m^2")
