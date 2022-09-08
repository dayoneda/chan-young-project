
#gender=input("당신의 성별을 입력해주세요 ")
#height=int(input("당신의 키를 입력해주세요 cm"))
#if gender=="남자":
#    print("당신의 표준체중은 {0}kg입니다".format(height*height*22))
#elif gender=="여자":
#     print("당신의 표준체중은 {0}kg입니다".format(height*height*21))

def std_weight(height,gender):
    if gender =="남자":
        return height * height * 22 
    elif gender =="여자":
        return height*height*21
    
gender=input("성별을 입력해주세요 ")
height=int(input("키를 입력해주세요 "))
weight=round(std_weight(height/100,gender),2)
print("당신의 표준몸무게는 {}kg입니다".format(weight))