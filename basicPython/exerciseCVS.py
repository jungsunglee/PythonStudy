import csv

# csv file 생성
data = [
    ["이름", "반", "번호"],
    ["재석", 1, 20],
    ["홍철", 3, 18]
]

file = open("student.csv", "w", newline="", encoding="utf-8-sig") 
# newline="" : 윈도우로 csv file 생성시 자동으로 한줄 띄우는 것을 방지
# encoding="utf-8-sig" : 윈도우에서 파일 깨지는 것을 방지
writer = csv.writer(file)

for i in data:
    writer.writerow(i) # writerow method로 한줄 씩 저장

file.close()


# csv file 읽기
file = open("student.csv", "r", encoding="utf-8-sig")
reader = csv.reader(file)
for data in reader:
    print(data)
file.close()