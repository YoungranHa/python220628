#  web2.py
#웹클롤링을 위한 선언
from bs4 import BeautifulSoup
#웹서버에 요청
import urllib.request

# 파일로 저장
f=open('c:\\work\\webtoon.txt','wt',encoding='utf-8')
for i in range(1,6):
    url='https://comic.naver.com/webtoon/list?titleId=20853&weekday=fri&page='+str(i)

    print(url)

    data=urllib.request.urlopen(url)
    soup=BeautifulSoup(data,'html.parser')

    cartoons=soup.find_all('td',class_='title')

    for item in cartoons:
        title=item.find('a').text
        print(title.strip()+'\n')
        f.write(title.strip()+'\n')
f.close
print('--웹 크롤링 종료---')