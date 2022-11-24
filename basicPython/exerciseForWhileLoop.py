# multiplication tables
print("Please input the number from 2 to 9 to display a multiplicatiopn table")
num = int(input())

for i in range(1,10):
    if 1 < num < 10:
        print(num, " * ", i, " = ", num*i)
    else:
        print("YOu input the worng number")
        break

# Game menu
while True:
    print("Please select the menu")
    command = int(input("1.Start Game 2.Shwo Ranking 3.End >>> "))
    if command == 1:
        print("Start the Game")
    elif command == 2:
        print("The Realtime Ranking")
    elif command == 3:
        print("End of the Game")
        break
    else:
        print("You input the wrong number")

# Exercis Korean language

ko_list = ['사랑해', '귀엽다', '고마워', '행복해']
wrongAns = 0
for correct in ko_list:
    print("Please type this word {}".format(correct))
    answer = input("Please input the upper word : ")
    if correct!=answer:
        wrongAns += 1
print("Total question : {}".format(len(ko_list)))
print("Correct answer : {}".format(len(ko_list)-wrongAns))
print("Incorrent answer : {}".format(wrongAns))


