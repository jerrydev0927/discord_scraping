import requests
import json
from bs4 import BeautifulSoup

with open('coin_name.json', 'r') as json_file:
    coin_name = json.load(json_file)

coin_disord = []

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
}

for url in coin_name:

  response = requests.get(url, headers=headers)

  soup = BeautifulSoup(response.content, 'html.parser')

  community_links = {}

  lists = soup.find_all("span", attrs={'class': 'tw-flex tw-items-center tw-gap-x-1'})
  for list in lists:
    community_type = list.text
    if community_type == "\n\nDiscord\n":
        div = list.parent
        community_link = div.parent.get('href')
        community_links = {url: community_link}
        coin_disord.append(community_links)
    with open('discord.json', 'w') as json_file:
        json.dump(coin_disord, json_file)

            
