import json

from interbloc_api_client.client import Client
from interbloc_api_client.api.cosmoshield import (
    get_all_blacklisted_domains_cosmoshield_domains_blacklist_get as get_all_blacklisted_domains
)


BASE_URL = 'https://api.interbloc.org'

client = Client(base_url=BASE_URL)


def get_blacklisted_domains():
    response = get_all_blacklisted_domains.sync_detailed(client=client)
    if response.status_code != 200:
        raise Exception('Invalid response')

    return json.loads(response.content)
