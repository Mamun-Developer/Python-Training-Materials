import time
# 1. Input N of Numbers
# 2. Run loop and input all number into list
# 3. Run look and sum all number
# 4. Print the result

def numberN(message):
    '''
    This function receives an input from an user and returns an integer number
    :param message: That you want to print while taking input
    :return: N
    '''
    return int(input(message))

def inputListOfNumber(n):
    '''
    blah blah blah
    :param n:
    :return:
    '''
    numbers = list()
    for i in range(0,n):
        num = int(input(" "))
        numbers.append(num)

    return numbers

def sum_list_of_numbers(numList):
    '''
    Sums up all the numbers in the list and returns as an integer form.
    The list must contain integer numbers.
    :param numList:
    :return:
    '''
    result = 0
    for i in numList:
        result  = result + i
    return result
print(__name__)

if __name__=="__main__":
    n = numberN("Enter N: ")
    nums = inputListOfNumber(n)
    result = sum_list_of_numbers(nums)
    print("SUM of "+str(nums)+" = "+str(result))




