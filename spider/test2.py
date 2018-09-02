# http://eleanoa.ys168.com/
import time

import requests
import re
import os

userAgent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36";

headers = {
    'User-Agent': userAgent}

r = requests.get('http://ce.ys168.com/f_ht/ajcx/ml.aspx?cz=ml_dq&_dlmc=eleanoa&_dlmm=', headers=headers)
print(r.text)

pattern = re.compile(r'li id="ml_(.*?)".*?>.*?<a class="ml" href="javascript:;">(.*?)</a>', re.S)
pattern1 = re.compile(r'<a href="(.*?)".*?>(.*?)</a>', re.S)
items = re.findall(pattern, r.text)
curPath = 'G:\\55Python\\Demo\\迷糊的安安\\'

for item in items:
    print(item[0], item[1])

    if not os.path.isdir(curPath + item[1]):
        os.mkdir(curPath + item[1])

    r1 = requests.get('http://ce.ys168.com/f_ht/ajcx/wj.aspx?cz=dq&mlbh=' + item[0] + '&_dlmc=eleanoa&_dlmm=',
                      headers=headers)
    items1 = re.findall(pattern1, r1.text)

    for item1 in items1:
        print(item1[0], item1[1])

        # time.sleep(0.1)

        if str(item1[0]).find('.html') == -1:
            try:
                r = requests.get(item1[0], headers=headers)
                r.raise_for_status()

                if not os.path.isfile(curPath + item[1] + "\\" + item1[1]):
                    with open(curPath + item[1] + "\\" + item1[1], "wb") as f:
                        f.write(r.content)
                        f.flush()
                else:
                    print(item1[1] + '已经存在')
            except:
                print(item1[0] + '无法下载')
