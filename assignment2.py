import sys
from datetime import datetime

@staticmethod
def checkGoodString(string):
    count = sum(c.isdigit() for c in string)
    if (len(string) < 9) or (string.capitalize() == string)\
    or (count != 1):
        return False
    return True

@staticmethod
def connectTcp(host, type):
    return None

class Assignment2:
    def __init__(self, year) -> None:
        self.year = year

    def tellAge(self, current_year):
        print("Your age is %d" % (current_year - self.year))
        # sys.stdout.write("Hello %s\n" (self.year))

    def listAnneversaries(self):
        list = []
        x = self.year
        n = 0
        current = 2021
        while (current - x) >= 10:
            n += 10
            list.append(n)
            x+=10
        return list
    
    def modifyYear(self, n):
        rv = self.year
        return "hello"


a = Assignment2(1991)
a.tellAge(datetime.now().year)
rv = a.listAnneversaries()
print(rv)
rv = checkGoodString("f1obar0more")
print(rv)
rv = checkGoodString("foobar0more")
print(rv)

