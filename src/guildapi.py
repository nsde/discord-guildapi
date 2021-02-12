import requests
import json

def getguild(guild_id):
    guild_id = str(guild_id)
    http_response = requests.get(f'https://discord.com/api/guilds/{guild_id}/widget.json')
    response_data = http_response.json()
    data = json.dumps(response_data)
    return data