# simple-price-scraper

**Track prices across product pages into one CSV. No heavy dependencies.**

Point it at a list of product URLs; it appends timestamped title + price rows
to `prices.csv`, so you can watch prices move over time.

## Run it

```
echo "https://example.com/product" >> urls.txt
python scrape.py   # appends timestamped rows to prices.csv
```

Polite request pacing built in. Standard library only.

## What clients use this for

- Competitor price monitoring for small shops
- MAP / resale price checks across marketplaces
- Whole-catalogue price audits (hundreds of pages → one sheet)
- Alerts when a watched price moves

## Want this pointed at your market?

This is a sample of paid client work. Commissions: custom scrapers, scheduled
price tracking, catalogue audits, data delivered as clean CSV / Excel.

Flat fee agreed up front, 50% prepayment in USDC (Polygon), delivery in 24–48h.

**DM on X: [@cOldfaceculYYY](https://x.com/cOldfaceculYYY)** — tell me which pages you watch by hand today, get a fixed quote.
