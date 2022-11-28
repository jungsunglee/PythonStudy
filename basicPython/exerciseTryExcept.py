# 원화 환률 -> 달러

won = input("Input the KRW : ")
dollar = input("Input rate of dollar exchange : ")

try :
    print(f"{int(won)/int(dollar): .2f} USD")
except ValueError as e: # 문자열 입력 시 발생하는 ERROR 지정
    # as 로 error을 지정한 후 출력하면 발생하는 error msg. 출력 가능
    print("\nThere is a string ERROR", e)
except ZeroDivisionError as e: # 0으로 나눌 시 발생하는 ERROR 지정
    print("\nThere is a ZeroDivisionERROR", e)
else:
    print("Everything is OK")
finally:
    print("Good bye")