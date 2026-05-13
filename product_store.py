class product:
    count=0
    def __init__(self,name,price):
        self.name=name
        self.price=price
        product.count +=1
    def get_info(self):
        print(f"the price of {self.name} is {self.price}")
    @staticmethod
    def discount(price,discount):
        final_price=price-(discount*price/100)
        print(f"the discounted price is {final_price}")
    @classmethod
    def count(cls):
        print(f"total product in the store is {product.count}")
i1=product("phone",10000)
i2=product("laptop",50000)
i1.get_info()
i2.get_info()
i1.discount(10000,10)
i2.discount(50000,10)



