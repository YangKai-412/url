import urllib.request as request

import json

import ssl # 在 urllib.error.URLError異常時加入

src = "https://data.taipei/opendata/datalist/apiAccess?scope=resourceAquire&rid=296acfa2-5d93-4706-ad58-e83cc951863c"
ssl._create_default_https_context = ssl._create_unverified_context
with request.urlopen(src) as response:
    data = json.load(response)  # 利用 json 模組處理 json 資料格式

# 將公司名稱列表出來
clist = data['result']['results']
with open('data.txt', 'w', encoding='utf-8') as f:
    for company in clist:
        f.write(company['公司名稱'] + '\n')
