# Define a procedure, add_to_index,
# that takes 3 inputs:

# - an index: [[<keyword>,[<url>,...]],...]
# - a keyword: String
# - a url: String

# If the keyword is already
# in the index, add the url
# to the list of urls associated
# with that keyword.

# If the keyword is not in the index,
# add an entry to the index: [keyword,[url]]

index = []

def in_index(index, keyword):
    ls = [x[0] for x in index]
    if keyword in ls:
        return ls.index(keyword)
    return -1

def add_to_index(index, keyword, url):
    i = in_index(index, keyword)
    if i < 0:
        index.append([keyword, [url]])
    else:
        index[i][1].append(url)
        
add_to_index(index,'udacity','http://udacity.com')
add_to_index(index,'computing','http://acm.org')
add_to_index(index,'udacity','http://npr.org')
print(index)
#>>> [['udacity', ['http://udacity.com', 'http://npr.org']], ['computing', ['http://acm.org']]]
