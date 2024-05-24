import requests
from bs4 import BeautifulSoup
import csv

def scrape_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        titles = soup.find_all('h2', class_='title')

        with open('scraped_data.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Title'])

            for title in titles:
                writer.writerow([title.get_text()])
        
        print("Data saved to scraped_data.csv")
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")

url = 'https://example.com/articles'  # Replace with the actual URL
scrape_data(url)