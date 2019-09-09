import re

import requests
from requests import RequestException


def check(url, data, head):
    pattern = '<title>小黑盒，一款专为steam游戏玩家服务的专业应用。</title>'
    try:
        response = requests.get(url, params=data, headers=head)
        if response.status_code == 200:
            text = response.text
            if re.search(pattern, text):
                return None
            else:
                return text
        else:
            return None
    except RequestException:
        return "RequestException"
