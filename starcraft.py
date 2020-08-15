name = "마린"
hp = 40
damage = 5
print("{0} 유닛이 생성되었습니다.".format(name))
print("체력 {0}, 공격력 {1}\n".format(hp, damage))

tank_name = "탱크"
tank_hp = 150
tank_damage = 35
print("{0} 유닛이 생성되었습니다.".format(tank_name))
print("체력 {0}, 공격력 {1}\n".format(tank_hp, tank_damage))

def attack(name, location, damage):
    print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(\
        name, location, damage))
attack(name, "1시", damage)
attack(tank_name, "1시", tank_damage)

class Unit:
    def __init__(self, name, hp, speed): #init은 초기화
        self.name = name
        self.hp = hp
        self.speed = speed
    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
            .format(self.name, location, self.speed))
#if wraith2.clocking == True:
    #print("{0}는 현재 클로킹 상태입니다".format(wraith2.name))

#메소드
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage
    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
            .format(self.name, location, self.damage))
    def damaged(self, damage) :
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))
firebat1 = AttackUnit("파이어뱃", 50, 4, 16) 
firebat1.attack("5시")
firebat1.damaged(50)
marine1 = AttackUnit("마린", 80, 4, 5)
tank1 = AttackUnit("탱크", 150, 3, 15)

class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
            .format(name, location, self.flying_speed))

class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)
        Flyable.__init__(self, flying_speed)
    def move(self, location): #move 새롭게 정의
        print("[공중 유닛 이동]")
        self.fly(self.name, location)
wraith1 = FlyableAttackUnit("레이스", 100, 5, 10)
valkyrie=FlyableAttackUnit("발키리", 200, 6, 5)
valkyrie.fly(valkyrie.name, "3시")
vulture = AttackUnit("벌쳐", 80, 10, 20)
battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

vulture.move("11시")
battlecruiser.move("9시")

class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        super().__init__(name, hp, 0) #self 없이
        self.location = location
        #pass는 그냥 넘어가기 함수가 완성된 것처럼 보이기\

class House:
    def __init__(self, location, house_type, deal_type, price,completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    def show_detail(self):
        print( self.location, self.house_type, self.deal_type, self.price ,self.completion_year )
houses = []
house1 = House("강남", "아파트", "매매", "10억", "2010년")
house2 = House("마포", "오피스텔", "전세", "5억", "2007년")
house3 = House("송파", "빌라", "월세", "500/50", "2000년")

houses.append(house1)
houses.append(house2)
houses.append(house3)

print("총 {0}대의 매물이 있습니다.".format(len(houses)))
for House in houses:
    House.show_detail()
