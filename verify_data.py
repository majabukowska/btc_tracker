import requests


def is_btc_api_available(api):
    r = requests.get(api)
    if r.status_code != 200:
        return f"Status code {r.status_code}"
    return True