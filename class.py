

class Computer():

    # func
    def __init__(self,color,make,speed,storage):
        self.color=color
        self.make=make
        self.speed=speed
        self.storage=storage

    def turnOn(self):
        print(f'{self.make} is on ')
    def turnOff(self):
        print(f'{self.make} is off ')
    def __repr__(self): #DEV
        return f'Computer({self.color},{self.make},{self.speed},{self.storage})'
    def __str__(self): # print
        return f'Computer color = {self.color} , make = {self.make} , speed={self.speed} , storage = {self.storage}'


#x=computer()# var
#x=Computers() #obj
asus=Computer('red','asus',2.4,512) # __init__(self)
macbook=Computer('black','macbook',3.6,1024) # self macbook obj

print(macbook.__repr__())
print(macbook)



#hodipc=Computer('black','mackbook',3.6,1024)
#print(macbook.make)
#print(asus.color)
#print(macbook.make)
#asus.color='red'
#asus.speed=2.4
#macbook.speed=3.6
#macbook.color='black'
#asus.turnOn()
#asus.turnOff()

# del asus # to delete obj

