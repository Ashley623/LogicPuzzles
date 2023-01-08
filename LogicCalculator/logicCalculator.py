import copy

"""
Summary:
    runGame runs through a game of the logic calculator and returns the solution

Parameters:
    goal (int): The end number to get to
    cur (int): The current number, which at the beginning call is the starting number
    count (int): The number of moves you are able to take
    options (list of str): The different moves available to make
    past (list of str): The previous moves done, [] at start

Returns:
    past (list of str): The moves that result in the correct number
"""
def runGame(goal, cur, count, options, past):
    # Base cases for the recursion
    if(goal == cur):
        return past # Found correct solution
    if(count == 0):
        return None # Found dead end
    
    # Tries out each option, and then recusively calls this method again to see if it results in a correct solution or
    #   a dead end
    for i in options:
        past.append(i)
        # Add the current option to the past
        temp = copy.copy(past)
        # Copys the past so that if it is changed in the recursive call it is not changed outside
        #   the recursive call
        
        # Checks which option i is, then recursively calls this method again with cur updated with the option chosen
        #   and with count decreased by one
        if(i[0:3] == "sum"):
            val = int(i[3:])
            r = runGame(goal, cur + val, count - 1, options, past)
        elif(i[1:3] == "to"):
            cur = str(cur)
            val = ""
            for j in cur: # Checks if any digit is a digit to change and adds the correct value to val
                if(j == i[0]):
                    val += i[3]
                else:
                    val += j
            r = runGame(goal, int(val), count - 1, options, past)
        elif(i[0:3] == "exp"):
            val = cur ** int(i[3:])
            r = runGame(goal, int(val), count - 1, options, past)
        elif(i[0:4] == "back"):
            # This options removes the right most digit
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
            # This option switches the sign of the number
            r = runGame(goal, cur*-1, count - 1, options, past)
        elif(i[0:7] == "reverse"):
            cur = str(cur)
            val = ""
            for j in range(len(cur)-1, -1, -1): # Loops through to reverse the number as a string
                val += cur[j]
            r = runGame(goal, int(val), count - 1, options, past)
        else:
            raise Exception("Command not recognized")
            r = None
        past = temp[:-1]
        # Removes the current option from past, because if it didn't work we need to add a new one to past
        if(r):
            # If r is not None, that means a correct solution was found, and then you should return r
            return r
    return None # Returns none if none of the options resulted in correct solutions