from random import *
cnt = 0
n =int(input("탑승인원: "))
for i in range(1,n): 
    time = randrange(5,59) 
    if 5<=time<=15:
        print("[O] 승차가능(소요시간:{0}분)".format(time))
        cnt+=1
    else:
        print("[ ] 승차불가(소요시간:{0})".format(time))
print("총 탑승가능인원:{}".format(cnt))
