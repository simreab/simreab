import requests, bs4
'''
#get title of every book with 2 star rating
base_num = 1
base_url = 'https://books.toscrape.com/catalogue/page-{}.html'

res = requests.get(base_url.format(1))
soup = bs4.BeautifulSoup(res.text, 'lxml')

products = (soup.select('.product_pod'))

example = products[0]

print([] == example.select(".star-rating.Two"))
print(example.select("a")[1]['title'])

two_star_titles = []

for n in range(1, 51):
    scrape_url = base_url.format(n)
    res = requests.get(scrape_url)

    soup = bs4.BeautifulSoup(res.text, 'lxml')
    books = soup.select(".product_pod")

    for book in books:
        if len(book.select(".star-rating.Two")) != 0:
            book_title = book.select("a")[1]['title']
            two_star_titles.append(book_title)
            
if len(two_star_titles) != 0:
    print(*two_star_titles, sep = "\n")
else:
    print('List Empty')'''


base_url = 'http://quotes.toscrape.com/page/{}/'
res = requests.get(base_url.format(1))
soup = bs4.BeautifulSoup(res.text, 'lxml')

authors = set()
for name in soup.select('.author'):
    authors.add(name.text)
print(authors)
print('\n')

quotes = []
for quote in soup.select('.text'):
    quotes.append(quote.text)
print(quotes)

for n in range(0, len(soup.select('.tag-item'))):
    print(soup.select('.tag-item')[n].text)

unique_authors = []
for n in range(0, 10):
    pages = requests.get(base_url.format(1))
    soup = bs4.BeautifulSoup(pages.text, 'lxml')
    
    for name in soup.select('.author'):
        unique_authors.append(name.text)
        
print(tuple(unique_authors))
print('\n')
    
