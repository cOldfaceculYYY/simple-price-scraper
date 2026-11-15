#!/usr/bin/env python3
"""Simple price scraper — sample build.

Fetches a list of product pages, extracts title + price with plain
regex (no heavy deps), and appends a timestamped row to prices.csv.
Polite by default: 2s between requests, honest user-agent.

Usage: put URLs in urls.txt (one per line), then: python scrape.py
"""
import csv, re, time, urllib.request
from datetime import datetime, timezone

UA = {"User-Agent": "price-check-sample/1.0 (personal project)"}
PRICE_RE = re.compile(r"[$€£]\s?\d[\d,]*\.?\d{0,2}")
TITLE_RE = re.compile(r"<title>(.*?)</title>", re.S | re.I)

def fetch(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=20) as r:
        return r.read().decode("utf-8", "ignore")

def main():
    urls = [u.strip() for u in open("urls.txt") if u.strip()]
    with open("prices.csv", "a", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        for url in urls:
            try:
                html = fetch(url)
                title = (TITLE_RE.search(html).group(1).strip()
                         if TITLE_RE.search(html) else "")
                price = PRICE_RE.search(html)
                w.writerow([datetime.now(timezone.utc).isoformat(),
                            title[:80], price.group(0) if price else "", url])
                print("ok:", title[:50])
            except Exception as e:
                print("skip:", url, e)
            time.sleep(2)

if __name__ == "__main__":
    main()
