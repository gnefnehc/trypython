import os
import re
# print(os.getcwd())

import requests
import re
from bs4 import BeautifulSoup

##名子找網頁編號
def namefindurl(name,season):
    url = 'http://subhd.com/search0/'
    #tvshow = 'arrow'
    res = requests.get(url+name+'.'+season)#tvshow
    soup = BeautifulSoup(res.text, "html.parser")
    box = soup.find_all(class_="box")

    for i in box:
        # print(i)
        d_title = i.find(class_='d_title').text
        # print(season in d_title.lower())
        if name.lower() in d_title.lower():
            if season.lower() in d_title.lower():
                href = i.find(class_="pull-left lb_l hidden-xs").a
                if href != None:##is none ['href'] is error
                    # print(href['href'])
                    return(href['href'])

###切割列表以集分割
def souptosdict(soup):
    tbodyTr = soup.tbody.findAll(['tr'])
    sdict = {}
    slist = []
    sTemp = ''
    count = 0
    # print(tbodyTr[3])

    for i in tbodyTr:
        if not i.find(class_="dt_edition"):
            if sTemp:#第二次找到sTemp
                # print('sTemp : '+sTemp)
                sdict[sTemp]=slist
                slist=[]
                sTemp = re.findall('\d*',i.text)[3]

            if sTemp=='':#第一次空字串
                sTemp = re.findall('\d*',i.text)[3]

        if i.find(class_="dt_edition"):
            if i.find(class_="label label-info"):# or i.find(class_="label label-success") or i.find(class_="label label-primary")
                ifc = i.find(class_="dt_edition")
                slist.append('en.tw_'+ifc.a['href']+'_'+ifc.text)

        count+=1
        if count==len(tbodyTr):
            # print('count==end')
            if sTemp=='':
                # print('sTemp : end')
                sdict['end']=slist
                slist=[]

            if sTemp:
                # print('sTemp : '+sTemp)
                sdict[sTemp]=slist
                slist=[]

    # print(type(sdict['23'][0]))
    return(sdict)


# path = os.getcwd()+'/tvshow/'
# for i in os.listdir(path):
#     print(i)
#     if re.split('_',i)!=3:
#         name = re.split('_',i)[0]
#
        # seaEpi = re.split('_',i)[1]
        # season = int(seaEpi[1:3])
        # episode = int(seaEpi[4:6])
#         # season = re.findall('[Ss][0-9][0-9]',i)[0]
#         a = re.split('/',namefindurl(name, season))[2]
#         print(a)
#         os.rename(path+i, path+i+'_'+a)
#
#     # if re.split('_',i)==3:


url = 'http://subhd.com/do0/'
tvshow = 'arrow_s04e10_26302901'
name = re.split('_',tvshow)[0]
#season episode
seaEpi = re.split('_',tvshow)[1]
season = int(seaEpi[1:3])
episode = int(seaEpi[4:6])
urlNumbe = re.split('_',tvshow)[2]
res = requests.get(url+'/'+urlNumbe)#tvshow
soup = BeautifulSoup(res.text, "html.parser")

sdict = souptosdict(soup)
print(sdict.keys())
# print(sdict['23'])

sdictCount=len(sdict)
# print(sdictCount)
if 'end'in sdict:
    # print('end')
    sdictCount-=1
print(sdictCount)

while episode<sdictCount:
    episode+=1
    # print(sdict[str(episode)][0])
    rs2l = re.split('_',sdict[str(episode)][0])[2].lower()
    print(rs2l)
    srtName = re.split('[^a-z0-9.-]|.?720p?|.?10820p?',rs2l)
    srtNameNew = ''
    for i in srtName:
        srtNameNew+=i
    print(srtNameNew)
    # print('download : '+str(episode))
