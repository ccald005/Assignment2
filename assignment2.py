import sys
from socket import *
from datetime import datetime

@staticmethod
def checkGoodString(string):
    if (len(string) < 9) or (string.capitalize() == string)\
    or (sum(c.isdigit() for c in string) != 1):
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
        sys.stdout.write("Your age is %d\n" % (current_year - self.year))

    def listAnneversaries(self):
        return list(range(10, (2022-self.year), 10))
    
    def modifyYear(self, n):
        return str(self.year)[:2]*n + str(self.year*n)[::2]


a = Assignment2(2000)
a.tellAge((datetime.now().year)-2)
rv = a.listAnneversaries()
print(rv)

rv = checkGoodString("f1obar0more")
print(rv)
rv = checkGoodString("foobar0more")
print(rv)

# rv = a.modifyYear(5)
# print(rv)

# rv = connectTcp("www.google.com", 80)
# if rv:
#     print("success")
# else:
#     print("fail")

x  = 22//10

print("%d" % x)
