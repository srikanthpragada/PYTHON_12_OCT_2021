import requests
from bs4 import BeautifulSoup

with open("books.xml", "rt") as file:
    bs = BeautifulSoup(file.read(), "lxml-xml")
    books = bs.find_all("book")
    for book in books:
        print(book.title.text)
        print(book.author.text)
        print('-' * 50)

