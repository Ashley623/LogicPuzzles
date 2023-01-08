from logicCalculator import runGame

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