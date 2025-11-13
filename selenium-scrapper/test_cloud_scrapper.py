import cloudscraper
scraper = cloudscraper.create_scraper()
html = scraper.get("https://www.hltv.org/stats/matches?...").text
print(html[:500])
