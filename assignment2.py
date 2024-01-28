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