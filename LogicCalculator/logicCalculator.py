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

# Question 1
print(runGame(2, 0, 2, ["sum1"], []))

# Question 2
print(runGame(8, 0, 3, ["sum2", "sum3"], []))

# Question 3
print(runGame(12, 0, 3, ["times4", "sum1", "sum2"], []))

# Question 4
print(runGame(7, 1, 3, ["sum4", "sum-2"], []))

# Question 5
print(runGame(20, 0, 3, ["times4", "sum4"], []))

# Question 6
print(runGame(40, 0, 4, ["sum2", "times4"], []))

# Question 7
print(runGame(10, 100, 4, ["sum3", "times0.2"], []))

# Question 8
print(runGame(4, 4321, 3, ["back"], []))

# Question 9
print(runGame(4, 0, 3, ["sum8", "times5", "back"], []))

# Question 10
print(runGame(9, 50, 4, ["times0.2", "times3", "back"], []))

# Question 11
print(runGame(100, 99, 3, ["sum-8", "times11", "back"], []))

# Question 18
print(runGame(101, 0, 3, ["append1", "append0"],[]))

# Question 28
print(runGame(222, 0, 4, ["append1", "1to2"], []))

# Question 29
print(runGame(93, 0, 4, ["sum6", "times7", "6to9"], []))

# Question 37
print(runGame(9, 0, 3, ["sum-1", "sum-2", "exp2"], []))

# Question 41
print(runGame(-6, 0, 3, ["sum4", "sum2", "switch"], []))

# Question 52
print(runGame(4, 25, 5, ["sum-4", "times-4", "times" + str(1/3), "times" + str(1/8), "switch"], []))

# Question 55
print(runGame(101, 100, 3, ["append1", "sum9", "reverse"], []))