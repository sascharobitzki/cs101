# Define a procedure, lookup,
# that takes two inputs:

# - an index
# - keyword

# The procedure should return a list
# of the urls associated
# with the keyword. If the keyword
# is not in the index, the procedure
# should return an empty list.

index = [['udacity', ['http://udacity.com', 'http://npr.org']],
         ['computing', ['http://acm.org']]]

def lookup(index, keyword):    
    return [k for u in index if u[0] is keyword for k in u[1]]

print(lookup(index,'udacity'))
#>>> ['http://udacity.com','http://npr.org']
