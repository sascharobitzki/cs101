# Define a procedure, add_page_to_index,
# that takes three inputs:

#   - index
#   - url (String)
#   - content (String)

# It should update the index to include
# all of the word occurences found in the
# page content by adding the url to the
# word's associated url list.

index = []
    
def in_index(index, keyword):
    ls = [x[0] for x in index]
    if keyword in ls:
        return ls.index(keyword)
    return -1

def add_to_index2(index, keyword, url):
    i = in_index(index, keyword)
    if i < 0:
        index.append([keyword, [url]])
    else:
        index[i][1].append(url)
        
def add_to_index(index, keyword, url):
    for entry in index:
        if entry[0] == keyword:
            entry[1].append(url)
            return
    index.append([keyword, [url]])

def add_page_to_index(index, url, content):
    for e in content.split():
        add_to_index2(index, e, url)

add_page_to_index(index,'fake.text',"This is a test")
print(index)
#>>> [['This', ['fake.text']], ['is', ['fake.text']], ['a', ['fake.text']], ['test',['fake.text']]]
