import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36'} 

url = 'https://book.douban.com/subject/'+ input ('请输入书籍号\n') + '/blockquotes'

r = requests.get(url,headers = headers)
soup = BeautifulSoup(r.text,'html.parser')

title = soup.find('div',id="content").find('h1').text
items = soup.find('div',class_="blockquote-list score bottom-line").find('ul').findAll('li')

filename = title + '.txt'
with open(filename,'w',newline='',encoding='utf-8') as file:

    for item in items:
        new_url = item.find('figure').find('a').get('href')
        r = requests.get(new_url,headers = headers)
        soup = BeautifulSoup(r.text,'html.parser')
        contant = soup.find('pre',id = "link-report").find('figure').text
        file.write(contant + "\n\n" + "-------------------------------------------------------------------------------------------------------------------------------\n")

    

