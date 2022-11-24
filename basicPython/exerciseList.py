# 6번 개수 9개 추가 / 2번 50개로 수정 / 3 ~ 6번까지 출력 / 오름차순 정렬
result = [33, 40, 12, 63, 52]

#1
result.append(9)
print(result)

#2
result[1] = 50
print(result)

#3
print(result[2:6])

#4
result.sort()
print(result)

# 일주일간 턱걸이 횟수를 저장해서 출력
pullUp_list = []
total = 0
for i in range(1,8):
    a = input("{} day pull-up count : ".format(i))
    pullUp_list.append(a)
    total += int(a)

print('Pull-up Average : {}'.format(total/7))
