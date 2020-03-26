import requests
from bs4 import BeautifulSoup
from csv import writer

response = requests.get('https://webscraper.io/test-sites/e-commerce/allinone')

soup = BeautifulSoup(response.text, 'html.parser')

posts = soup.find_all(class_='col-sm-4')

with open('post.csv', 'a') as csv_files:
    csv_writer = writer(csv_files)
    headers = ['Title', 'Links', 'Price']
    csv_writer.writerow(headers)

    for post in posts: 
        title = post.find(class_='title').get_text().replace('\n', '')
        link = post.find('a')['href']
        price = post.select('.price')[0].get_text()
        csv_writer.writerow([title, link, price])
       

