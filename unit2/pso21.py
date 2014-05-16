# By Sam the Great from forums
# That freaking superhero has been frequenting Udacity
# as his favorite boss battle fight stage. The 'Udacity'
# banner keeps breaking, and money is being wasted on
# repairs. This time, we need you to proceduralize the
# fixing process by building a machine to automatically
# search through debris and return the 'Udacity' banner
# to the company, and be able to similarly fix other goods.

# Write a Python procedure fix_machine to take 2 string inputs
# and returns the 2nd input string as the output if all of its
# characters can be found in the 1st input string and "Give me
# something that's not useless next time." if it's impossible.

# NOTE: # If you are experiencing difficulties taking
#         this problem seriously, please refer back to
#         "Superhero flyby", the prequel, in Problem Set 11.

# TOOLS: # if statement
#          while loop
#          string operations
#          Unit 1 Basics

# BONUS: # 
# 5***** #  If you've graduated from CS101,
#  Gold  #  try solving this in one line.
# Stars! #

def fix_machine_obsolete(debris, product):
    #return("Give me something that's not useless next time." if 0 in list(0 if e not in debris else 1 for e in product) else product)
    return (product if not list(char for char in product if char not in debris) else "Give me something that is not useless next time.")

def fix_machine(debris, product):
    d = list(debris)
    return ("Give me something that's not useless next time." if None in [None if e not in d else d.pop(d.index(e)) for e in product] else product)

def fix_machine_mh(debris, product):
    return ("Give me something that's not useless next time." if any(debris.count(c) < product.count(c) for c in product) else product)

### TEST CASES ###
print("Test case 1: ", fix_machine('UdaciousUdacitee', 'Udacity') == "Give me something that's not useless next time.")
print("Test case 2: ", fix_machine('buy me dat Unicorn', 'Udacity') == 'Udacity')
print("Test case 3: ", fix_machine('AEIOU and sometimes y... c', 'Udacity') == 'Udacity')
print("Test case 4: ", fix_machine('wsx0-=mttrhix', 't-shirt') == 't-shirt')
print("Test case 5: ", (fix_machine(' bedgih,onpsrut', 'oops, not enough debris') == "Give me something that's not useless next time."))