import re
import sys
import time
import requests
from bs4 import BeautifulSoup

# Fix Windows terminal encoding for special characters
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# ── Settings ──────────────────────────────────────────────────────────────────

URL = "https://www.amazon.in/s?k=iphone"
TARGET_PRICE = 80000  # budget in INR

# Browser-like headers (required – Amazon blocks plain requests without them)
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:126.0) Gecko/20100101 Firefox/126.0",
    "Accept-Language": "en-IN,en;q=0.5",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Connection": "keep-alive",
}

# ── Scrape Amazon ─────────────────────────────────────────────────────────────

session = requests.Session()

# Step 1: visit homepage first (avoids bot detection)
session.get("https://www.amazon.in", headers=HEADERS, timeout=10)
time.sleep(2)

# Step 2: fetch the search results page
print(f"Fetching: {URL}\n")
response = session.get(URL, headers=HEADERS, timeout=10)
soup = BeautifulSoup(response.text, "html.parser")

# Each product card has this attribute
cards = soup.find_all("div", attrs={"data-component-type": "s-search-result"})

# ── Parse & Compare ───────────────────────────────────────────────────────────

print("=" * 60)
print(f"  Amazon iPhone Search Results")
print(f"  Budget: Rs. {TARGET_PRICE:,}")
print("=" * 60)

count = 0
for card in cards:
    # Title is inside an anchor with class 'a-text-normal'
    title_tag = card.find("a", class_="a-text-normal")
    # Price whole number part (e.g. "59,900")
    price_tag = card.find("span", class_="a-price-whole")

    if not title_tag or not price_tag:
        continue

    title = title_tag.get_text(strip=True).encode("ascii", errors="replace").decode("ascii")
    price = float(re.sub(r"[^\d.]", "", price_tag.get_text()))
    status = "Within Budget" if price <= TARGET_PRICE else "Over Budget"

    count += 1
    print(f"\n[{count}] {title[:60]}")
    print(f"     Price  : Rs. {price:,.0f}")
    print(f"     Status : {status}")

    if count == 5:
        break

print("\n" + "=" * 60)
if count == 0:
    print("No results found. Try running again after a few seconds.")
