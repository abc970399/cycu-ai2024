import requests
from bs4 import BeautifulSoup

url = 'https://scweb.cwa.gov.tw/zh-tw/earthquake/details/2024040307580972019'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

# Find the element that contains "發震時間"
element = soup.find(lambda tag: '發震時間' in tag.text)

# Find the next siblings of the element
next_elements = element.find_next_siblings()

# Print the text of each element
for next_element in next_elements:
    print(next_element.text.strip())