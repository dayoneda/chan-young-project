class Unit:
    def __init__(self,name,hp,):
        self.name=name
        self.hp=hp
        
class AttackUnit(Unit):
    def __init__(self,name,hp,damage):
        Unit.__init__(self,name,hp)
        self.damage=damage
    def attack(self,location):
        print("{0}유닛이 {1}시 지점을 공격중입니다".format(self.name,location))
    def damaged(self,damaged):
        print("{}유닛이 데미지{}을 받았습니다".format(self.name,damaged))
        self.hp-=damaged
        if self.hp<=0:
            print("{0}유닛이 파괴되었습니다".format(self.name))
class flyable:
    def __init__(self,flying_speed):
        self.flying_speed=flying_speed
    def fly(self,name,location):
        print("{0}유닛이 {1}방향으로 이동중입니다 이동속도:{2}"\
            .format(name,location,self.flying_speed))    

class flyableAttackUnit(AttackUnit,flyable):
    def __init__(self,name,hp,damage,flying_speed):
        AttackUnit.__init__(self,name,hp,damage)
        flyable.__init__(self,flying_speed)


valkyrie=flyableAttackUnit("발키리",250,12,25)
valkyrie.attack(2)
valkyrie.fly("발키리",2)