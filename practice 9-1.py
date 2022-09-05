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
magician=AttackUnit("magician",200,9999)
magician.attack(1)
magician.damaged(40)
magician.damaged(500)