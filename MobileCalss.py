# MobilePhone
# __ini__(self,brand,model,price )
#__repr__ __str__ __eq__
#**etgar __add__ , __gt__
# total price



class MobilePhone():
    def __init__(self,brand, model , price ):
        self.brand=brand
        self.model=model
        self.price=price
    def __repr__(self):
        return f'MobilePhone({self.brand},{self.model},{self.price})'
    def __str__(self):
        return f'phone brand is :{self.brand} and the model is {self.model}'
    def __eq__(self, other):
        return self.brand==other.brand
    def __add__(self, other):
        return self.price +other.price
    def __gt__(self, other):
        return self.price>other.price

iphone=MobilePhone('apple','13 pro max', 5779)
samsung=MobilePhone('samsung','s5', 4522)

