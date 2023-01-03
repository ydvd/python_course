from io import BytesIO
from bs4 import BeautifulSoup
import requests
import json
from PIL import Image
from io import BytesIO

search = input("Search for: ")
params = { "q": search }

req = requests.get("http://www.bing.com/images/search", params=params)
print("Status: ", req.status_code)

soup = BeautifulSoup(req.text, features="html.parser")

links = soup.findAll("a", {"class":"iusc"})

for item in links:

    # The way to get the URL has changed A LOT since 2016, so this is the way it actually works now:
    meta = json.loads(item.attrs["m"])
    img_obj = requests.get(meta["murl"]) 
    title = meta["murl"].split("/")[-1]

    print("Downloading", title, "...")    
    img = Image.open(BytesIO(img_obj.content))
    img.save("./scraped_images/" + title, img.format)