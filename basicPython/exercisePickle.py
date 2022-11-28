# 1. 파이썬 객체 pickle로 저장하기
import pickle

data = {
    "목표1" : "매일 운동",
    "목표2" : "매일 공부"
}

file = open("data.pickle", "wb") # wb : writer binary
pickle.dump(data, file) # dump함수 호출해서 data객체를 file 형식으로 저장함.
file.close()

# 2. pickle 파일 파이썬으로 가져오기
file = open("data.pickle", "rb")
data = pickle.load(file)
print(data)
file.close()