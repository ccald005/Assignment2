import sys
from socket import *

class Assignment2:
    def __init__(self, year):
        self.year = year

    def tellAge(self, currentYear):
        sys.stdout.write("Your age is %d\n" % (currentYear - self.year))

    def listAnniversaries(self):
        return list(range(10, (2022-self.year), 10))
    
    def modifyYear(self, n):
        return str(self.year)[:2]*n + str(self.year*n)[::2]
    
    @staticmethod
    def checkGoodString(string):
        count = sum(c.isdigit() for c in string)
        print('\n'+string)
        print("len = %d\nsum = %d\nstring.capitalize() = %s" % (len(string), count, string.capitalize()==string))
        # if (len(string) < 9) or (string.capitalize() == string)\
        # or (sum(c.isdigit() for c in string) != 1):
        #     return False
        # return True
        if (len(string) >= 9) and (string[0].capitalize() != string[0])\
        and (sum(c.isdigit() for c in string) == 1):
            return True
        return False

    @staticmethod
    def connectTcp(host: str, port: int):
        sock = socket(AF_INET, SOCK_STREAM)
        sock.settimeout(3)
        try:
            sock.connect((host, port))
        except error as e:
            return False
        else:
            sock.close()
            return True
        

a = Assignment2(2000)
a.tellAge(2022)
rv = a.listAnniversaries()
print(rv)


rv = Assignment2.checkGoodString("d1obar0more")
print(str(rv)+'\n')
rv = Assignment2.checkGoodString("foobar0more")
print(str(rv)+'\n')


rv = a.modifyYear(5)
print(rv)

# rv = Assignment2.connectTcp('123.123.123.123', 12345)
rv = Assignment2.connectTcp('www.google.com', 80)
if rv:
    print("success")
else:
    print("fail")
