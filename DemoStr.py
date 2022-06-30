# DemoStr.py

print('c:\work\test.txt')
print('c:\\work\\test.txt')
print('c:/work/test.txt')
#raw string notation(가공하지 않은 문자열 표기법)
print(r'c:\work\test.txt')

#자동으로 문자열 생성
names=['이순신','전우치','박문수']
for name in names:
    print('안녕하세요. {0}님 다운 이름입니다',format(name))
    print('='*40)