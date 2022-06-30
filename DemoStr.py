# DemoStr.py

from base64 import standard_b64decode
from unittest import result


print('c:\work\test.txt')
print('c:\\work\\test.txt')
print('c:/work/test.txt')
#raw string notation(가공하지 않은 문자열 표기법)
print(r'c:\work\test.txt')

#자동으로 문자열 생성
names=['이순신','전우치','박문수']
for name in names:
    print('안녕하세요. {0}님 다운 이름입니다'.format(name))
    print('='*40)

#str클래스의 메서드
#print(dir(str))
strA='python is very powerful'
strB='파이썬은 강력해'
print(len(strA))
print(len(strB))
print(strA.capitalize())
print('----')
print(strA.count("p"))
print(strA.count("p",7))
print("demo.ppt".endswith('ppt'))
print('MBC:2580'.isalnum())
print('2580'.isalnum())

strData='<<<< spam and han >>>'
result=strData.strip('<> ')
print(strData)
print(result)
result=result.replace('spam','spam agg')
print(result)
lst=result.split()
print(lst)
print('---다시 원래대로 복구---')
print(':'.join(lst))