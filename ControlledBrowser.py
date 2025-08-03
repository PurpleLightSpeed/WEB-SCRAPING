from selenium import webdriver

browser = webdriver.Firefox()
print(type(browser))
browser.get("https://inventwithpython.com")

### Clicking Browser Buttons
## Selenium can simulate clicks on various browser buttons through the following methods:
# browser.back() Clicks the Back button
# browser.forward() Clicks the Forward button
# browser.refresh() Clicks the Refresh/Reload button
# browser.quit() Clicks the Close Window button

