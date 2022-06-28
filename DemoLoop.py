# DemoLoop.py

import itertools


value=5
while value > 0:
    print(value)
    value-=1

print("---for in---")
lst=[100,"apple", 3.14]
for item in lst:
    print(lst,type(item))

#사전식구조(dict)
d={"apple":100,"orange":200,"kiwi":300}
for k,v in d.items():
    print(k,v)

#구구단 출력
for x in [2,3,4,5,6]:
    print("----{0}단----".format(x))
    for y in [1,2,3,4,5,6,7,8,9]:
        print("{0}*{1}={2}".format(x,y,x*y))


print("---삼격형출력---")
for x in [1,2,3,4,5,6,7,8,9,10]:
    print("*" * x)

print("---braek---")
lst=[1,2,3,4,5,6,7,8,9,10]
for i in lst:
    if i>5:
        break
    print("Item:{0}".format(i))

print("---countinue---")
lst=[1,2,3,4,5,6,7,8,9,10]
for i in lst:
    if i%2:
        continue
    print("Item:{0}".format(i))

print("---range()---")
print(list(range(10)))
print(list(range(1,11)))
print(list(range(2000,2023)))



for i in range(5):
    print(i)

print("---리스트 컴프리현션---")
lst=list(range(1,11))
print([i**2 for i in lst if i>5])


tp=("apple","orange","kiwi")
print([len(i) for i in tp])
d={100:"apple", 200:"orange"}
print([v.upper() for v in d.values()])


print("---피러링---")
lst=[10,25,30]
iterL=filter(None, lst)
for i in iterL:
        print(i)

#함수를 정의
def getBiggerThan20(i):
        return i > 20

iterL = filter(getBiggerThan20, lst)
for i in iterL:
    print(i)

