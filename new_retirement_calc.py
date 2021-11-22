# James Diller
# 2021FA.CSC.256.0001
# Unit 14 - Retirement Behavioral Test (Unit 14)
# 2021/11/21

#Rewritten so I can use Gherkin easier

rYear = [1960, 1959, 1958, 1957, 1956, 1955, 1943, 1942, 1941, 1940, 1939, 1938, 1937]
rAge = [[67,0],[66,10],[66,8],[66,6],[66,4],[66,2],[66,0],[65,10],[65,8],[65,6],[65,4],[65,2],[65,0]]
rMonth = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

class retiree():
    def __init__(self):
        self.birth_year = 0
        self.birth_month = 0

    def set_birthdate(self, birth_year, birth_month):
        self.birth_year = birth_year
        self.birth_month = birth_month

    def age(self):
        for i in range(len(rYear)):
            if self.birth_year >= rYear[i]:
                break
        return rAge[i]

    def date(self):
        retire_age = self.age()
        retire_month = self.birth_month + retire_age[1]
        retire_year = self.birth_year + retire_age[0]
        if retire_month > 12:
            retire_month = retire_month - 12
            retire_year = retire_year - 1

        return [retire_year, retire_month]
"""
def user_interface():
    while True:
        bYear = int(input("\nEnter the year of birth or 0 to exit "))
        if bYear == 0:
            break
        bMonth = 0
        while bMonth < 1 or bMonth > 12:
            bMonth = int(input("Enter the month of birth "))
            if bMonth < 1 or bMonth > 12:
                print("Month has to be between 1 and 12\n")

        smuck = retiree()
        smuck.set_birthdate(bYear, bMonth)
        r_age = smuck.age()
        r_date = smuck.date()

        print ("Your full retirement age is", r_age[0], "years and", r_age[1], "months.")
        print ("This will be in", rMonth[(r_date[1]-1)], "of", r_date[0])

print("Social Security Full Retirement Age Calculator")
user_interface()
print ("\nFarewell.")
"""
