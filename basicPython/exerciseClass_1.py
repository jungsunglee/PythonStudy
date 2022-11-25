# Class Example
class Monster:
    def __init__(self, health, attack, speed) -> None:
        self.health = health
        self.attack = attack
        self.speed = speed
    
    def say(self):
        print("I'm a Monster")
    def decrease_health(self,num):
        self.health -= num
    def get_health(self):
        return self.health

goblin = Monster(800, 1200, 300)
wolf = Monster(1500, 200, 350)

goblin.decrease_health(100)
print(goblin.get_health())


# 파이썬에서는 자료형도 class다.
a = 10
b = "문자"
c = True

print(type(a))
print(type(b))
print(type(c))

#문자열 객체의 method list 확인
print(b.__dir__())


# Example of class inheritance
import random as R

class MonsterPar:
    max_num = 1000 # class variable 선언
    def __init__(self, name, health, attack) -> None:
        if MonsterPar.max_num == 0:
            print("Could not generate more monster.")
            
        elif MonsterPar.max_num !=0:
            self.name = name
            self.health = health
            self.attack = attack
            MonsterPar.max_num -= 1 # class variable 사용 시 self를 사용하지 않음 / class 자체의 변수라는 의미

    def move(self):
        print(f"[{self.name}] Move on the ground")

class Wolf(MonsterPar): # Inheritance from Parent Class
    pass

class Shark(MonsterPar):
    def move(self): # Method Overwriting
        print(f"[{self.name}] Swim in the water")

class Dragon(MonsterPar):
    # 생성자 overwriting
    def __init__(self, name, health, attack) -> None:
        super().__init__(name, health, attack) # super()로 parent class를 불러올 수 있고 parent class의 __init__을 상속받음
        self.skill_list = ("Fire", "Tail Attack", "Wind") #skill을 attribute로 받으면 instance 생성 시 계속해서 사용되어 중복됨 / skill은 변하지 않는 값임.

    def move(self): # Method Overwriting
        print(f"[{self.name}] Fly in the sky")

    def skill(self):
        print(f"[{self.name}] Execute skill : {self.skill_list[R.randint(0,2)]}")

wolf = Wolf('Wolf', '200', '200')
wolf.move()

shark = Shark('Shark', '300', '150')
shark.move()

dragon = Dragon('Dragon', '500', '500')
dragon.move()
dragon.skill() 

# Private Variable and method in the class
class varivable_test:
    __privateAttr = "OK"
    def public(self):
        print("Public method")
    def __private(self):
        print("Private method")

    def print__private(self): #private method는 class 내부에서 호출해서 사용 가능
        self.__private()
    def print__privateAttr(self):
        print(self.__privateAttr)

test = varivable_test()
test.public()

test.print__private() # OK
test.__private() # private method는 해당 class안에서만 사용할 수 있음 Error return

test.print__privateAttr() # OK
print(test.__privateAttr) # private attribute는 해당 class안에서만 사용가능 Error return
