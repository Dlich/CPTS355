def maxInt(L):
    return maxHelper(L,0)

def maxHelper(L,curMax):
    if (len(L) == 0):
        return curMax
    for item in L:
        if isinstance(item,list):
            curMax = maxHelper(item,curMax)
        else:
            curMax = max(item,curMax)
    return curMax



def max(a,b):
    if a>b: return a
    else: return b


#print(maxInt([1,[2,[3,4,5],2,5],[5,6,8,9,[10]],7]))
print(maxInt([1,[2,3]]))