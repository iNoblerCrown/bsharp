reservedWords = ["move", "delete"]
pythonVersion = ["os.?", "os.remove"]

def lineSeperator(inputstring):
    l = inputstring.split("\n")
    for x in range(len(l)):
        l[x] = l[x].replace("to", "")
    return l

def commandCheck(inputList):
    output = str("")
    for x in range(len(inputList)):
        if "=" in inputList[x]:
            output += f"{inputList[x]}\n"

def getReservedWordID(inputList, checkedCode):

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
        both.append([l[i], b[i].strip(" ")])
    i = 0
    for i in range(len(both)):
        try:
            both[i][0] = reservedWords.index(both[i][0])
        except ValueError:
            print(f"Your command at line {i} is not correct. \nYour code has been executed without the command '{both[i][0]}'.")
            both[i][0] = ""
    return both


def convertToPY(arrayOfCode, currentOutput):
    output = str(f"import os\nimport shutil\n{currentOutput}\n")
    for x in range(len(arrayOfCode)):
        if arrayOfCode[x][0] != "":
            output += pythonVersion[int(arrayOfCode[x][0])]
            output += "(" + arrayOfCode[x][1] + ")\n"
    return output

def executeAll(stringOfPyCode):
    y = True
    try:
        exec(stringOfPyCode)
    except Exception as x:
        print(f"The Error '{x}' has occured.")
        y = False
    if y == True:
        print("Your code has worked flawlessly")

def JITExecution(stringOfPyCode):
    l = stringOfPyCode.split("\n")
    for x in range(len(l)):
        try:
            exec(l[x])
        except Exception as i:
            print(f"The error '{i}' has occured at line {x + 1}. \n All other code has been executed successfully.")
            y = False
    if y == True:
        print("Your code has worked flawlessly")


def main(inputString, mode):
    a = lineSeperator(inputString)
    y = commandCheck(a)
    a = getReservedWordID(a, y)
    a = convertToPY(a, y)
    if mode == "step-by-step" or mode == "sbs":
        JITExecution(a)
    elif mode == "all-at-once" or mode == "aao":
        executeAll(a)
    return a

def start():
    x = input("Your code:\n")
    y = input("How should the code be executed?\n(all-at-once [aao] or step-by-step [sbs])\n")
    main(x, y)


start()