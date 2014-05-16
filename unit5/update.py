# Define a procedure,

# hashtable_update(htable,key,value)

# that updates the value associated with key. If key is already in the
# table, change the value to the new value. Otherwise, add a new entry
# for the key and value.

# Hint: Use hashtable_lookup as a starting point.
# Make sure that you return the new htable

def hashtable_update(htable, key, value):
    if hashtable_lookup2(htable, key):
        bucket = hashtable_get_bucket(htable, key)
        for entry in bucket:
            if entry[0] == key:
                entry[1] = value
                break
    else:
        hashtable_add(htable, key, value)
        
    return htable

# def hashtable_lookup(htable, key):
#     bucket = hashtable_get_bucket(htable, key)
#     for entry in bucket:
#         if entry[0] == key:
#             return entry[1]
#     return None

def hashtable_lookup2(htable, key):
    return next((e[1] for e in hashtable_get_bucket(htable, key) if key == e[0]), None)

def hashtable_add(htable, key, value):
    bucket = hashtable_get_bucket(htable, key)
    bucket.append([key, value])

def hashtable_get_bucket(htable, keyword):
    return htable[hash_string2(keyword, len(htable))]

# def hash_string(keyword, buckets):
#     out = 0
#     for s in keyword:
#         out = (out + ord(s)) % buckets
#     return out

def hash_string2(keyword, buckets):    
    return sum(map(lambda x: ord(x), keyword)) % buckets

def make_hashtable(nbuckets):
    table = []
    for unused in range(0, nbuckets):
        table.append([])
    return table

table = [[['Ellis', 11], ['Francis', 13]], [], [['Bill', 17], ['Zoe', 14]], [['Coach', 4]], [['Louis', 29], ['Nick', 2], ['Rochelle', 4]]]

hashtable_update(table, 'Bill', 42)
hashtable_update(table, 'Rochelle', 94)
hashtable_update(table, 'Zed', 68)
print(table)
#>>> [[['Ellis', 11], ['Francis', 13]], [['Zed', 68]], [['Bill', 42], ['Zoe', 14]], [['Coach', 4]], [['Louis', 29], ['Nick', 2], ['Rochelle', 94]]]