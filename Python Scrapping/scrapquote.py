import requests
from bs4 import BeautifulSoup
from time import sleep
from csv import DictWriter
from csv import DictReader

def read_quotes(filename):
    with open(filename,"r") as file:
        csv_reader = DictReader(file)
        for item in csv_reader:
            print(item)
read_quotes("quotes.csv")


baseUrl = "http://quotes.toscrape.com/"


def scrapquotes():
    url = "/page/1"
    allQuotes = []
    while url:
        res = requests.get(f"{baseUrl}{url}")
        soup = BeautifulSoup(res.text, "html.parser")
        quotes = soup.find_all(class_="quote")
        for quote in quotes:
            allQuotes.append({
                "text": quote.find("span").get_text(),
                "author": quote.find(class_="author").get_text(),
                "link": quote.find("a")["href"]
            })
        nextBtn = soup.find(class_="next")
        url = nextBtn.find("a")["href"] if nextBtn else None
        # sleep(2)
    return allQuotes


print(scrapquotes())

quotes = scrapquotes()

with open("quotes.csv", "w") as file:
    headers = ["text", "author", "link"]
    csv_writer = DictWriter(file, fieldnames=headers)
    csv_writer.writeheader()
    for quote in quotes:
        # print(quote)
        csv_writer.writerow(quote)
