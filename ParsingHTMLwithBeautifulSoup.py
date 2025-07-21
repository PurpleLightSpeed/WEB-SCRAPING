import requests, bs4

# Correct URL
res = requests.get("https://automatetheboringstuff.com/example3.html")
res.raise_for_status()
example_soup = bs4.BeautifulSoup(res.text, 'html.parser')
print(type(example_soup))

# Save the HTML to a file
with open("example3.html", "w", encoding="utf-8") as f:
    f.write(res.text)

# Now open and parse the saved file
with open("example3.html", encoding="utf-8") as example_file:
    example_soup = bs4.BeautifulSoup(example_file, 'html.parser')
print(type(example_soup))

example_file = open("example3.html", encoding="utf-8")
example_soup = bs4.BeautifulSoup(example_file.read(), 'html.parser')
elems = example_soup.select("#author")
print(type(elems)) # elems is a list of Tag objects.
print(len(elems))
print(type(elems[0]))
print(str(elems[0])) # The Tag object as a string
print(elems[0].get_text()) # The inner text of the element
print(elems[0].attrs)

p_elems = example_soup.select("p")
print(str(p_elems[0]))
print(p_elems[0].get_text())
print(str(p_elems[1]))
print(p_elems[1].get_text())
print(str(p_elems[2]))
print(p_elems[2].get_text())

soup = bs4.BeautifulSoup(open('example3.html'), 'html.parser')
span_elem = soup.select('span')[0]
print(str(span_elem))
print(span_elem.get('id'))
print(span_elem.get('some_nonexistent_addr') == None)
print(span_elem.attrs)





