import requests
from bs4 import BeautifulSoup
import csv

class data:
    def __init__(self,title,author,score,number):
        self.title = title
        self.author = author
        self.score = score
        self.number = number
    def back(self):
        total = "《" + self.title + "》" + '/'+ self.author +' 评分:'+ self.score + "   书名号:" + self.number
        return str(total)

def web_rejust(i):
    url = 'https://book.douban.com/top250?start='+str(i*25)
    return url

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36'}

books = []

for i in range(0,10):
    r = requests.get(web_rejust(i),headers = headers)
    soup = BeautifulSoup(r.text,'html.parser')
    items = soup.findAll('table',width="100%")
    for item in items:
        title = item.find_all('a')[1].get('title')
        author = item.find('p').text
        score = item.find('span',{"class":"rating_nums"}).text
        number = item.find('a').get('href')[32:39]
        book = data(title,author,score,number)
        books.append(book)

file = '豆瓣书籍top250.txt'
with open(file,'w',newline='',encoding='utf-8') as f:
    i=1
    for each in books:
        f.write("NO."+str(i)+"  ")
        f.write(each.back())
        f.write("\n")
        f.write("--------------------------------------------------------------------------\n")
        i = i+1