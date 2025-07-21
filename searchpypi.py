# searchpypi.py - Opens several search results on pypi.org

import requests, sys, webbrowser, bs4

print("Searching...") # Display text while downloading the search results page.
res = requests.get(f"https://pypi.org/search/?q={' '.join(sys.argv[1:])}")
res.raise_for_status()

# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, 'html.parser')
# Open a browser tab for each result.
link_elems = soup.select('.package-snippet')
