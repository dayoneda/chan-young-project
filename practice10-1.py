class BigNumberError(Exception):
    def __init__(self,msg):
        self.msg=msg
    def __str__(self):
        return self.msg

try:
    print("한 자리수 전용계산기입니다")
    num1,num2=map(int,input("값을 입력해주세요 ").split())
    if num1>=10 or num2>=10:
        raise BigNumberError("입력값:{0},{1}".format\
            (num1,num2))
    print("{1}/{2}={3}입니다".format(num1,num2,num1/num2))
    
except ValueError:
    print("잘못된 값을 입력하였습니다")
except BigNumberError as err:
    print("에러가 발생하였습니다")
    print(err)
finally:
    print("이용해주셔서 감사합니다")