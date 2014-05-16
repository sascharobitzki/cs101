# A list is symmetric if the first row is the same as the first column,
# the second row is the same as the second column and so on. Write a
# procedure, symmetric, which takes a list as input, and returns the
# boolean True if the list is symmetric and False if it is not.

def symmetric(l, r=1):
    if len(l) > 0 and len(l) != len(l[0]): return False
    c = [[] for unused in range(len(l))]
    [[c[j].append(l[i][j]) for j in range(len(l[i]))] for i in range(len(l))]
    return False if 0 in [r*0 if l[i] != c[i] else r*1 for i in range(len(l))] else True

print(symmetric([]))
#>>> True
print(symmetric([[1, 2, 3],
                 [2, 3, 4],
                 [3, 4, 1]]))
#>>> True
print(symmetric([["cat", "dog", "fish"],
                ["dog", "dog", "fish"],
                ["fish", "fish", "cat"]]))
#>>> True
print(symmetric([["cat", "dog", "fish"],
                ["dog", "dog", "dog"],
                ["fish","fish","cat"]]))
#>>> False
print(symmetric([[1, 2],
                [2, 1]]))
#>>> True
print(symmetric([[1, 2, 3, 4],
                [2, 3, 4, 5],
                [3, 4, 5, 6]]))
#>>> False
print(symmetric([[1,2,3],
                 [2,3,1]]))
#>>> False