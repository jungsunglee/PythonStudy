# 세정수 합계 평균 출력

def printSumAvg(x,y,z):
    '''
    Caluculate the sum and average of 3 integers.
    '''
    sum = x+y+z
    print("SUM :", sum, "Average :", sum/3)
    print(f"SUM : {sum} Average : {sum/3}")

printSumAvg(10,20,30)

# Lotto Number
import random as R

def getRandomNumber():
    '''
    Display random number from 1 to 45
    '''
    lotto_re = []
    count = 0
    while count != 7:
        dupulicate = False    
        number = R.randint(1,45)
        for x in lotto_re:
            if x == str(number): 
                dupulicate = True
        if dupulicate == False:
            lotto_re.append(str(number))
            count+=1

    number = ' '.join(lotto_re)
    return number

def getRandomNumber_v2():
    '''
    Display random number from 1 to 45
    '''
    lotto_re = []
    count = 0
    while count != 7:
        number = R.randint(1,45)
        if number not in lotto_re:
            lotto_re.append(str(number))
            count+=1

    number = ' '.join(lotto_re)
    return number

for i in range(20):
    print(getRandomNumber_v2())
