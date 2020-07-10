#https://www.rithmschool.com/blog
import requests
from bs4 import BeautifulSoup
from csv import writer

response = requests.get("https://www.rithmschool.com/blog")
soup = BeautifulSoup(response.text,"html.parser")
articles = soup.find_all("article")

with open("blog_data.csv","w") as csv_file:
    csv_writer = writer(csv_file)
    csv_writer.writerow(["title", "link", "date"])
    # print(articles)
    for article in articles:
        aTag =article.find("a")
        title = aTag.get_text()
        url = aTag["href"]
        date = article.find("time")["datetime"]
        csv_writer.writerow([title, url, date])