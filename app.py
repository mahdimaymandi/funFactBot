from mastodon import Mastodon
import ssl
import requests
import json
import config

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

mastodon = Mastodon(
    access_token = config.bot_token,
    api_base_url = 'https://mstdn.plus/'
)

def postFunFact():
    limit = 1
    api_url = 'https://api.api-ninjas.com/v1/facts?limit={}'.format(limit)
    response = requests.get(api_url, headers={'X-Api-Key': config.ninja_key})
    if response.status_code == requests.codes.ok:
        data = json.loads(response.text)
        fact = data[0]["fact"]
        message = fact + "\n\n#funfact"
        mastodon.status_post(message)
    else:
        print("Error:", response.status_code, response.text)

postFunFact()
