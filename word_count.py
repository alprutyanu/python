def word_count(arr):
    """Counts frequency of words in an array
    Returns map"""
    map = {}
    for i in arr:
        map.setdefault(i, 0)
        map[i] += 1
    return map

arr1 = ['a','s','d','r','w','s','a']
print word_count(arr1)