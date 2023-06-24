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
    l = []  #list of commands (used reserved words)
    t = []  #location of parameter divider ":"
    b = [] #parameters
    both = []
    for _ in range(len(inputList)):
        l.append("")
        for y in range(len(inputList[_])):
            if inputList[_][y] != ":":
                l[_] = l[_] + inputList[_][y]
                t.append(-1)
            else:
                t[_] = y
                break
    for z in range(len(t)):
        if t[z] != -1:
            b.append(inputList[z][t[z] +1 :])
        else:
            b.append("")
    for i in range(len(l)):
        both.append([l[i], b[i]])
    i = 0
    for i in range(len(both)):
        try:
            both[i][0] = reservedWords.index(both[i][0])
        except ValueError:
            print(f"Your command at line {i} is not correct. \nYour code has been executed without the command '{both[i][0]}'")
            both[i][0] = ""
    return both
print(getReservedWordID(testList))