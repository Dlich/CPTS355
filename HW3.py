def main():
    d2 = {'Amazon':{'Mon':30,'Wed':100,'Sat':200},'Etsy':{'Mon':50,'Tue':20,'Wed':25,'Fri':30},'Ebay':{'Tue':60,'Wed':100,'Thu':30},'Shopify':{'Tue':100,'Thu':50,'Sat':20}}
    d3 = [{'Amazon':{'Mon':30,'Wed':100,'Sat':200},'Etsy':{'Mon':50,'Tue':20,'Wed':25,'Fri':30},'Ebay':{'Tue':60,'Wed':100,'Thu':30},'Shopify':{'Tue':100,'Thu':50,'Sat':20}},{'Shopify':{'Mon':25},'Etsy':{'Thu':40, 'Fri':50},'Ebay':{'Mon':100,'Sat':30}},{'Amazon':{'Sun':88},'Etsy':{'Fri':55},'Ebay':{'Mon':40},'Shopify':{'Sat':35}}]
    userTestSalesLog = {'LilUziVert':{'Tue':50,'Thu':60},'DrDre':{'Mon':70,'Tue':20, 'Fri':50},'21Savage':{'Tue':100,'Wed':100,'Thu':50},'Skrillex':{'Fri':100,'Sat':150,'Mon':200}}
    L1 = [{"x":1,"y":True,"z":"found"},{"x":2},{"y":False}]
    #print(palindromes("hellolle"))
    #print(palindromes("abbcbbd"))
    routes = {
"Lentil": ["Chinook", "Orchard", "Valley", "Emerald","Providence", "Stadium", "Main",
"Arbor", "Sunnyside", "Fountain", "Crestview", "Wheatland", "Walmart", "Bishop",
"Derby", "Dilke"],
"Wheat": ["Chinook", "Orchard", "Valley", "Maple","Aspen", "TerreView", "Clay",
"Dismores", "Martin", "Bishop", "Walmart", "PorchLight", "Campus"],
"Silver": ["TransferStation", "PorchLight", "Stadium", "Bishop","Walmart", "Shopco",
"RockeyWay"],
"Blue": ["TransferStation", "State", "Larry", "TerreView","Grand", "TacoBell",
"Chinook", "Library"],
"Gray": ["TransferStation", "Wawawai", "Main", "Sunnyside","Crestview", "CityHall",
"Stadium", "Colorado"]
}
    L2 = [(0,{"x":0,"y":True,"z":"zero"}),
 (0,{"x":1}),
 (1,{"y":False}),
 (1,{"x":3, "z":"three"}),
 (2,{})]

     
   # print(busStops(routes, "Stadium"))
    #print (searchDicts2(L2,"x"))
    #print (searchDicts2(L2,"t"))
   #print(sumSales(d2))
   #print(sumSalesN(d3))
    #print(palindromes("cabbbaccab"))
    #print(palindromes("bacdcabdbacdc"))
    #print(palindromes("myracecars"))
    iSequence = interlaceIter(iter([1,2,3,4,5,6,7,8,9]),iter("abcdefg"))
    print(typeHistogram(iSequence,5)) # returns [('int', 3), ('str', 2)]
    print(typeHistogram(iSequence,5)) # returns [('str', 3), ('int', 2)]
    print(typeHistogram(iSequence,5)) # returns [('int', 2), ('str', 2)]
    print(typeHistogram(iSequence,5)) # returns []
    #iSequence.__next__() # returns 1
    #iSequence.__next__() # returns 'a'
    #iSequence.__next__() # returns 2
    #for item in iSequence:
     #       print(item) 

def sumSales(d):
    new_dict = dict()
    for i in d:
        for j in d.get(i):
                if j in new_dict:
                        new_dict[j] = d.get(i).get(j) + new_dict.get(j)
                else:
                        new_dict[j] = d.get(i).get(j)

    return new_dict

def sumSalesN(L):
        new_dict = dict()
        for i in L:
            for j in i:
                for k in i.get(j):
                        #print(k)
                        if k in new_dict:
                                new_dict[k] = i.get(j).get(k) + new_dict.get(k)
                        else:
                                new_dict[k] = i.get(j).get(k)

        return new_dict

def searchDicts(L,k):
    var = None
    for dictionary in L:
        for key in dictionary:
            if key == k:
               var = dictionary.get(key)

    return var

def searchDicts2(tL,k):
        def searchDictsHelper(tL,k,index):
                newIndex = tL[index][0]
                if k in tL[index][1]:
                        return tL[index][1].get(k)
                elif (index == 0 and tL[index][1].get(k) == None):
                        return None
                else:
                        return searchDictsHelper(tL,k,newIndex)
        return searchDictsHelper(tL,k,len(tL)-1)

                        
def busStops(buses, stop):
    busRoutes = [key for key in buses if stop in buses.get(key)]
    return busRoutes

def palindromes(S):
        new_list = []
        i = 0
        while i < len(S):
                newString = S[i]
                j = i+1
                i = i+1
                while j < len(S):
                        newString = newString + S[j]
                        reverseString = newString [::-1]
                        #print(newString)
                        j = j+1
                        if (newString == reverseString and new_list.count(newString) == 0):
                                new_list.append(newString)
        new_list.sort()
        return new_list

class interlaceIter(object):
        def __init__(self,iter1,iter2):
                self.i1 = iter1
                self.i2 = iter2
                self.flag = False
                try:
                        self.current = self.i1.__next__()
                except:
                        self.current = None
        
        def __next__(self):
                if self.current is None:
                        raise StopIteration
                result = self.current
                try:
                        if (self.flag == False):
                                self.current = self.i2.__next__()
                                self.flag = True
                        else:
                                self.current = self.i1.__next__()
                                self.flag = False
                except StopIteration:
                        raise StopIteration
                
                return result
        def __iter__(self):
                return self

def typeHistogram(it,n):
        newList = []
        newDict = dict()
        counter = 0
        while counter < n:
              counter = counter+1
              try:
                      var = next(it)
                      typeVar = type(var).__name__
                      if newDict.get(typeVar) == None:
                              newDict[typeVar] = 1
                      else:
                              newDict[typeVar] = newDict.get(typeVar) + 1
              except StopIteration:
                      break
        newTuple = tuple(newDict.items())
        for tup in newTuple:
                newList.append(tup)
        return newList

main()
