import requests
from bs4 import BeautifulSoup
import csv

def scrape_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        books = soup.find_all('article', class_='product_pod')

        with open('scraped_books.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Title', 'Price'])

            for book in books:
                title = book.h3.a['title']
                price = book.find('p', class_='price_color').text
                writer.writerow([title, price])
        
        print("Data saved to scraped_books.csv")
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")

url = 'http://books.toscrape.com'
scrape_data(url)