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

    # Alle 3 deze functies werken
    # 1 komt uit de video
    # 2 heb ik precies het item gevonden (en eerste 3 tekens weggehaald want Bing zet er "Web" voor)
    # 3 heb ik algemeen in het item gezocht, want het is ook meteen de eerste "p" tag die in het item staat
    summ1 = item.find("a").parent.parent.find("p").text
    summ2 = item.find("div", {"class":"b_caption"}).find("p").text[3:]
    summ3 = item.find("p").text

    children = item.children

    if(text and  href):
        print(text, "\n\t", href, "\n\t", summ2)
        1 == 1 # breakpoint
    else:
        print("Not a link?")
