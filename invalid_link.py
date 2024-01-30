import requests
import json

invalid_text = "Unknown Invite"

with open('discord.json', 'r') as json_file:
    discord_url = json.load(json_file)

link = "https://discord.com/api/v9/invites/{}?with_counts=true&with_expiration=true"

dicord_url = []

for url in discord_url:
    for x in url:
        invite_link = url[x].split("/")[-1]
        response = requests.get(link.format(invite_link))
        result_text = response.text
        if(result_text[13:27] == invalid_text):
            dicord_url.append(url)
    with open('result.json', 'w') as json_file:
        json.dump(dicord_url, json_file)

    
