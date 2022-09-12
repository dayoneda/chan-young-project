try:
    num1,num2=map(int,input("계산하는 숫자를 입력해주세요 ").split())
    num3=round(num1/num2,2)
    print("{}/{}={}입니다".format(num1,num2,num3))
except ValueError:
    print("숫자를 입력해주세요")
except ZeroDivisionError as err:
    print(err)