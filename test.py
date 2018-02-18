# %%
import requests
from bs4 import BeautifulSoup
import re
# %%

# import requests
# url = "http://www.baidu.com"
# proxies = {
#   "https": "http://111.13.109.27:80",
# }
# response = requests.get(url, proxies=proxies)
# print (response.content)

name = 'Arrow.S05E23.WEB-DL.x264-RARBG' #Arrow.S05E23.WEB-DL.x264-RARBG #arrow.s04e23.hdtv.x264-dimension
url = 'https://rarbg.to/torrents.php?search='
# https://rarbg.to/torrents.php?search=arrow.s04e23.hdtv.x264-dimension
h = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'zh-TW,zh;q=0.8,en-US;q=0.6,en;q=0.4',
    'Connection':'keep-alive',
    'Cookie':'skt=b95uya2xod; skt=b95uya2xod; q2bquVJn=qCBnZk87; LastVisit=1506412485; q2bquVJn=qCBnZk87; expla=2; tcc; aby=2; expla2=2%7CTue%2C%2026%20Sep%202017%2013%3A52%3A32%20GMT',
    'Host':'rarbg.to',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
}
# %%
res = requests.get(url+name, headers=h)#tvshow
soup = BeautifulSoup(res.text, "html.parser")
# %%

# soup.findAll(class_="lista2")[0].findAll('td')[1].a['href']
# soup.findAll(class_="lista2")[0].findAll('td')[1].text
sfac = soup.findAll(class_="lista2")
temp = ''
# int(re.findall('720|1080|000',temp)[0])
tTemp = ''
hTemp = ''
for i in sfac:
    href = re.split('/',i.findAll('td')[1].a['href'])[2].lower()

    text = i.findAll('td')[1].text
    # print(text)

    # print(temp,int(re.findall('720|1080',text)[0]))
    if not re.findall('720|1080',temp):# not720 1080
        if re.findall('720|1080',text):
            temp = re.findall('720|1080',text)[0]
        tTemp = text
        hTemp = href

    if re.findall('720|1080',text):
        # print(re.findall('720|1080',text),re.findall('720|1080',temp)[0])
        if int(re.findall('720|1080',text)[0])>int(re.findall('720|1080',temp)[0]):
            # print('!!!')
            temp = re.findall('720|1080',text)[0]
            tTemp = text
            hTemp = href

    # print(href,text)

# %%
print(hTemp,tTemp)
re.split(' ')
i ='1qvmojt&'
print(i)
n = 'Arrow.S04E23.1080p.HDTV.X264-DIMENSION'
u = 'https://rarbg.to/download.php?id={id}&f={n}&%5Brartv%5D-[rarbg.to].torrent'.format(id=id,n=n)
https://rarbg.to/download.php?id=vb4d2t3&f=Badge.373.1973.1080p.BluRay.H264.AAC-RARBG-[rarbg.to].torrent
print(i)
type(u) # https://rarbg.to/download.php?id=ifmur9p&f=Arrow.S05E23.WEB-DL.x264-RARBG-[rarbg.to].torrent
# %%
