"""(2021FA.CSC.256.0001)
James Diller
Lesson 01 - Full Retirement Age Calculator

Rewritten with more age ranges
"""

rYear = [1960, 1959, 1958, 1957, 1956, 1955, 1943, 1942, 1941, 1940, 1939, 1938, 1937]
rAge = [[67,0],[66,10],[66,8],[66,6],[66,4],[66,2],[66,0],[65,10],[65,8],[65,6],[65,4],[65,2],[65,0]]
rMonth = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

def calcRetirement(bYear,bMonth):
    for i in range(len(rYear)):
        if bYear >= rYear[i]:
            break

    bMonth = bMonth + rAge[i][1]
    if bMonth > 12:
        bMonth = bMonth - 12
        bYear = bYear + 1
    bYear = bYear + rAge[i][0]

    return [bYear,bMonth,i]

def user_interface():
    bYear = 1
    while bYear > 0:
        bYear = int(input("\nEnter the year of birth or 0 to exit "))
        if bYear == 0:
            break
        bMonth = 0
        while bMonth < 1 or bMonth > 12:
            bMonth = int(input("Enter the month of birth "))
            if bMonth < 1 or bMonth > 12:
                print("Month has to be between 1 and 12\n")

        results = calcRetirement(bYear, bMonth)

        print ("Your full retirement age is", rAge[results[2]][0], "years and", rAge[results[2]][1], "months.")
        print ("This will be in", rMonth[results[1]-1], "of", results[0])


print("Social Security Full Retirement Age Calculator")
user_interface()
print ("\nFarewell.")
