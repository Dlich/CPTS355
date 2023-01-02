import unittest
from HW3 import *

class HW3Tests(unittest.TestCase):
    def setUp(self):
        pass
    def test_sumSales(self):
        salesLog= {'Amazon':{'Mon':30,'Wed':100,'Sat':200},'Etsy':{'Mon':50,'Tue':20,'Wed':25,'Fri':30},'Ebay':{'Tue':60,'Wed':100,'Thu':30},'Shopify':{'Tue':100,'Thu':50,'Sat':20}}
        summedLog = {'Fri': 30, 'Mon': 80, 'Sat': 220, 'Thu': 80, 'Tue': 180, 'Wed': 225}
        userTestSalesLog = {'LilUziVert':{'Tue':50,'Thu':60},'DrDre':{'Mon':70,'Tue':20, 'Fri':50},'21Savage':{'Tue':100,'Wed':100,'Thu':50},'Skrillex':{'Fri':100,'Sat':150,'Mon':200}}
        userTestSummedLog = {'Tue': 170, 'Thu': 110, 'Mon': 270, 'Fri': 150, 'Wed': 100, 'Sat': 150}
        userTestSalesLog2 = {}
        userTestSummedLog2 = {}
        self.assertDictEqual(sumSales(salesLog),summedLog)
        self.assertDictEqual(sumSales(userTestSalesLog), userTestSummedLog)
        self.assertDictEqual(sumSales(userTestSalesLog2), userTestSummedLog2)

    def test_sumSalesN(self):
        salesLogN = [{'Amazon':{'Mon':30,'Wed':100,'Sat':200},'Etsy':{'Mon':50,'Tue':20,'Wed':25,'Fri':30},'Ebay':{'Tue':60,'Wed':100,'Thu':30},'Shopify':{'Tue':100,'Thu':50,'Sat':20}},{'Shopify':{'Mon':25},'Etsy':{'Thu':40, 'Fri':50}, 'Ebay':{'Mon':100,'Sat':30}},{'Amazon':{'Sun':88},'Etsy':{'Fri':55},'Ebay':{'Mon':40},'Shopify':{'Sat':35}}]
        summedLogN = {'Fri': 135,'Mon':245,'Sat':285,'Sun': 88,'Thu': 120,'Tue':180,'Wed':225}
        userTestSalesLogN = [{'PopSmoke':{'Tue':30,'Thu':100,'Sat':200},'LilUziVert':{'Mon':30,'Tue':60,'Wed':50,'Fri':15},'Subtronics':{'Tue':5,'Wed':8,'Thu':4},'MotleyCrue':{'Sat':100,'Fri':50,'Wed':20}},{'MotleyCrue':{'Wed':25},'LilUziVert':{'Thu':29, 'Fri':10}, 'Subtronics':{'Tue':100,'Mon':30}},{'PopSmoke':{'Mon':89},'LilUziVert':{'Fri':55},'Subtronics':{'Mon':40},'MotleyCrue':{'Sat':35}}]
        userTestSummedLog = {'Tue': 195, 'Thu': 133, 'Sat': 335, 'Mon': 189, 'Wed': 103, 'Fri': 130}
        self.assertDictEqual(sumSalesN(salesLogN),summedLogN)
        self.assertDictEqual(sumSalesN(userTestSalesLogN), userTestSummedLog)

    def test_searchDicts(self):
        #searchDicts inputs
        dictList = [{"x":1,"y":True,"z":"found"},{"x":2},{"y":False}]
        userTestDictList = [{"t":4,"i":"test"},{"i": "test2"},{"t":True}]
        self.assertEqual(searchDicts(dictList,"x"),2)
        self.assertEqual(searchDicts(dictList,"y"),False)
        self.assertEqual(searchDicts(dictList,"z"),"found")
        self.assertEqual(searchDicts(dictList,"t"),None)
        self.assertEqual(searchDicts(userTestDictList,"t"),True)
        self.assertEqual(searchDicts(userTestDictList, "i"), "test2")

    def test_searchDicts2(self):
        dictList2 = [(0,{"x":0,"y":True,"z":"zero"}), (0,{"x":1}), (1,{"y":False}), (1,{"x":3, "z":"three"}), (2,{})]
        userTestDictList2 = [(0,{"y":True}),(0,{"x":5}),(0,{"z":"Test"}),(1,{"x":4, "y":False}),(2,{"t":True}),(3,{"x":5}),(5,{})]
        self.assertEqual(searchDicts2(dictList2,"x"),1)
        self.assertEqual(searchDicts2(dictList2,"y"),False)
        self.assertEqual(searchDicts2(dictList2,"z"),"zero")
        self.assertEqual(searchDicts2(dictList2,"t"),None)
        self.assertEqual(searchDicts2(userTestDictList2, "x"),5)
        self.assertEqual(searchDicts2(userTestDictList2, "y"), False)

    def test_busStops(self):
        routes = {
            "Lentil": ["Chinook", "Orchard", "Valley", "Emerald","Providence", "Stadium", "Main", "Arbor", "Sunnyside", "Fountain", "Crestview", "Wheatland", "Walmart", "Bishop", "Derby", "Dilke"],
            "Wheat": ["Chinook", "Orchard", "Valley", "Maple","Aspen", "TerreView", "Clay", "Dismores", "Martin", "Bishop", "Walmart", "PorchLight", "Campus"],
            "Silver": ["TransferStation", "PorchLight", "Stadium", "Bishop","Walmart", "Shopco", "RockeyWay"],
            "Blue": ["TransferStation", "State", "Larry", "TerreView","Grand", "TacoBell", "Chinook", "Library"],
            "Gray": ["TransferStation", "Wawawai", "Main", "Sunnyside","Crestview", "CityHall", "Stadium", "Colorado"]
        }
        self.assertEqual(busStops(routes,"Stadium"),['Lentil', 'Silver', 'Gray'])
        self.assertEqual(busStops(routes,"Bishop"),['Lentil', 'Wheat', 'Silver'])
        self.assertEqual(busStops(routes,"EECS"),[])
        self.assertEqual(busStops(routes,"Chinook"), ['Lentil','Wheat','Blue']) #usertest1
        self.assertEqual(busStops(routes, None), []) #usertest2

    def test_palindromes(self):
        self.assertEqual(palindromes ('cabbbaccab'),['abbba', 'acca', 'baccab', 'bb', 'bbb', 'cabbbac', 'cc'] )
        self.assertEqual(palindromes ('bacdcabdbacdc') ,['abdba', 'acdca', 'bacdcab', 'bdb', 'cabdbac', 'cdc', 'cdcabdbacdc', 'dcabdbacd'])
        self.assertEqual(palindromes (' myracecars')  ,['aceca', 'cec', 'racecar'])
        self.assertEqual(palindromes('hellolle'), ['ellolle', 'll', 'lloll', 'lol'])
        self.assertEqual(palindromes('abbcbbd'), ['bb', 'bbcbb', 'bcb'])

    class OddsEvens(object):
        def __init__(self,init):
            self.current = init
        def __next__(self):
            result = self.current
            self.current += 2
            return result
        def __iter__(self):
            return self

    #This function assumes that the first value in L is less than or equal to N.
    def getUntilN(self,L,N):
        tempL = []
        for item in L:
            tempL.append(item)
            if item>=N: break
        return tempL

    def test_interlaceIter(self):
    	#test 1
        iSequence = interlaceIter(iter([1,2,3,4,5,6,7,8,9]),iter("abcdefg"))
        iSequenceUserTest = interlaceIter(iter([1,2,3,4,5,6]),iter("abcdef"))

        self.assertEqual(iSequence.__next__(),1)
        self.assertEqual(iSequence.__next__(),'a')
        self.assertEqual(iSequence.__next__(),2)
        self.assertEqual(iSequenceUserTest.__next__(), 1)
        rest = []
        for item in iSequence:
            rest.append(item)
        userRest = []
        for item in iSequenceUserTest:
            userRest.append(item)
        self.assertEqual(userRest, ['a',2,'b',3,'c',4,'d',5,'e',6])
        self.assertEqual(rest,['b',3,'c',4,'d',5,'e',6,'f',7,'g'])


        #test2
        naturals = interlaceIter(self.OddsEvens(1),self.OddsEvens(2))
        self.assertEqual(naturals.__next__(),1)
        first20 = self.getUntilN(naturals,20)
        self.assertEqual(first20,[x for x in range(2,21)])
        self.assertEqual(naturals.__next__(),21)


    def test_typeHistogram(self):
    	#test 1
        iSequence1 = interlaceIter(iter([1,2,3,4,5,6,7,8,9]),iter("abcdefg"))
        iSequenceUserTest1 = interlaceIter(iter([1,2,3,4,5,6]),iter("abcdef"))
        self.assertEqual(sorted(typeHistogram(iSequence1,5)), sorted([('int', 3), ('str', 2)]))
        self.assertEqual(sorted(typeHistogram(iSequence1,5)), sorted([('str', 3), ('int', 2)]))
        self.assertEqual(sorted(typeHistogram(iSequence1,5)), sorted([('int', 2), ('str', 2)]))
        self.assertEqual(sorted(typeHistogram(iSequence1,5)), [])
        #test 2
        iSequence1 = interlaceIter(iter([1,2,3,4,5,6,7,8,9]),iter("abcdefg"))
        iSequence2 = interlaceIter(iSequence1, iter([(1,'a'),(2,'b'),(3,'c'),(4,'d')]))
        self.assertEqual(sorted(typeHistogram(iSequence2,8)),sorted([('int', 2), ('str', 2),('tuple',4)]))
        self.assertEqual(sorted(typeHistogram(iSequence2,8)), [])




if __name__ == '__main__':
    unittest.main()

