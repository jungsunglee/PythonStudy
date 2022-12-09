import os.path
import csv
from post import Post
import traceback

dataList = []
dataPath = ".\\basicPython\simpleBlog\data.csv"

if os.path.isfile(dataPath):
    print("\nLoading...")
    with open(dataPath, "r", encoding="utf-8-sig") as f:
        reader = csv.reader(f)
        for i in reader:
            post = Post(int(i[0]), i[1], i[2], int(i[3]))
            dataList.append(post)
else:
    with open(dataPath, "w", newline="",encoding="utf-8-sig") as f:
        pass
        # 이부분에 파일 저장 루틴 추가
#print(dataList[0].getTitle()) #객체 자체를 list에 추가하여 관리

def writePost():
    inTitle = input("Please Input the title\n>>>")
    inContent = input("Please Input the content\n>>>")
    '''if len(dataList)==0:
        inID =  1
    else:
        inID = dataList[len(dataList)-1].getId() +1'''
    if len(dataList)==0:
        inID = 1
    else: 
        inID = dataList[-1].getId()+1 #dataList의 -1은 마지막 객체를 의미함.
    newPost = Post(inID, inTitle, inContent,0)
    dataList.append(newPost)
    print("# Completed posting")
    # file에 저장하지 않고 dataList에 객체를 추가하여 관리
    '''with open(dataPath, "a",newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f)
        writer.writerow([newPost.getId(),newPost.getTitle(),newPost.getContent(),newPost.getHits()])'''

def displayIndex():   
    id_list = [] # id를 list로 관리함.

    if len(dataList)==0:
        print("There is no any post.")
        return None

    while True:
        try:
            refreshData(id_list)
            command = int(input("Please select the Number to show more detail.\n(If you want to go back menu, please Input the -1.)\n>>>"))
        except ValueError as e:
            print("[ERROR] Please Input the number.\n", e, "\n")
        else:
            if command == -1:
                break
            elif command in id_list: # in을 활용해서 해당 list에 있는 번호인지 확인
                detailPost(command)
                break
            else:
                print("There is no the post number in the list\n")

def refreshData(id_list):
    index = ''
    for i in range(len(dataList)):
        index += f"Number : {dataList[i].getId()}\nTitle : {dataList[i].getTitle()}\nHits : {dataList[i].getHits()}\n\n"
        id_list.append(dataList[i].getId())
    print("\n- Index -\n" + index) # Title

def detailPost(command: int):
    for data in dataList: # data 객체(post) 직접 접근 : 중요
        if data.getId() == command:
            data.incresceHits()
            print("\n- View the more datil post -\n") # Title
            print(f"Number : {data.getId()}")
            print(f"Hits : {data.getHits()}")
            print(f"Title : {data.getTitle()}")
            print(f"Content : {data.getContent()}")
            print("\n")
            target_data = data
    while True:
        try:
            modiCommand = int(input("Modify : 1  Delete : 2\n(If you want to go back menu, please Input the -1.)\n>>>"))
            if modiCommand == -1:
                break
            elif modiCommand == 1:
                update_post(target_data)
                break
            elif modiCommand == 2:
                delte_post(target_data)
                break
            else:
                raise Exception("Input value range error.")
        except ValueError as e:
            print("[ERROR] Please Input the number.\n", e, "\n")
        except Exception as e:
            print("[ERROR] Please Input the right number(1, 2, -1)\n", e)

def update_post(target_data): # data 객체를 사용하여 값에 접근
    ModiTitle = input("Please input the title for modification\n>>>")
    ModiContent = input("Please input the content for modification\n>>>")
    oriId = target_data.id
    oriHits = target_data.hits
    target_data.set_post(oriId, ModiTitle, ModiContent, oriHits)
    print("Complete the modification.")

def delte_post(target_data):
    dataList.remove(target_data)
    print("Deleted the Post.")

def save_data(dataList:list):
    with open(dataPath, "w", newline='', encoding="utf-8-sig") as f:
        writer = csv.writer(f)
        for data in dataList:
            raw = [data.id, data.title, data.content, data.hits]
            writer.writerow(raw)
    print("Completed saving data.")

while True:
    try :
        command=int(input("\n- Simple Blog -\n- Please Select Menu -\n1. Write Post\n2. Posts Index\n3. End\n>>>"))
        if command <1 or command >3:
            raise Exception("Input value range error.")
    except ValueError as e:
        traceback.print_exc()
        print("[ERROR] Please Input the number from 1 to 3\n", e)
    except Exception as e:
        traceback.print_exc()
        print("[ERROR] Please Input the right range number from 1 to 3\n", e)
    else: # try문에서 else는 error가 발생하지 않을 때 동작임
        if command == 1:
            print("Write Posts\n")
            writePost()            
        elif command ==2:
            displayIndex()
        elif command ==3:
            save_data(dataList)
            print("Good Bye!!")
            break


