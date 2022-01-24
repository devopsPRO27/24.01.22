import math

class Point():
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __str__(self):
        return f'the point axis is :x={self.x} , {self.y}'
    def __repr__(self):
        return f'Point({self.x},{self.y})'
    def getDes(self):
        d=math.sqrt(self.x**2+self.y**2)
        return d
        #return sqrt(self.x**2+self.y**2)
    def __eq__(self, other):
        if self.x==other.x :
            return True
        return False
    def __gt__(self, other):
        if self.y >= other.y and self.x>other.x:
            return True
        return False
    def __add__(self, other):
        x1=self.x+other.x
        y1=self.y+other.y
        return Point(x1,y1)


p1=Point(4,8)
p2=Point(5.19,-1.18)
p3=Point(4,12)
p4=Point(4,7)
print(p1)
print(p2)
print(p3)
print(p4)
print(p1>p3)
print(p1==p2)
p5=p1+p4
print(p5)

#print(p1.__repr__(),'--------',p2.__repr__())
#print(p1.getDes())
#print(p2.getDes())
