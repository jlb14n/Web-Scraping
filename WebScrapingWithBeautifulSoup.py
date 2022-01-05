from bs4 import BeautifulSoup
import requests

def getHTML(url):
    response = requests.get(url)
    return response.text

books=[]
for i in range(1,51):
    try:   
        html = getHTML("http://books.toscrape.com/catalogue/page-{0}.html".format(i))
        soup = BeautifulSoup(html,'html.parser')
        for item in soup.find_all('li',attrs={'class':"col-xs-6 col-sm-4 col-md-3 col-lg-3"}):
            book={}
            book['title']=item.find('h3').find('a').attrs['title']
            book['price']=item.find('p',attrs={'class':'price_color'}).get_text()[2:]
            book['rating']=item.find('p',attrs={'class':'star-rating'}).attrs['class'][1]
            books.append(book)
    except:
        continue

with open('BooksToScrape.csv','w', encoding="utf-8") as file:
    file.write('title,price[£],rating\n')
    for book in books:
        file.write('"{0}",{1},{2}\n'.format(book['title'],book['price'],book['rating']))
