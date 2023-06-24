reservedWords = []
testList = ["aa:aaa", "a", "a"]
def lineSeperator(inputstring):
    l = inputstring.split("\n")
    return l

def getReservedWordID(inputList):
    IDs = {}
    for x in range(len(inputList)):
        d = {
            x : ""
        }
        IDs.update(d)
    l = []
    t = []
    for _ in range(len(inputList)):
        l.append("")
        for y in range(len(inputList[_])):
            if inputList[_][y] != ":":
                l[_] = l[_] + inputList[_][y]
                t.append(-1)
            else:
                t[_] = y
                break
    



#a
print(getReservedWordID(testList))