# *
# **
# ***
# ****
# *****

# Assignment 1.0
# *
# *
# **
# **
# ***
# ***
# ****
# ****
# *****
# ******
# ******

totalLine = int(input("Total Lines =  "))
totalCharInFirstLine = int(input("Total Char in first line = "))
incInEachLine = int(input("Increment Number in each line = "))
targetChar = str(input("Enter Char = "))
decrement = False
dec = int(input("For INC: 0, For DEC: 1"))
if dec == 0:
    decrement = False
else:
    decrement = True


def printPattern(tar_char, total_line, total_ch_in_first_line, inc_each_line):

    for i in range(total_line):
        for j in range(total_ch_in_first_line):
            print(tar_char,end="")

        print()
        if decrement == False:
            total_ch_in_first_line = total_ch_in_first_line + inc_each_line
        else:
            total_ch_in_first_line = total_ch_in_first_line - inc_each_line
printPattern(targetChar,totalLine,totalCharInFirstLine,incInEachLine)

