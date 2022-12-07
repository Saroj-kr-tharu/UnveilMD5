# program to crack password or hash with online dictionary
from os import system
from urllib.request import urlopen
import hashlib

class cracking:
    def __init__(self):
        self.link=""" https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt """
        self.hash=""

    def raw_data(self):
        system("cls")
        self.hash = input("\t\t Enter a hash Value -----> ")
        self.processing_data()

    def processing_data(self):
        passlist = str(urlopen(self.link).read(), 'utf-8')
        i=0
        for password in passlist.split("\n"):
            i+=1
            hashguess = hashlib.md5(bytes(password, "utf-8")).hexdigest()
            if hashguess == hash:
                print("\n\n\t\t\t\t <------ The password is  " +str(password)+" -------->")
                print("\t\t\t\t  Total Test Password ------>  " +str(i))
                quit()
            else:
                print("\t\t\t\t <------- Password guess " + str(password) + " does not match, trying next --------> ")

        print("\n\n\t\t\t\t  <----- Password not in passwordlist -----> ")
        print("\t\t\t\t  Total Test Password ------>  " +str(i))

if __name__=="__main__":
    ch=cracking()
    ch.raw_data()
    