# WRITE YOUR NAME and YOUR COLLABORATORS HERE
# Daniel Lichtchouk
#------------------------- 10% -------------------------------------
# The operand stack: define the operand stack and its operations
opstack = []  #assuming top of the stack is the end of the list

# Now define the HELPER FUNCTIONS to push and pop values on the opstack 
# Remember that there is a Postscript operator called "pop" so we choose 
# different names for these functions.
# Recall that `pass` in python is a no-op: replace it with your code.

def opPop():
    if opstack.__len__() == 0:
        print ("Stack is empty")
    else:
        var = opstack.__getitem__(len(opstack)-1)
        opstack.pop(len(opstack)-1)
        return var
    
    # opPop should return the popped value.
    # The pop() function should call opPop to pop the top value from the opstack, but it will ignore the popped value.

def opPush(value):
    opstack.append(value)

#-------------------------- 20% -------------------------------------
# The dictionary stack: define the dictionary stack and its operations
dictstack = []  #assuming top of the stack is the end of the list

# now define functions to push and pop dictionaries on the dictstack, to 
# define name, and to lookup a name

def dictPop():
    if dictstack.__len__() == 0:
        print ("Stack is empty")
    else:
        var = dictstack.__getitem__(len(dictstack)-1)
        dictstack.pop(len(dictstack)-1)
        return var
    # dictPop pops the top dictionary from the dictionary stack.

def dictPush(d):
    dictstack.append(d)
    #dictPush pushes the dictionary ‘d’ to the dictstack. 
    #Note that, your interpreter will call dictPush only when Postscript 
    #“begin” operator is called. “begin” should pop the empty dictionary from 
    #the opstack and push it onto the dictstack by calling dictPush.

def define(name, value):
    if dictstack.__len__() == 0:
        print ("Dictionary Stack is empty")
        newDict = dict()
        newDict[name] = value
        dictPush(newDict)
    else:
        dictstack[len(dictstack)-1][name] = value
    #add name:value pair to the top dictionary in the dictionary stack. 
    #Keep the '/' in the name constant. 
    #Your psDef function should pop the name and value from operand stack and 
    #call the “define” function.

def lookup(name):
    var = None
    name = "/" + name
    for item in dictstack:
        if item.get(name) != None:
            var = item.get(name)
    if var == None:
        print ("Could not find name")
    return var
    # return the value associated with name
    # What is your design decision about what to do when there is no definition for “name”? If “name” is not defined, your program should not break, but should give an appropriate error message.


#--------------------------- 10% -------------------------------------
# Arithmetic, comparison, and boolean operators: add, sub, mul, eq, lt, gt, and, or, not 
# Make sure to check the operand stack has the correct number of parameters 
# and types of the parameters are correct.
def add():
    if len(opstack) > 1:
        var1 = opPop()
        var2 = opPop()
        if (isinstance(var1,int) and isinstance(var2,int)):
            opPush(var2+var1)
        else:
            print("Error - one operand was not a number")
            opPush(var2)
            opPush(var1)
    else:
        print("Opstack is not big enough")

def sub():
    if len(opstack) > 1:
        var1 = opPop()
        var2 = opPop()
        if (isinstance(var1,int) and isinstance(var2,int)):
            opPush(var2-var1)
        else:
            print("Error - one operand was not a number")
            opPush(var2)
            opPush(var1)
    else:
        print("Opstack is not big enough")

def mul():
    if len(opstack) > 1:
        var1 = opPop()
        var2 = opPop()
        if (isinstance(var1,int) and isinstance(var2,int)):
            opPush(var1*var2)
        else:
            print("Error - one operand was not a number")
            opPush(var2)
            opPush(var1)
    else:
        print("Opstack is not big enough")

def eq():
    if len(opstack) > 1:
        var1 = opPop()
        var2 = opPop()
        if (isinstance(var1,int) and isinstance(var2,int)) and var1 == var2:
            opPush(True)
        else:
            print("Error - one operand was not a number or the numbers werent equal")
            opPush(False) 
    else:
        print("Opstack is not big enough")

def lt():
    if len(opstack) > 1:
        var1 = opPop()
        var2 = opPop()
        if (isinstance(var1,int) and isinstance(var2,int)) and var2 < var1:
            opPush(True)
        else:
            print("Error - one operand was not a number or the first popped number wasnt less than the second popped number")
            opPush(False)
    else:
        print("Opstack is not big enough")

def gt():
    if len(opstack) > 1:
        var1 = opPop()
        var2 = opPop()
        if ((isinstance(var1,int) and isinstance(var2,int))) and var2 > var1:
            opPush(True)
        else:
            print("Error - one operand was not a number or the first popped number wasnt greater than the second popped number")
            opPush(False)
    else:
        print("Opstack is not big enough")

def psAnd():
    if len(opstack) > 1:
        var1 = opPop()
        var2 = opPop()
        if (isinstance(var1,bool) and isinstance(var2,bool)):
            if ((var1 and var2) == True):
                opPush(True)
            else:
                opPush(False)
        else:
            print("error - one operand was not a bool")
    else:
        print("Opstack is not big enough")





def psOr():
    if len(opstack) > 1:
        var1 = opPop()
        var2 = opPop()
        if (isinstance(var1,bool) and isinstance(var2,bool)):
            if ((var1 == True) or (var2 == True)):
                opPush(True)
            else:
                opPush(False)
        else:
            print("error - one operand was not a bool")
    else:
        print("Opstack is not big enough")

def psNot():
    if len(opstack) > 0:
        var1 = opPop()
        if isinstance(var1,bool):
            opPush(not(var1))
        else:
            print("error - one operand was not a bool")
    else:
        print("Opstack is not big enough")

#--------------------------- 25% -------------------------------------
# Array operators: define the string operators length, get, getinterval, put, putinterval
def length():
    if len(opstack) > 0:
        var = opPop()
        if isinstance(var,list):
            opPush(len(var))
        else:
            opPush(var)
            print("Popped item wasn't a list")
    else:
        print("Stack is empty")

def get():
    if len(opstack) > 1:
        index = opPop()
        arr = opPop()
        if isinstance(index,int) and isinstance(arr,list):
            opPush(arr[index])
        else:
            opPush(arr)
            opPush(index)
            print("One of the values wasn't an array or an integer")
    else:
        print("Stack wasn't big enough")

def getinterval():
    if (len(opstack)) > 2:
        count = opPop()
        index = opPop()
        arr = opPop()
        if (isinstance(index, int)) and isinstance(arr,list) and isinstance(count,int):
            opPush(arr[index:(index+count)])
        else:
            print("one of the varibles wasnt correct")
            opPush(arr)
            opPush(index)
            opPush(count)
    else:
        print("Stack not big enough")
            

def put():
    if (len(opstack)) > 2:
        value = opPop()
        index = opPop()
        arr = opPop()
        if isinstance(index,int) and isinstance(arr,list) and isinstance(value,int):
            arr[index] = value
        else:
            print("one of the varibales wasnt correct")
            opPush(arr)
            opPush(index)
            opPush(value)
    else:
        print("stack not big enough")


def putinterval():
    if (len(opstack)) > 2:
        arr2 = opPop()
        index = opPop()
        arr1 = opPop()
        if isinstance(arr2,list) and isinstance(index,int) and isinstance(arr1,list):
            for item in arr2:
                arr1[index] = item
                index = index + 1
        else:
            print("one of the variables wasn't correct")
    else:
        print("Stack not big enough")
            

#--------------------------- 15% -------------------------------------
# Define the stack manipulation and print operators: dup, copy, count, pop, clear, exch, mark, cleartomark, counttotmark
def dup():
    if (len(opstack)) > 0:
        var = opPop()
        opPush(var)
        opPush(var)
    else:
        print("Not big enough")

def copy():
    if (len(opstack)) > 2:
        count = opPop()
        copyList = []
        while count > 0:
            copyList.append(opPop())
            count = count - 1
        copyList.reverse()
        for item in copyList:
            opPush(item)
        for item in copyList:
            opPush(item)

    else:
        print("Stack not big enough")
        

def count():
    opPush(len(opstack))

def pop():
    if (len(opstack)) > 0:
        return opPop()
    else:
        print("Stack not big enough")

def clear():
    while len(opstack)>0:
        opPop()

def exch():
    if (len(opstack)) > 1:
        item1 = opPop()
        item2 = opPop()
        opPush(item1)
        opPush(item2)
    else:
        print("Stack not big enough")

def mark():
    opPush("-mark-")

def cleartomark():
    if "-mark-" in opstack:
        var = opPop()
        count = 0
        while var != "-mark-":
            count = count+1
            var = opPop()
    else:
        print("Mark is not on the stack")
def counttomark():
    count = 0
    if "-mark-" in opstack:
        for item in reversed(opstack):
            if (item == "-mark-"):
                break
            else:
                count = count + 1
        opPush(count)
    else:
        print("No mark in the stack")

def stack():
    for item in opstack:
        print(item)

#--------------------------- 20% -------------------------------------
# Define the dictionary manipulation operators: psDict, begin, end, psDef
# name the function for the def operator psDef because def is reserved in Python. Similarly, call the function for dict operator as psDict.
# Note: The psDef operator will pop the value and name from the opstack and call your own "define" operator (pass those values as parameters).
# Note that psDef()won't have any parameters.

def psDict():
    opPop()
    newDict = dict()
    opPush(newDict)

def begin():
    newDict = opPop()
    dictPush(newDict)

def end():
    dictPop()

def psDef():
    value = opPop()
    name = opPop()
    define(name,value)

def main():
    strt = "op"
    print(strt[0])
    #copy()
    #self.assertTrue(opPop()==4 and opPop()==3 and opPop()==1 and opPop()==4 and opPop()==3 and opPop()==1 and opPop()==True)


main()