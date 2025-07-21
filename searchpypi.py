# searchpypi.py - Opens several search results on pypi.org

import requests, sys, webbrowser, bs4

if len(sys.argv) < 2:
    print("Usage: python searchpypi.py <search term>")
    sys.exit()

print("Searching...") # Display text while downloading the search results page.
headers = {'User-Agent': 'Mozilla/5.0'}
res = requests.get(f"https://pypi.org/search/?q={' '.join(sys.argv[1:])}", headers=headers)
res.raise_for_status()

# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, 'html.parser')
# print(soup.prettify())
link_elems = soup.select('a.result')
print(f"Found {len(link_elems)} results.")

# Open a browser tab for each result.
num_open = min(5, len(link_elems))
for i in range(num_open):
    url_to_open = (f"https://pypi.org{link_elems[i].get('href')}")
    print("Opening", url_to_open)
    webbrowser.open(url_to_open)
    
