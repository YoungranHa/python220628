# functiuon2.py

def swap(x,y):
    return y,x


result=swap(5,6)
print(result)

def intersect(prelist, postlist):
    result=[]
    for x in prelist:
        if x in postlist and x not in result:
            result.append(x)
    return result

print(intersect("HAM","SPAM"))
