'''
Have the function SimplePassword(str) take the str parameter being passed and determine if it passes as a valid password that follows the list of constraints:

1. It must have a capital letter. ok
2. It must contain at least one number. ok
3. It must contain a punctuation mark or mathematical symbol. ok
4. It cannot have the word "password" in the string.
5. It must be longer than 7 characters and shorter than 31 characters. ok

If all the above constraints are met within the string, the your program should return the string true, otherwise your program should return the string false. For example: if str is "apple!M7" then your program should return "true".
'''
import string
"test"

def SimplePassword(strParam):
    rePunc = reCapital = reNum = reLen = rePass = False
    for i in strParam:
        if i in string.punctuation:
            rePunc=True
        if i.isupper():
            reCapital=True
        if i.isdigit():
            reNum=True
    if strParam.lower().find("password"):
        rePass=True

    if 7 < len(strParam) < 31:
        reLen=True

    print(rePunc, reCapital, reNum, rePass, reLen)

    if ((rePunc == True)&(reCapital == True)&(reNum == True)&(rePass==True)&(reLen==True)):
        strParam = "true"
    else:
        strParam = "false"
    return strParam

print(SimplePassword(input()))