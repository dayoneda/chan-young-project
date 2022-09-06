class House:
    def __init__(self,location,house_type,deal_type,price,completion_year):
        self.location=location
        self.house_type=house_type
        self.deal_type=deal_type
        self.price=price
        self.completion_year=completion_year

    def show_detail(self):
        print((self.location,self.house_type,\
            self.deal_type,self.price,self.completion_year))

house_list=[]
house1=House("강남","아파트","매매","10억","2010년")
house2=House("마포","오피스텔","전세","5억","2007년")
house3=House("송파","빌라","월세","500/50","2000년")

house_list.append(house1)
house_list.append(house2)
house_list.append(house3)

print("총{0}대의 매물이 있습니다".format(len(house_list)))
for house in house_list:
    house.show_detail()
