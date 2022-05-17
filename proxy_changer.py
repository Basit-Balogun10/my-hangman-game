# import requests
# import random
# from bs4 import BeautifulSoup as bs
#
#
# def get_free_proxies():
#     url = "https://free-proxy-list.net/"
#     # get the HTTP response and construct soup object
#     soup = bs(requests.get(url).content, "html.parser")
#     for row in soup.find("table", attrs={"id": "proxylisttable"}).find_all("tr")[1:]:
#         tds = row.find_all("td")
#         try:
#             ip = tds[0].text.strip()
#             port = tds[1].text.strip()
#             host = f"{ip}:{port}"
#             proxies.append(host)
#         except IndexError:
#             continue
#     print(proxies)
#     return
#
# get_free_proxies()
#
# def get_session(proxies):
#     # construct an HTTP session
#     session = requests.Session()
#     # choose one random proxy
#     proxy = random.choice(proxies)
#     session.proxies = {"http": proxy, "https": proxy}
#     return session
#
#
#
#
# for i in range(5):
#     s = get_session(proxies)
#     try:
#         print("Request page with IP:", s.get("http://icanhazip.com", timeout=1.5).text.strip())
#     except Exception as e:
#         print()
#         print('Continuing')
#         continue


# # METHOD 2
from lxml.html import fromstring
import requests
from itertools import cycle
import traceback


def get_proxies():
    url = 'https://free-proxy-list.net/'
    response = requests.get(url)
    parser = fromstring(response.text)
    proxies = set()
    for i in parser.xpath('//tbody/tr')[:10]:
        if i.xpath('.//td[7][contains(text(),"yes")]'):
            proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
            proxies.add(proxy)
    return proxies


# If you are copy pasting proxy ips, put in the list below
# proxies = ['121.129.127.209:80', '124.41.215.238:45169', '185.93.3.123:8080', '194.182.64.67:3128', '106.0.38.174:8080', '163.172.175.210:3128', '13.92.196.150:8080']# get_proxies()#
get_proxies()
print(proxies)
proxy_pool = cycle(proxies)
print(proxies)
url = 'https://httpbin.org/ip'
for i in range(1, 11):
    # Get a proxy from the pool
    proxy = next(proxy_pool)
    print("Request #%d" % i)
    try:
        response = requests.get(url, proxies={"http": proxy, "https": proxy})
        print(response.json())
    except:
        # Most free proxies will often get connection errors. You will have retry the entire request using another proxy to work.
        # We will just skip retries as its beyond the scope of this tutorial and we are only downloading a single url
        print("Skipping. Connnection error")
