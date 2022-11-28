# 1. file write
file = open("./basicPython/pkgTest/data.txt", "w", encoding="utf=8") # utf=8은 한글 안깨지게 함
file.write("1. 파일 쓰기")
file.close()

# 2. file append
file = open("./basicPython/pkgTest/data.txt", "a", encoding="utf=8")
file.write("\n2. 파일 추가") # append는 이어 파일이 작성됨 \n으로 줄바꿈 추가
file.close()

# 3. file read
file = open("./basicPython/pkgTest/data.txt", "r", encoding="utf=8")

# 3.1 Read whole contents of the file
data = file.read()
print(data)
file.close()

# 3.2 Read each line of the file.
file = open("./basicPython/pkgTest/data.txt", "r", encoding="utf=8")
while True:
    dataLine = file.readline()
    print(dataLine, end="") # readline이 줄바꿈 문자 추가하여 이를 삭제해줌.
    if dataLine =="": # file의 끝에 공백문자가 나옴
        break
file.close()