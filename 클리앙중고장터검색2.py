# coding:utf-8
from turtle import title
from bs4 import BeautifulSoup
import urllib.request
import re 

#User-Agent를 조작하는 경우(아이폰에서 사용하는 사파리 브라우져의 헤더) 
hdr = {'User-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/603.1.23 (KHTML, like Gecko) Version/10.0 Mobile/14E5239e Safari/602.1'}

for n in range(1,11):
        #뽐뿌의 휴대폰 게시판
        data ='https://www.ppomppu.co.kr/zboard/zboard.php?id=ppomppu2&divpage=10&page=' + str(n)
        print(data)
        #웹브라우져 헤더 추가 
        req = urllib.request.Request(data, \
                                    headers = hdr)

        data = urllib.request.urlopen(req).read()
        page = data.decode('utf-8', 'ignore')
        soup = BeautifulSoup(page, 'html.parser')

        #  <td valign='middle'>
        #   <a href='zboard.php?id=sponsor&no=87518&sn=on&ss=off&sc=off&search_type=name&keyword=%C6%F9%BF%C1%BC%C7'>[SK/KT/LG]["번이/기변/최대할인"][할부/현완]["아이폰12
        
        list = soup.find_all('td', attrs={'valign':'middle'})

        for item in list:
                try:
                        title=item.find('a').txt
                        print(title.strip())
                        # if (re.search('아이폰', title)):
                        #         print(title.strip())
                        #         print('https://www.clien.net'  + item['href'])
                except:
                        pass
        
