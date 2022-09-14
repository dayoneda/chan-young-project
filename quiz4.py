class QuantityError(Exception):
    def __init__ (self,msg):
        self.msg=msg
    def __str__(self):
        return self.msg



chicken=10
waiting=1
while(True):
    try:
        order=int(input("주문번호{0}번손님 주문하실 치킨수량을 말해주세요"\
            .format(waiting)))
        if order<1:
            raise ValueError
        elif chicken < order:
            raise QuantityError("재료가 부족합니다")
        else:    
            chicken-=order
            waiting+=1
            print("[남은 수량:{0}마리]".format(chicken))
        if chicken ==0:
            print("솔드아웃!")
            break
    except ValueError:
        print("잘못된 값을 입력하였습니다.")
    except QuantityError as err:
        print(err)