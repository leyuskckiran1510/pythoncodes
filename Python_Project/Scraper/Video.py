import requests
from urllib.parse import urlencode
import ffmpeg
import uuid

url=input("Enter Url     "   )
query=urlencode({'url':f'{url}','phonydata':'true'})
print(query)
headers={'authority': 'backendace.1010diy.com',
                      'method': 'GET',
                      'path': '/web/free-mp3-finder/detail?'+query,
                      'scheme': 'https',
                      'accept':'*/*',
                      'accept-encoding': 'gzip, deflate, br',
                      'accept-language': 'en-US,en;q=0.9',
                      'referer': 'https',
                      'sec-fetch-dest': 'empty',
                      'sec-fetch-mode': 'cors',
                      'sec-fetch-site': 'same-site',
                      'sec-fetch-user': '?1',
                      'sec-gpc': '1',
                        'origin': 'https://client_ace.1010diy.com',
                      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Brave Chrome/90.0.4430.85 Safari/537.36'}
site='https://backendace.1010diy.com/web/free-mp3-finder/detail?'+query


res=requests.get(site,headers=headers)
urls={}
exs={}
download_link='https://stream_ace.1010diy.com'
for n,i in enumerate(res.json()['data']['audios']):
    urls[f'{n}a']=i['url']
    exs[f'{n}a']=i['ext']
    print(f'{n}a\t','audio only\t',i['formatNote'],"\t\n\t[+]",i['url'][:10],"...")
for n,i in enumerate(res.json()['data']['videos']):
    urls[f'{n}v']=i['url']
    exs[f'{n}a']=i['ext']
    print(f'{n}v\t',f'videos\twith audio = {i["audio_exist"]}\t\n[-]',i['formatNote'],"\t\n\t[+]",i['url'][:10],".....")


inn=input("Enter a choice  from  like 1a,1v.... to download ")


try:
    print(urls[inn])
    res= requests.get(urls[inn],headers={"range":"bytes=0-"})
    with open(f'{uuid.uuid1}.{exs[inn]}','wb') as opn:
        opn.write(res.content)
except:
    print(download_link+urls[inn])
    res= requests.get(download_link+urls[inn],headers={"range":"bytes=0-"})
    with open(f'{uuid.uuid1}.{exs[inn]}','wb') as opn:
        opn.write(res.content)
    


print("Sucessfully Downloaded")


#yes=res.json()['data']['audios']['formatNote']
#yes2=res.json()['data']['videos']
def output():
    video = ffmpeg.input('video.mp4')
    audio = ffmpeg.input('audio.wav')
    out = ffmpeg.output(video, audio, video_path, vcodec='copy', acodec='aac', strict='experimental')
    out.run()
