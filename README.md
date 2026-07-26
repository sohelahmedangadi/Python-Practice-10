# Assignment 10 – Amazon Product Scraper 🛒

A Python web-scraping script that fetches **Python programming books** from
Amazon India, extracts their titles and prices using **BeautifulSoup**, and
compares each price against a configurable budget threshold.

---

## Features

| Feature | Detail |
|---|---|
| Target site | Amazon India (`amazon.in`) |
| Browser-like headers | ✅ Included (User-Agent, Accept-Language, etc.) |
| Data extracted | Product title, price (₹), product URL |
| Price comparison | Flags each item as **Within Budget** or **Over Budget** |
| Budget threshold | ₹500 (configurable in `amazon_scraper.py`) |

---

## Project Structure

```
Python Assignement-10/
├── amazon_scraper.py   ← Main scraper script
├── README.md           ← This file
└── screenshots/
    ├── code.png        ← Screenshot of the source code
    └── output.png      ← Screenshot of the terminal output
```

---

## How to Run

### 1. Prerequisites

Make sure **Python 3.10+** is installed. Verify with:

```bash
python --version
```

### 2. Install Dependencies

```bash
pip install requests beautifulsoup4
```

### 3. Run the Scraper

```bash
python amazon_scraper.py
```

### 4. Expected Output

```
[INFO] Fetching: https://www.amazon.in/s?k=python+programming+books

======================================================================
               Amazon Product Price Comparison
                       Budget: ₹500
======================================================================

[1] Python Crash Course, 3rd Edition
     Price  : ₹449.00
     Status : ✅ Within Budget
     Link   : https://www.amazon.in/...

[2] Automate the Boring Stuff with Python
     Price  : ₹799.00
     Status : ❌ Over Budget
     Link   : https://www.amazon.in/...
...
----------------------------------------------------------------------
  Total products scraped : 5
  Within budget (≤ ₹500) : 2
  Over budget   (> ₹500) : 3
======================================================================
```

---

## Configuration

Open `amazon_scraper.py` and edit the constants at the top:

```python
TARGET_PRICE_INR = 500      # Change your budget (in ₹)
SEARCH_URL = "https://www.amazon.in/s?k=python+programming+books"
                             # Change search keyword
```

---

## Notes

- Amazon occasionally returns a CAPTCHA or empty page. If you get
  `[WARN] No products found`, wait a moment and run again.
- The browser-like `HEADERS` dictionary mimics a real Chrome browser
  request to reduce bot-detection.
- Prices shown are in **Indian Rupees (₹)** as scraped from `amazon.in`.

