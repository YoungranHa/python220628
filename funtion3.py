# funtion3.py
#함수정의

from imghdr import tests


x=2
def func1(a):
    return a+x

print(func1(1))

def func2(a):
    x=5
    return a+x

print(func2(1))


print("---불변형식---")
a=1.2
print(id(a))
a=2.3
print(id(a))

print("---가벼형식---")
lst=[1,2,3]
print(id(lst))
lst.append(4)
print(id(lst))

g=1
def testScope(a):
    #global g
    g=2
    return g+a

print(testScope(1))
print("전역변후 g:",g)