from bs4 import BeautifulSoup
import requests

search = input("Search for: ")
params = { "q": search }

req = requests.get("http://www.bing.com/search", params=params)
print("Status: ", req.status_code)

soup = BeautifulSoup(req.text, features="html.parser")

results = soup.find("ol", {"id": "b_results"})
links = results.findAll("li", {"class": "b_algo"})

for item in links:
    text = item.find("a").text
    href = item.find("a").attrs["href"]

    if(text and  href):
        print(text, "\n     ", href)
    else:
        print("Not a link?")


# (soup.prettify())