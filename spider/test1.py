# 糗事百科

import requests
import re

userAgent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36";

headers = {
    'User-Agent': userAgent}

r = requests.get('http://www.qiushibaike.com/hot/page/1', headers=headers)
print(r.status_code)


"""
    正则表达式
    说明：匹配这段html中的h2里的元素，为什么不直接匹配h2是应为还有其他h2标签在
    <a.*?>.*<h2>(.*?)</h2>.*</a>

    html
    <a href="/users/24003169/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">
    <img src="//pic.qiushibaike.com/system/avtnew/2400/24003169/thumb/20180306093405.JPEG?imageView2/1/w/90/h/90" alt="无奈恋上你的chun">
    </a>
    <a href="/users/24003169/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
    <h2>
    无奈恋上你的chu…
    </h2>
    </a>
"""

pattern = re.compile(r'<a.*?>.*?<h2>(.*?)</h2>.*?</a>.*?<div class="content">.*?<span>' +
                     '(.*?)</span>.*?</div>.*?<span class="stats-vote">' +
                     '<i class="number">(.*?)</i>.*?<i class="number">(.*?)</i>', re.S)
items = re.findall(pattern, r.text)

for item in items:
    print(item[0], item[1], item[2], item[3])
