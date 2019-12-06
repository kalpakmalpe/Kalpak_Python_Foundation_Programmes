#Anonymous Functions 

def demo(n):
    return lambda  a : a * n


double=demo(2)
triple=demo(3)


print(double(4))
print(triple(4))


for a in map(double,[1,2,3,4,5,6]):
    print("double:-",a)


for b in map(triple,[2,3,5,6,78,90]):
    print("Triple:-",b)


