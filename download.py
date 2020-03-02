#!/usr/bin/env python
# coding: utf-8

import requests
import re
from html import unescape

s = requests.Session()
s.headers.update({'User-Agent': 'M'})

for n in range(91563, 91563+1000):
    u = f'https://regards.monuments-nationaux.fr/fr/asset/id/{n}/x/idFeatureFrom/798/thumbIndex/0/mosaicCount/177/ajax/1/format/json'
    h = s.get(u).json()['html']
    title = unescape(re.search('<h1 title="([^"]+)"', h).group(1))
    print(title)
    url=f'https://regards.monuments-nationaux.fr/fr/asset/highRes/id/{n}/ajax/1/format/json'
    r = s.get(url)
    u2 = r.json()['html']
    r=s.get(u2)
    with open(f'{title}.jpg', 'wb') as f:
        f.write(r.content)

