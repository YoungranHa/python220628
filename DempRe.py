#DempRe.py
import re

result=re.search('[0-9]*th','    35th')
#매칭 오브젝트가 리턴
print(result)
print(result.group())

#블럭 주석 처리 :crtl+/
# result=re.match('[0-9]*th','    35th')
# print(result)
# print(result.group())

print(bool(re.search('apple','this is apple')))
print(bool(re.match('apple','this is apple')))

#연도를 찾는
result=re.search('\dd'올해 우리는 2022년')
print(result.group())

r