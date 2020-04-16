import requests, csv, json
from bs4 import BeautifulSoup
from csv import writer

response = requests.get('https://webscraper.io/test-sites/e-commerce/allinone')

soup = BeautifulSoup(response.text, 'html.parser')

posts = soup.find_all(class_='col-sm-4')

with open('post.csv', 'a') as csv_files:
    csv_writer = writer(csv_files)
    headers = ['Id', 'Title', 'Links', 'Price']
    csv_writer.writerow(headers)

    index = 1
    for post in posts:
        id = index
        title = post.find(class_='title').get_text().replace('\n', '')
        link = post.find('a')['href']
        price = post.select('.price')[0].get_text()
        csv_writer.writerow([id, title, link, price])
        index += 1
       
# converting the csv data to json
csvFilePath = 'post.csv'
jsonFilePath = 'post.json'

data = {}
with open(csvFilePath) as csvFile:
    csvReader = csv.DictReader(csvFile)
    csvReader = list(csvReader)
    for rows in range(0, len(csvReader)):
        id = rows
        data[id] = csvReader[rows]

with open('jsonFilePath', 'a') as jsonFile:
    jsonFile.write(json.dumps(data, indent=4))


