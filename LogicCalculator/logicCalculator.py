import copy


def runGame(goal, cur, count, options, past):
    if(goal == cur):
        return past
    if(count == 0):
        return None
    for i in options:
        past.append(i)
        temp = copy.copy(past)
        if(i[0:3] == "sum"):
            val = int(i[3:])
            r = runGame(goal, cur + val, count - 1, options, past)
        elif(i[1:3] == "to"):
            cur = str(cur)
            val = ""
            for j in cur:
                if(j == i[0]):
                    val += i[3]
                else:
                    val += j
            r = runGame(goal, int(val), count - 1, options, past)
        elif(i[0:3] == "exp"):
            val = cur ** int(i[3:])
            r = runGame(goal, int(val), count - 1, options, past)
        elif(i[0:4] == "back"):
            val = str(cur)[:-1]
            if(val == ""):
                val = 0
            r = runGame(goal, int(val), count - 1, options, past)
        elif(i[0:5] == "times"):
            val = float(i[5:])
            if(abs(cur*val - int(cur*val)) > 0.1):
                r = None
            else:
                r = runGame(goal, int(cur * val), count - 1, options, past)
        elif(i[0:6] == "append"):
            val = str(cur) + i[6:]
            r = runGame(goal, int(val), count - 1, options, past)
        elif(i[0:6] == "switch"):
            r = runGame(goal, cur*-1, count - 1, options, past)
        elif(i[0:7] == "reverse"):
            cur = str(cur)
            val = ""
            for j in range(len(cur)-1, -1, -1):
                val += cur[j]
            r = runGame(goal, int(val), count - 1, options, past)
        else:
            raise Exception("Command not recognized")
            r = None
        past = temp[:-1]
        if(r):
            return r
    past = []
    return None