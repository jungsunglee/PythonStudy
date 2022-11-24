# cur_sub >= 1000 -> 수익 창출 가능
cur_sub = int(input("Please input the number of subscribers : "))
if cur_sub >= 1000: print("You could get the income")
else: print("You cound not get the income")

# studyTime >= 10 잠금해제 / 10 > studyTime >= 5 30분 사용 가능 / else 사용 불가
cur_sT = int(input("Please input the study time : "))
if cur_sT >= 10: print("The smart phone is unlocked")
elif cur_sT >= 5: print("You could use the smart phone for 30m")
else: print("You cound not use the smart phone")

# 세과목 평균이 80 이상이면 불합격 / 0 ~ 100 사이 숫자를 입력하지 않으면 "잘못입력하였습니다." 출력
koScore = int(input("Please input the score of korean test : "))
enScore = int(input("Please input the score of English test : "))
maScore = int(input("Please input the score of Mathmatics test : "))
list = [koScore,enScore,maScore]
if all(0<= x <=100 for x in list):
    averageScore = (koScore + enScore + maScore) / 3
    if averageScore >= 80:
        print("Fail")
    else:
        print("Pass")

else: print("Please check the score(0 <= Scroe <= 100")