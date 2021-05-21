#coding:utf-8
import sys
import re
import sys
import random
from bs4 import BeautifulSoup
import socket
reload(sys) 
sys.setdefaultencoding('utf-8')
import requests
class renkler:
    HEADER = '\033[95m'
    mavi = '\033[94m'
    yesil = '\033[92m'
    sari = '\033[93m'
    kirmizi = '\033[91m'
    beyaz = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
print renkler.yesil + """
#######################################################
#               Cüneyt TANRISEVER                     #
#         Reverse ip Cekeici :*)                      #
#         Kullanimi : google.com enter                #
#         seklinde yaziniz. Http vs kullanmayiniz.    #
#         Yalniz domaini yaziniz.                     #
#######################################################
"""
print "basladi"
sor=raw_input("url gir basinda http olmasin = ")
v=[]
vv=[]
vvv=[]
vvvv=[]
sonv=[]
try:
    if "http" in sor:
        print renkler.kirmizi+"iyi bir sonuc icin http veya https yazma"+renkler.beyaz
        sys.exit()
    addr1 = socket.gethostbyname(sor) 
    print str(addr1)+"\n"
    urlcik="http://viewdns.info/reverseip/?host=%s&t=1"%(str(addr1))


    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.28 Safari/537.36' }
    rq=requests.session()
    rq.headers.update(headers)
    request = rq.get(urlcik,timeout=10)
    c= request.content
    soup= BeautifulSoup(c,'html.parser')
    kb= soup.findAll("td")
    for i in kb:
        c=re.match("<td>+.*</td>",str(i))
        if c:
            vv.append(c.group())
    for i in vv[4:]:
        k=i.replace("<td>","")
        vvv.append(k)
    for i in vvv:
        k=i.replace("</td>","")
        vvvv.append(k)
    for i in vvvv:
        cc=open("urller.txt","a")
        cc.write(i+"\n")
        cc.close()
        print str(i)+"\n"
except socket.gaierror:
    print renkler.kirmizi+"url bulunamadi atlaniyor..."+renkler.beyaz
                
v=[]
vv=[]
vvv=[]
vvvv=[]
sonv=[]
print renkler.yesil+"urller.txt dosyasina yazilmistir.\nAyni urller dosyadan silinmistir.\nScript ayirma islemi baslatilmistir."+renkler.beyaz
urlist= open("urller.txt","r").readlines()
deli=[]
deli1=[]
deli3=[]
for dexmod in urlist:
    dex=dexmod.replace("\n","")
    deli.append(dex)
for kar in deli:
    if deli1.count(kar)==0:
        deli1.append(kar)
urlist= open("urller.txt","w")
urlist.close()
for delic in deli1:
    urlist= open("urller.txt","a")
    urlist.write(delic+"\n")
    urlist.close()
deli=[]
deli1=[]
deli3=[]
