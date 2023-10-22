import requests
from urllib.request import urlretrieve
from bs4 import BeautifulSoup as bs

from fake_useragent import UserAgent


# ua = UserAgent()
# header = {"User-Agent": str(ua.chrome)}


url = 'https://www.google.com/search?q=cat&tbm=isch'

# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"
# }
response = requests.get(url)

html_text = response.text
html = bs(html_text, 'html.parser')

thumbs = html.select("a div img", limit=10)

i = 0
for thumb in thumbs:
    # print(thumb["src"])
    urlretrieve(thumb["src"], str(i)+".jpg")
    i += 1
