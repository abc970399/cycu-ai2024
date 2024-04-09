import requests
from bs4 import BeautifulSoup

def parse_url(url):
    # Extract date from the url
    date = url[5:9]
    return date

base_url = 'https://scweb.cwa.gov.tw/zh-tw/earthquake/details/'
response = requests.get(base_url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find all sub urls
sub_urls = [a['href'] for a in soup.find_all('a', href=True) if a['href'].startswith(base_url)]

for sub_url in sub_urls:
    date = parse_url(sub_url)
    if date > '0403':
        response = requests.get(sub_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        print(soup.prettify())