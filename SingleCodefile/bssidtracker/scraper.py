from bs4 import BeautifulSoup as bs
import requests as req
import re
import json
from pprint import pprint


encoded_use = 'QUlEMjU4NzFhZDE4YjVkZGEzYzE4MTVkNmUwYzlkODI2YTU6N2I2ZmE1NzQ0MTQxZWY5MTE3NjczNWNjZTdmNTdmZDU='
header = {'Authorization': 'Basic ' + encoded_use}
BSSID = '20:57:AF:3E:BF:90'
base_url = 'https://api.wigle.net/api/v3/detail/wifi/'
res = req.get(base_url + BSSID, headers=header)
pprint(res.json())