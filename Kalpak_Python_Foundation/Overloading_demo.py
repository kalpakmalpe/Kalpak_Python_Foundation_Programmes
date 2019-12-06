
class point:
    x=0
    y=0

    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __str__(self):
        return"("+str(self.x)+","+str(self.y)+")"


    def __add__(self, other):
        return(self.x+other.x,self.y+other.y)
6

    def __sub__(self, other):
        return(self.x-other.x,self.y-other.y)

    def __mul__(self, other):
        return(self.x*other.x,self.y*other.y)

    def __truediv__(self, other):
        return (self.x / other.x, self.y / other.y)

    def __floordiv__(self, other):
        return (self.x // other.x, self.y // other.y)

    def __mod__(self, other):
        return (self.x % other.x, self.y % other.y)

    def __pow__(self, other):
        return (self.x **other.x, self.y ** other.y)

    def __lt__(self, other):
        return (self.x < other.x, self.y < other.y)

    def __gt__(self, other):
        return (self.x > other.x, self.y > other.y)

    def __le__(self, other):
        return (self.x <= other.x, self.y <= other.y)

    def __ge__(self, other):
        return (self.x >= other.x, self.y >= other.y)

    def __eq__(self, other):
        return (self.x == other.x, self.y == other.y)

    def __ne__(self, other):
        return (self.x != other.x, self.y != other.y)


    def __iadd__(self, other):
        self.x+=other.x
        self.y+=other.y
        return point(self.x,self.y)

    def __isub__(self, other):
        self.x-=other.x
        self.y-=other.y
        return point(self.x,self.y)


    def __imul__(self, other):
        self.x*=other.x
        self.y*=other.y
        return point(self.x,self.y)

    def __itruediv__(self, other):
        self.x/=other.x
        self.y/=other.y
        return point(self.x,self.y)

    def __ifloordiv__(self, other):
        self.x//=other.x
        self.y//=other.y
        return point(self.x,self.y)

    def __imod__(self, other):
        self.x%=other.x
        self.y%=other.y
        return point(self.x,self.y)

    def __ipow__(self, other):
        self.x**=other.x
        self.y**=other.y
        return point(self.x,self.y)

p1=point(2,3)
print(p1)

p2=point(1,1)
print(p2)

print(p1+p2)
print(p1-p2)
print(p1*p2)
print(p1/p2)
print(p1//p2)
print(p1%p2)
print(p1**p2)
print(p1<p2)
print(p1>p2)
print(p1<=p2)
print(p1>=p2)
print(p1==p2)
print(p1!=p2)

s1=point(1,2)
s2=point(2,3)
s2+=s1
print(s2)

w1=point(2,2)
w2=point(3,3)
w2-=w1
print(w2)


w3=point(4,4)
w4=point(5,5)
w3*=w3
print(w4)




