import requests

response = requests.get("https://automatetheboringstuff.com/files/rj.txt")
print(type(response))
print(response.status_code == requests.codes.ok)
print(len(response.text))
print(response.text[:210])

response = requests.get("https://inventwithpython.com/page_that_does_not_exist")
try:
    response.raise_for_status()
except Exception as exc:
    print(f"There was a problem with {exc}")
    
response = requests.get("https://automatetheboringstuff.com/files/rj.txt")
response.raise_for_status()
with open("RomeoAndJuliet.txt", "wb") as play_file:
    for chunk in response.iter_content(100000):
        play_file.write(chunk)

# Call requests.get() to download the file.
# Call open() with 'wb' to create a new file in write binary mode.
# Loop over the Response object’s iter_content() method.
# Call write() on each iteration to write the content to the file.
