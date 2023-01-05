import os
import requests
import json
from io import BytesIO
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO

def StartSearch(query):
    params = { "q": query }

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
        try:
            img = Image.open(BytesIO(img_obj.content))
        except:
            print("Image request did not return an image.") # Scraper probably got blocked by a bot blocker

        # Create folder (so I can delete it before pushing to Git)
        if not os.path.exists(os.getcwd() + "\\scraped_images\\"):
            os.mkdir(os.getcwd() + "\\scraped_images")
        if not os.path.exists(os.getcwd() + "\\scraped_images\\" + query):
            os.mkdir(os.getcwd() + "\\scraped_images\\" + query)

        try:
            img.save("./scraped_images/" + query + "/" + title, img.format)
        except:
            print("Couldn't save " + title + img.format)

while True:
    query = input("Search for: ")
    if(query == "exit()"):
        break
    StartSearch(query)
