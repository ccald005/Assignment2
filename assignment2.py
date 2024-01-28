import sys
from socket import *
from datetime import datetime

@staticmethod
def checkGoodString(string):
    count = sum(c.isdigit() for c in string)
    if (len(string) < 9) or (string.capitalize() == string)\
    or (count != 1):
        return False
    return True

@staticmethod
def connectTcp(host: str, port: int):
    sock = socket(AF_INET, SOCK_STREAM)
    try:
        sock.connect((host, port))
    except socket.error as e:
        return False
    else:
        sock.close()
        return True

class Assignment2:
    def __init__(self, year):
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
        return str(self.year)[:2]*n + str(self.year*n)[::2]


a = Assignment2(2000)
a.tellAge(datetime.now().year)
rv = a.listAnneversaries()
print(rv)
rv = checkGoodString("f1obar0more")
print(rv)
rv = checkGoodString("foobar0more")
print(rv)

rv = a.modifyYear(5)
print(rv)

rv = connectTcp("www.google.com", 80)
if rv:
    print("success")
else:
    print("fail")
