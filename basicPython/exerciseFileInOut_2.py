import csv

readData = []
data = [
    ['종목', '매입가', '수량', '목표가'],
    ['삼성전자', 85000, 10, 90000],
    ['네이버', 380000, 5, 400000]
]
with open('mystock.csv','w',newline='',encoding='utf-8-sig') as f:
    wr=csv.writer(f)
    for i in data:
        wr.writerow(i)

with open('mystock.csv','r',encoding='utf-8-sig') as f:
    r = csv.reader(f)
    index = 0
    for i in r:
        rawList = []
        if index == 0:
            readData.append(i)
            index += 1
        else:
            rawList.append(i[0]) # list 값을 일부분만  int형으로 변경
            rawList += list(map(int, i[1:4])) 
            readData.append(rawList) 


for i in range(1,3):
    profits = (readData[i][3] - readData[i][1]) * readData[i][2]
    profitRate =((readData[i][3]/readData[i][1])-1) * 100
    print(f'{readData[i][0]} {profits} {profitRate: .2f}%')