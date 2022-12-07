import json
from django.test import TestCase
from urllib.request import urlopen

import requests

with urlopen("http://127.0.0.1:8000/posts/posts_list/")as resp:
    res = resp.read()

data = json.loads(res)
print(json.dumps(data, indent=2))
