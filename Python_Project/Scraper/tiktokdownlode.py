import requests

url = "https://v16-web.tiktok.com/video/tos/alisg/tos-alisg-pve-0037c001/ba6b3bdaf3654b2180e64fa9e0389f9f/?a=1988&br=1108&bt=554&cd=0|0|1&ch=0&cr=0&cs=0&cv=1&dr=0&ds=3&er=&expire=1629907018&ft=9wMeReYO4kag3&l=202108250956500102451441315B2EC96B&lr=tiktok_m&mime_type=video_mp4&net=0&pl=0&policy=3&qs=0&rc=M3MzbGlzOjZ2NjMzODczNEApZ2gzZjNlZmU3N2ZkZDw5NGdoXmhxXmReaDFgLS1kMS1zczNgXmJjYGA2NGIyXl5jNDY6Yw==&signature=8ebe1685df3ecbb08eba53712b3b8c56&tk=0&vl=&vr="

#querystring = {"a":"1988","br":"1108","bt":"554","cd":"0|0|1","ch":"0","cr":"0","cs":"0","cv":"1","dr":"0","ds":"3","er":"","expire":"1629909747","ft":"9wMeReYO4kag3","l":"202108251042190102450751980434D968","lr":"tiktok_m","mime_type":"video_mp4","net":"0","pl":"0","policy":"3","qs":"0","rc":"M3MzbGlzOjZ2NjMzODczNEApZ2gzZjNlZmU3N2ZkZDw5NGdoXmhxXmReaDFgLS1kMS1zczNgXmJjYGA2NGIyXl5jNDY6Yw==","signature":"d23226c04123966096cd3e58ad17b52f","tk":"0","vl":"","vr":""}

payload = ""
headers = {
    "Accept-Encoding": "identity;q=1, *;q=0",
    "Range": "bytes=0-",
    "Referer": "https://v16-web.tiktok.com/video/tos/alisg/tos-alisg-pve-0037c001/ba6b3bdaf3654b2180e64fa9e0389f9f/?a=1988&br=1108&bt=554&cd=0|0|1&ch=0&cr=0&cs=0&cv=1&dr=0&ds=3&er=&expire=1629907018&ft=9wMeReYO4kag3&l=202108250956500102451441315B2EC96B&lr=tiktok_m&mime_type=video_mp4&net=0&pl=0&policy=3&qs=0&rc=M3MzbGlzOjZ2NjMzODczNEApZ2gzZjNlZmU3N2ZkZDw5NGdoXmhxXmReaDFgLS1kMS1zczNgXmJjYGA2NGIyXl5jNDY6Yw==&signature=8ebe1685df3ecbb08eba53712b3b8c56&tk=0&vl=&vr=",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36"
}

response = requests.request("GET", url, data=payload, headers=headers)#, params=querystring)

with open('tiktok.mp4','wb') as opn:
    opn.write(response.content)
