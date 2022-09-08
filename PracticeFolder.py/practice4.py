
def cpoint(gun,soldiers):
    gun=gun-soldiers
    print("남은 현재총은 {0}정입니다".format(gun))
    #return gun
gun=10    
soldiers=int(input("경계인원수를 입력해주세요 "))
if gun<soldiers:
    print("총기가 모자릅니다 상부인원에게 보고바람")
else:
    cpoint(gun,soldiers)
 
