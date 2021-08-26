from urllib.parse import urlencode
import requests
import uuid
from concurrent.futures import ThreadPoolExecutor
import time

class Google:
    def __init__(self,query='',num=10):
        self.query= query
        self.urls=[]
        self.num=num
        
    def urls(self):
        self.urls=[]


#https://duckduckgo.com/i.js?l=us-en&o=json&q=try&vqd=3-272926314978172514561393670944284080213-46768884755372610953189977219212273210&f=,,,,,&p=1
class DuckDuckGo:
    def __init__(self,query='',num=100):
        self.enco=urlencode
        self.query= query
        self.urls=[]
        self.timer=time.time()
        self.status='No Download In Quee'
        self.num=num
        self.res=''
        self.headers={'authority': 'duckduckgo.com',
                      'method': 'GET',
                      'path': '/?q='+self.query,
                      'scheme': 'https',
                      'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                      'accept-encoding': 'gzip, deflate, br',
                      'accept-language': 'en-US,en;q=0.9',
                      'referer': 'https',
                      'sec-fetch-dest': 'document',
                      'sec-fetch-mode': 'navigate',
                      'sec-fetch-site': 'same-origin',
                      'sec-fetch-user': '?1',
                      'sec-gpc': '1',
                      'upgrade-insecure-requests': '1',
                      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Brave Chrome/90.0.4430.85 Safari/537.36'}
        self.url()
        self.status='Their Is A Download Queue. "call" the Download Fucntion , The Search Term is'+self.query

       
    def url(self):
        res=requests.get("https://duckduckgo.com/?q="+self.query,headers=self.headers)
        c=res.content[int(res.content.find(b'vqd')):int(res.content.find(b'vqd'))+86].decode().split("=")[-1].replace("'",'')
        for i in range(0,self.num//100+1):
            _defl=f"https://duckduckgo.com/i.js?vqd={c}&p={i}&s={100+i*100}&"
            custom_user_agent = "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0"
            qu=self.enco({'q':self.query})
            try:
                res = requests.get(_defl+qu, headers={"User-Agent": custom_user_agent})
                a=res.json()['results']
                self.urls+=a
            except Exception as e:
                print(e)
                pass

    def cleaner(self):
        pass

    def download(self):
        executor = ThreadPoolExecutor(100)
        for i in self.urls[:self.num]:
            future = executor.submit( self.contgen, (i['image']))
        print(f"It Took {time.time()-self.timer} sec with threadpool")
        self.timer=time.time()-self.timer

    def contgen(self,dourl):
        har=requests.get(dourl)
        if '.png' in dourl:
            ex='.png'
        else:
            ex='.jpg'
        with open(f"{uuid.uuid1()}{ex}",'wb') as opn:
            opn.write(har.content)

    def __str__(self):
        return self.status
        



class Bing:
    '''
Possible attack
lis=[]
headers={'authority': 'www.bing.com',
'method': 'GET',
'scheme': 'https',
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en-US,en;q=0.9',
'referer': 'https',
'sec-fetch-dest': 'document',
'sec-fetch-mode': 'navigate'
'sec-fetch-site': 'same-origin',
'sec-fetch-user': '?1',
'sec-gpc': '1',
'upgrade-insecure-requests': '1',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36'}
for i in range(1,10):
	url=f'https://www.bing.com/images/async?q=hello&first={i*10}&count=100&mmasync=1'
	res=requests.get(url,headers=headers)
	for j in str(res.content).split('src'):
		if 'th?id=OIF' in j:
			print(j.split('alt')[0][1:])
			lis.append(str(j.split('alt')[0][1:]))
    '''

    def __init__(self,query='',num=10):
        self.query= query
        self.urls=[]
        self.num=num
        
    def urls(self):
        self.urls=[]



