# Write a procedure, speed_fraction, which takes as its inputs the result of
# a traceroute (in ms) and distance (in km) between two points. It should 
# return the speed the data travels as a decimal fraction of the speed of
# light.

"""km per ms"""
speed_of_light = 300000./1000.

def speed_fraction(latency, distance):
    time = latency/2.
    speed = distance/time
    return speed/speed_of_light

print(speed_fraction(50, 5000))
#>>> 0.666666666667

print(speed_fraction(50, 10000))
#>>> 1.33333333333  # Any thoughts about this answer, or these inputs?