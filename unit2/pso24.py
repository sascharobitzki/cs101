# By AnnaGajdova from forums
# You are in the middle of a jungle. 
# Suddenly you see an animal coming to you. 
# Here is what you should do if the animal is:

# zebra >> "Try to ride a zebra!"
# cheetah >> If you are faster than a cheetah: "Run!" 
#            If you are not: "Stay calm and wait!". 
#            The speed of a cheetah is 115 km/h.
# anything else >> "Introduce yourself!"

# Define a procedure, jungle_animal, 
# that takes as input a string and a number, 
# an animal and your speed (in km/h), 
# and prints out what to do.

def jungle_animal(animal, my_speed):
    d = {'zebra': ["Try to ride a zebra!"], 'cheetah': ["Run!", "Stay calm and wait!"], 'anything else': ["Introduce yourself!"]}
    print((d[animal][0] if my_speed > 115 else d[animal][len(d[animal])-1]) if animal in d else d['anything else'][0])

jungle_animal('cheetah', 30)
#>>> "Stay calm and wait!"
jungle_animal('gorilla', 21)
#>>> "Introduce yourself!"
jungle_animal('zebra', 4)
jungle_animal('zebra', 68)
jungle_animal('cheetah', 197)