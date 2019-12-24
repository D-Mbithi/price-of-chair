import requests
from bs4 import BeautifulSoup as bs


url = "https://www.johnlewis.com/house-by-john-lewis-hinton-office-chair/black/p4201464"

request = requests.get(url)
content = request.content
soup = bs(content, "html.parser")
price_string = soup.find('p', {"class": "price price--large"}).text

price_string.strip()

price_with_simple = price_string[1:]

price = float(price_with_simple)

if price >= 130:
    print("Price is high.")
else:
    print("You can buy that one.")
    print(f"The current price is {price_with_simple}.")
