import re
import ast
import sys
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

def dictPush(d,linkValue):
    dictstack.append((d,linkValue))
    #dictPush pushes the dictionary ‘d’ to the dictstack. 
    #Note that, your interpreter will call dictPush only when Postscript 
    #“begin” operator is called. “begin” should pop the empty dictionary from 
    #the opstack and push it onto the dictstack by calling dictPush.

def define(name, value):
    if dictstack.__len__() == 0:
        print ("Dictionary Stack is empty")
        newDict = {}
        newDict[name] = value
        dictPush(newDict,0)
    else:
        dictstack[len(dictstack)-1][0][name] = value
    #add name:value pair to the top dictionary in the dictionary stack. 
    #Keep the '/' in the name constant. 
    #Your psDef function should pop the name and value from operand stack and 
    #call the “define” function.

def lookup(name,scope):
    if scope == "dynamic":
        var = None
        name = "/" + name
        for item in dictstack:
            if item[0].get(name) != None:
                var = item[0].get(name)
            if var == None:
                print ("Could not find name")
        return var
    else:
        var = None
        name = "/" + name
        itemFound = False
        tempTuple = list(dictstack)
        index = len(tempTuple) - 1
        while itemFound == False:
            if tempTuple[index][0].get(name) != None:
                var = tempTuple[index][0].get(name)
                itemFound = True
            else:
                index = tempTuple[index][1]
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
            opPush(var1+var2)
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
        if var1 == var2:
            opPush(True)
        else:
            opPush(False) 
    else:
        print("Opstack is not big enough")

def lt():
    if len(opstack) > 1:
        var1 = opPop()
        var2 = opPop()
        if var2 < var1:
            opPush(True)
        else:
            opPush(False)
    else:
        print("Opstack is not big enough")

def gt():
    if len(opstack) > 1:
        var1 = opPop()
        var2 = opPop()
        if var2 > var1:
            opPush(True)
        else:
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
    if (len(opstack)) > 1:
        count = opPop()
        copyList = list()
        while count > 0:
            val = opPop()
            copyList.append(val)
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
    copyOpStack = list(opstack)
    copyDictStack = list(dictstack)
    print("==============")
    while len(copyOpStack) != 0:
        print(copyOpStack.pop())
    print("==============")
    while len(copyDictStack) != 0:
        var = copyDictStack.pop()
        sys.stdout.write("----")
        sys.stdout.write(str(len(copyDictStack)))
        sys.stdout.write("---")
        sys.stdout.write(str(var[1]))
        print("---")
        for i,j in var[0].items():
            print(i,j)
    print("==============")
    

#--------------------------- 20% -------------------------------------
# Define the dictionary manipulation operators: psDict, begin, end, psDef
# name the function for the def operator psDef because def is reserved in Python. Similarly, call the function for dict operator as psDict.
# Note: The psDef operator will pop the value and name from the opstack and call your own "define" operator (pass those values as parameters).
# Note that psDef()won't have any parameters.

#def psDict():
#    opPop()
#    newDict = dict()
#    opPush(newDict)

#def begin():
#    newDict = opPop()
#    dictPush(newDict)

#def end():
#    dictPop()

def psDef():
    value = opPop()
    name = opPop()
    define(name,value)


def tokenize(s):
    return re.findall("/?[a-zA-Z][a-zA-Z0-9_]*|[\[][a-zA-Z-?0-9_\s!][a-zA-Z-?0-9_\s!]*[\]]|[-]?[0-9]+|[}{]+|%.*|[^ \t\n]", s)
    
def forall(scope):
    if len(opstack) > 1:
        code = opPop()
        inputs = opPop()
        if (isinstance(inputs, list) and isinstance(code, dict)):
            for x in inputs:
                opPush(x)  # push the array element onto the stack
                interpretSPS(code,scope)
        else:
            print("Error: forall expects an array and a codearray")
            opPush(inputs)
            opPush(code)
    else:
        print("Stack not big enough")

def psIf(scope):
    if len(opstack) > 1:
        code = opPop()
        boolean = opPop()
        if (isinstance(boolean, bool) and isinstance(code, dict)):
            if boolean == True:
                interpretSPS(code,scope)
            else:
                print("Boolean was not True")
        else:
            print("One of the variables wasnt correct")
            opPush(boolean)
            opPush(code)
    else:
        print("Stack not big enough")

def psRepeat(scope):
    if len(opstack) > 1:
        code = opPop()
        count = opPop()
        if isinstance(count,int) and isinstance(code,dict):
            while count > 0:
                interpretSPS(code,scope)
                count = count-1
        else:
            print("one of the variables wasnt correct")
            opPush(count)
            opPush(code)
    else:
        print("Stack not big enough")

def ifElse(scope):
    if len(opstack) > 2:
        code1 = opPop()
        code2 = opPop()
        boolean = opPop()
        if isinstance(boolean,bool) and isinstance(code1,dict) and isinstance(code2,dict):
            if boolean == True:
                interpretSPS(code2,scope)
            else:
                interpretSPS(code1,scope)
        else:
            print("one of the items isnt correct")
            opPush(boolean)
            opPush(code2)
            opPush(code1)
    else:
        "Stack not big enough"
builtinoperators = {'add':add, 'sub':sub, 'def':psDef, 'forall':forall, 'mul':mul, 'dup':dup,'length':length, 
'and':psAnd, 'eq':eq, 'getinterval':getinterval, 'putinterval':putinterval, 'get':get, 
'exch':exch, 'repeat':psRepeat, 'if':psIf, 'ifelse':ifElse, 'count':count, 'copy':copy, 
'lt':lt, 'gt':gt, 'or':psOr, 'not':psNot, 'put':put, 'pop':pop, 'clear':clear, 'mark':mark, 'cleartomark':cleartomark, 'stack':stack, 'counttomark':counttomark}

# COMPLETE THIS FUNCTION
# The it argument is an iterator.
# The tokens between '{' and '}' is included as a sub code-array (dictionary). If the
# parenteses in the input iterator is not properly nested, returns False.
def groupMatch(it):
    res = []
    for c in it:
        if c == '}':
            return {'codearray':res}
        elif c=='{':
            # Note how we use a recursive call to group the tokens inside the
            # inner matching parenthesis.
            # Once the recursive call returns the code-array for the inner 
            # parenthesis, it will be appended to the list we are constructing 
            # as a whole.
            res.append(groupMatch(it))
        else:
            #Checks if the string should be a boolean, a integer or a list and then appropriately changes them to their proper data types
            if c == "false":
                c = False
            elif c == "true":
                c = True
            elif c.isdigit() == True:
                c = int(c)
            elif '[' in c and ']' in c:
                newList = list()
                aList = c[1:-1].split(' ')
                for item in aList:
                    try: #Checks if the item is an integer
                        item = int(item)
                        newList.append(item)
                    except ValueError: #if the item isnt an integer then its either a boolean or a string
                        if item == "false":
                            item = False
                        elif item == "true":
                            item = True
                        newList.append(item)
                c = newList
            res.append(c)
    return False



# COMPLETE THIS FUNCTION
# Function to parse a list of tokens and arrange the tokens between { and } braces 
# as code-arrays.
# Properly nested parentheses are arranged into a list of properly nested dictionaries.
def parse(L):
    res = []
    it = iter(L)
    for c in it:
        if c=='}':  #non matching closing parenthesis; return false since there is 
                    # a syntax error in the Postscript code.
            return False
        elif c=='{':
            res.append(groupMatch(it))
        else:
            if c == "false":
                c = False
            elif c == "true":
                c = True
            elif c.isdigit() == True:
                c = int(c)
            elif '[' in c and ']' in c:
                newList = list()
                strList = c[1:-1].split(' ') #obtains everything in between the brackets and splits it by the spaces
                for item in strList:
                    try:
                        item = int(item)
                        newList.append(item)
                    except ValueError:
                        if item == "false":
                            item = False
                        elif item == "true":
                            item = True
                        newList.append(item)
                c = newList
            res.append(c)
    return {'codearray':res}


## Change the following functions for static scope support. 
# dictPush
# define
# lookup
# stack


# Add a scope argument to the the following functions 
# psIf
# psIfelse
# psRepeat
# forall
# interpretSPS
# interpreter

# ------ SSPS functions -----------
# search the dictstack for the dictionary "name" is defined in and return the (list) index for that dictionary (start searhing at the top of the stack)
def staticLink(name):
    def staticLinkHelper(name,tupList,index):
        if '/' + name in tupList[index][0]:
            return index
        elif (index == 0 and tupList[index][0].get('/' + name) != None):
            return 0
        elif (index == 0 and tupList[index][0].get('/' + name) == None):
            return None
        else:
            return staticLinkHelper(name,tupList,tupList[index][1])
    return staticLinkHelper(name,dictstack,len(dictstack)-1)

#the main recursive interpreter function
def interpretSPS(tokenList,scope): 
    #print(tokenList)
    for token in tokenList.get('codearray'): #checks each item in the codearray
        #print(token)
        if isinstance(token, int) or isinstance(token,bool):
            opPush(token)
        elif isinstance (token, dict):
            opPush(token)
        elif isinstance(token,list):
            newArr = []
            mark = '*'
            opPush(mark) #pushes a mark to know where the lists items start to be added
            interpretSPS({'codearray':token},scope) #recursively calls interpretSPS with the token to see what it needs to do with that token
            val = opPop()
            while val != mark:
                newArr.append(val)
                val = opPop()
            newArr.reverse()
            opPush(newArr)
        elif isinstance(token,str):
            if token[0] == '/': #if theres a slash then it means its a variable
                opPush(token)
            elif builtinoperators.get(token) != None: #if the string is in the builtinoperators dictionary, then it means its a function that we need to call
                opFunc = builtinoperators.get(token, None)
                if token == 'if' or token == 'ifelse' or token == 'repeat' or token == 'forall':
                    opFunc(scope)
                else:
                    opFunc()
            else: #if its none of things then it means its a variable
                val = lookup(token,scope)
                 #we need to lookup the variable to find the value associated with it
                if isinstance(val,dict): #if its a dictionary then we call interpretSPS to figure out what to do with it
                    dictPush({},staticLink(token))
                    interpretSPS(val,scope)
                    dictPop()
                elif val is not None: #otherwise we print it
                    opPush(val)
                else: #otherwise we get an error because there is none
                    print("Error: nothing found during lookup")
        else:
            print("Error: Invalid token")

#parses the input string and calls the recursive interpreter to solve the
#program
def interpreter(s, scope):
    tokenL = parse(tokenize(s))
    interpretSPS(tokenL,scope)

#clears both stacks
def clearBoth():
    opstack[:] = []
    dictstack[:] = []

########################################################################
####  ASSIGNMENT 5 - SSPS TESTS
########################################################################

def sspsTests():
    testinput1 = """
    /x 4 def
    /g { x stack } def
    /f { /x 7 def g } def
    f
    """
    testinput2 = """
    /x 4 def
    [1 1 1] dup 1 [2 3] putinterval /arr exch def
    /g { x stack } def
    /f { 0 arr {7 mul add} forall /x exch def g } def
    f
    """
    testinput3 = """
    /m 50 def
    /n 100 def
    /egg1 {/m 25 def n} def
    /chic
    	{ /n 1 def
	      /egg2 { n stack} def
	      m  n
	      egg1
	      egg2
	    } def
    n
    chic
        """
    testinput4 = """
    /x 10 def
    /A { x } def
    /C { /x 40 def A stack } def
    /B { /x 30 def /A { x } def C } def
    B
    """
    testinput5 = """
    /x 10 def
    /n 5  def
    /A { 0  n {x add} repeat} def
    /C { /n 3 def /x 40 def A stack } def
    /B { /x 30 def /A { x } def C } def
    B
    """
    testinput6 = """
    /out true def 
    /xand { true eq {pop false} {true eq { false } { true } ifelse} ifelse dup /x exch def stack} def 
    /myput { out dup /x exch def xand } def 
    /f { /out false def myput } def 
    false f
    """
    testinput7 = """
    /x [1 2 3 4] def
    /A { x length } def
    /C { /x [10 20 30 40 50 60] def A stack } def
    /B { /x [6 7 8 9] def /A { x 0 get} def C } def
    B
    """
    testinput8 = """
    [0 1 2 3 4 5 6 7 8 9 10] 3 4 getinterval /x exch def
    /a 10 def  
    /A { x length } def
    /C { /x [a 2 mul a 3 mul dup a 4 mul] def A  a x stack } def
    /B { /x [6 7 8 9] def /A { x 0 get} def /a 5 def C } def
    B
    """
    userTest1 = """
    /x 5 def
    /A { x dup } def
    /C { /x [7 25 10 3] def A stack } def
    C
    """
    userTest2 = """
    /y [3 30 5] def
    /g { y stack } def
    /t { /x [50 6] def g } def
    t
    """
    userTest3 = """
    /t 55 def
    /Q { t } def
    /r { /t [5 4 3] def Q stack } def
    r

    """
    ssps_testinputs = [testinput1, testinput2, testinput3, testinput4, testinput5, testinput6, testinput7, testinput8, userTest1, userTest2,userTest3]
    i = 1
    for input in ssps_testinputs:
        print('TEST CASE -',i)
        i += 1
        print("Static")
        interpreter(input, "static")
        clearBoth()
        print("Dynamic")
        interpreter(input, "dynamic")
        clearBoth()
        print('\n-----------------------------')

sspsTests()