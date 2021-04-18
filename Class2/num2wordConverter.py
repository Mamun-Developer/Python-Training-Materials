mid_numwords = [(1000, "thousand"), (100, "hundred"),
                     (90, "ninety"), (80, "eighty"), (70, "seventy"),
                     (60, "sixty"), (50, "fifty"), (40, "forty"),
                     (30, "thirty")]
midNumWords = {
    1000:"thousand",
    100:"hundred",
    90: "ninety",
    80: "eighty",
    70: "seventy",
    60: "sixty",
    50: "fifty",
    40: "forty",
    30: "thirty",
    20: "twenty"
}
low_numwords = ["twenty", "nineteen", "eighteen", "seventeen",
                     "sixteen", "fifteen", "fourteen", "thirteen",
                     "twelve", "eleven", "ten", "nine", "eight",
                     "seven", "six", "five", "four", "three", "two",
                     "one", "zero"]
low_numwords.reverse()

number = 998
if number<len(low_numwords):
    print(low_numwords[number])
elif number<100:
    second = number%10
    first = number - second
    if second == 0:
        print(midNumWords[first])
    else:
        pass
        print(midNumWords[first]+" "+low_numwords[second])
elif number<1000:
    third = number%10 #8
    second = (number % 100)-third #90
    first = int((number - (number % 100))/100) # 1/2/3/4/5/6/7/8/9/
    if (second==0) and (third==0):
        print(low_numwords[first]+" "+midNumWords[100])
    elif (second+third)<21:
        print(low_numwords[first]+" "+midNumWords[100]+" and "+low_numwords[second+third])
    else:
        print(low_numwords[first]+" "+midNumWords[100]+" and "+midNumWords[second]+" "+low_numwords[third])