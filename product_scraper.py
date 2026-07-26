import re
import requests
from bs4 import BeautifulSoup
import os

GBP_TO_INR = 107
TARGET_PRICE = 2000  # in INR

URLS = [
    "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html",
    "https://books.toscrape.com/catalogue/sharp-objects_997/index.html",
    "https://books.toscrape.com/catalogue/tipping-the-velvet_999/index.html",
]

os.makedirs("images", exist_ok=True)

for url in URLS:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    title = soup.find("h1").text.strip()
    price_gbp = float(re.sub(r"[^\d.]", "", soup.find("p", class_="price_color").text))
    price = round(price_gbp * GBP_TO_INR, 2)
    img_url = "https://books.toscrape.com/" + soup.find("img")["src"].replace("../../", "")

    # Download image
    img_data = requests.get(img_url).content
    with open(f"images/{title[:30]}.jpg", "wb") as f:
        f.write(img_data)

    # Price comparison
    status = "Within budget" if price <= TARGET_PRICE else "Over budget"

    print(f"Title : {title}")
    print(f"Price : Rs. {price:.2f}")
    print(f"Image : {img_url}")
    print(f"Status: {status} (Target: Rs. {TARGET_PRICE})")
    print("-" * 
