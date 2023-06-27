reservedWords = ["move", "delete", "say", "create", "rename", "close"]
pythonVersion = ["shutil.move", "os.remove", "print", "file = open", "os.rename", "exit()"]



def lineSeperator(inputstring):
    l = inputstring.split("\n")
    for x in range(len(l)):
        l[x] = l[x].replace(" to ", ",").replace("from", "")
    return l

def commandCheck(inputList):
    if inputList[0] == "close":
        exit()
    output = str("")
    for x in range(len(inputList)):
        if "=" in inputList[x]:
            output += f"{inputList[x]}\n"
        elif "loop":
            "Loop system einbauen"

    return output

def secondaryCommandCheck(inputList):
    for x in range(len(inputList)):
        if "=" in inputList[x]:
            inputList[x] = ""
        elif "loop property":
            "LOOP PROPERTY EINBAUEN"
    return inputList

def getReservedWordID(inputList):

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
        try:
            both.append([l[i], b[i].strip(" ")])
        except:
            ""
    i = 0
    for i in range(len(both)):
        if both[i][0] == "create":
            both[i][1] += ", 'w'"
        try:
            both[i][0] = reservedWords.index(both[i][0])
        except ValueError:
            if both[i][0] != "":
                print(f"Your command at line {i} is not correct. \nYour code has been executed without the command '{both[i][0]}'.")
                both[i][0] = ""
    return both


def convertToPY(arrayOfCode, currentOutput):
    b = str(f"import os\nimport shutil\n{currentOutput}\n")
    for x in range(len(arrayOfCode)):
        if arrayOfCode[x][0] != "":
            b += pythonVersion[int(arrayOfCode[x][0])]
            b += "(" + arrayOfCode[x][1] + ")\n"
    return b

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
    y = True
    l = stringOfPyCode.split("\n")
    for x in range(len(l)):
        try:
            exec(l[x])
        except Exception as i:
            print(f"The error '{i}' has occured at line {x - 2}. \n All other code has been executed successfully.")
            y = False
    if y == True:
        print("Your code has worked flawlessly")

def getExecutionMethod():
    y = input("How should the code be executed?\n(all-at-once [aao] or step-by-step [sbs])\n")
    return y

def main(inputString):
    a = lineSeperator(inputString)
    y = commandCheck(a)
    a = secondaryCommandCheck(a)
    a = getReservedWordID(a)
    mode = getExecutionMethod()
    a = convertToPY(a, y)
    if mode == "step-by-step" or mode == "sbs":
        JITExecution(a)
    elif mode == "all-at-once" or mode == "aao":
        executeAll(a)
    else:
        print("Unvalid execution method.")
        exit()
    return a

def start():
    x = input("Your code:\n")
    main(x)

#Test string
#main("""a = 1
#b = 2
#say: a + b""", "aao")

start()