# pip install selenium-wire
from seleniumwire import webdriver

# Create a new instance of the Firefox driver
driver = webdriver.Chrome()

# Go to the Google home page
driver.get('https://www.tiktok.com/tag/cats')

# Access requests via the `requests` attribute
for request in driver.requests:
    if request.response:
        if str(request.path).__contains__("https://www.tiktok.com/share/item/list?secUid"):
            print(request.path)
