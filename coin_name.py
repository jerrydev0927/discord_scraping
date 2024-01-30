import requests
import json
from bs4 import BeautifulSoup
  # Replace this with the target website URL
 
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
}

# def get_discord(url):
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
#     }
#     response = requests.get(url, headers=headers)

#     soup = BeautifulSoup(response.content, 'html.parser')

#     lists = soup.find_all("span", attrs={'class': 'tw-flex tw-items-center tw-gap-x-1'})
#     for list in lists:
#         community_type = list.text
#         if community_type == "\n\nDiscord\n":
#             div = list.parent
#             community_item = div.parent.get('href')
#             community_links = {url: community_item}
coin_lists = []
for i in range(1, 125):
    url = "https://www.coingecko.com/?page=" + str(i+1)
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    elements = soup.find_all("table")[0].find_all("tr")
    for element in elements:
        td = element.find_all("td")
        if len(td) >= 3:
            a = td[2].find("a")
            if a:
                coin = "https://www.coingecko.com/" + a.get('href')
                coin_lists.append(coin)
    with open('coin_name.json', 'w') as json_file:
        json.dump(coin_lists, json_file)




