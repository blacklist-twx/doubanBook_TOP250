import requests
from bs4 import BeautifulSoup

"""获取书籍排行信息"""
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36'} 
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
        print(book.back())

while(1):
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
    
    print("获取成功，已保存在当前文件夹啦~")

    

