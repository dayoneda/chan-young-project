


class FourCal:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    
    def add(self):
        return self.a + self.b    
    def sub(self):
        return self.a - self.b
    def mul(self):
        return self.a * self.b
    def div(self):
        return self.a / self.b 
a=FourCal(4,2)
print(a.add())
print(a.sub())

class MoreFourcal(FourCal):
    def pow(self):
        return self.a ** self.b

a=MoreFourcal(4,2)

print(a.pow())

class over(FourCal):
    def div(self):
        if self.b ==0:
           return 0
        else:
            return self.a / self.b 


        

