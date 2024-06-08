from io import UnsupportedOperation
import random
import sys

passLen = int(input("Enter your password length: "))

chars = "abcdefghijklmnopqrstvwxyz1234567890ABCDEFGHIJKLMNOPQRSTVWXYZ"
password = ''

if passLen > 25:
    print("Not 2 much bro :d, make lenght <= 25")
    sys.exit()
else:
    for x in range(passLen):
        password += random.choice(chars)
   
print("Your generated password: ", password)

passName = str(input("Enter your password's name: "))
f = open('passwords.txt','a')
try:
    f.write("\n")
    f.write("Your password for ")
    f.write(passName)
    f.write(" is: ")
    f.write(password)
except UnsupportedOperation as err1:
    print(err1)
    