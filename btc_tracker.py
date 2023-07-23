from common import btc_api
from verify_data import is_btc_api_available
import requests


def get_json_btc_tracker(api):
    if is_btc_api_available(api):
        r = requests.get(api).json()
        return r
    else:
        return is_btc_api_available(api)


print(get_json_btc_tracker(btc_api))