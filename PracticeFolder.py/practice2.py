def deposit(balance,money):
    print("금액이 입금되었으며 현재금액은{}원 입니다".format(balance+money))
    return balance+money
balance = 0 #고객의 데이터 값 
money =int(input("입금하실 금액을 입력해주세요 "))
balance = deposit(balance,money)
print(balance)

