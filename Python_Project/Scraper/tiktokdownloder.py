import requests
from urllib.parse import unquote
import webbrowser
from threading import Thread
import time

def main():
    url=input("Enter a Tik Tok Url  ")
    payload = ""
    headers = {
        "cookie": "s_v_web_id=verify_dfd80fa10f3d83f52c6bfe8d02a2b050; tt_csrf_token=AzR6r4BLHOZoN6qg8iOCZmsF; tt_webid_v2=7000293464513824258; tt_webid=7000293464513824258; ttwid=1%257CeypXY8EuHs-9Pg6oXt-GWCNV0SY9xMtqK_R83_c9DgA%257C1629882866%257Ca37735dc252f74862a607cbe0e12213658e66ee80974f71d50a073fb5ec53e05",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36"
    }
    response = requests.request("GET", url, data=payload, headers=headers)
    a=str(response.content)
    b=a.split('"downloadAddr":"')[1]
    b=b.split('","shareCover"')[0]
    a=eval(f"unquote('{b}')")
    a=a.encode('ascii','ignore').decode('unicode_escape')
    print(a)
    finally2(a)

def finally2(url):
    print("Downloading")
    x=time.time()
    payload = ""
    headers = {
        "Accept-Encoding": "identity;q=1, *;q=0",
        "Range": "bytes=0-",
        "Referer":url,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36"
    }
    response = requests.request("GET", url, data=payload, headers=headers)
    with open('tiktok.mp4','wb') as opn:
        opn.write(response.content)
    print("Downloded in ",time.time()-x)
    

if __name__ =="__main__":
    print(main())
