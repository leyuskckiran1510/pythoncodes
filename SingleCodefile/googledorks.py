import requests
from bs4 import BeautifulSoup as bs

url = "https://www.exploit-db.com/google-hacking-database"


for k in range(63):
	querystring = {"draw":f"{i}","columns[0][data]":"date",
	"columns[0][name]":"date","columns[0][searchable]":"true",
	"columns[0][orderable]":"true","columns[0][search][value]":"",
	"columns[0][search][regex]":"false","columns[1][data]":"url_title",
	"columns[1][name]":"url_title","columns[1][searchable]":"true",
	"columns[1][orderable]":"false","columns[1][search][value]":"",
	"columns[1][search][regex]":"false","columns[2][data]":"cat_id",
	"columns[2][name]":"cat_id","columns[2][searchable]":"true",
	"columns[2][orderable]":"false","columns[2][search][value]":"",
	"columns[2][search][regex]":"false","columns[3][data]":"author_id",
	"columns[3][name]":"author_id","columns[3][searchable]":"false",
	"columns[3][orderable]":"false","columns[3][search][value]":"",
	"columns[3][search][regex]":"false","order[0][column]":"0","order[0][dir]":"desc",
	"start":"15","length":"120","search[value]":"","search[regex]":"false","author":"",
	"category":"","_":"1649778664563"}


	payload = "------WebKitFormBoundaryho0CuHq2Z95lYYKz\nContent-Disposition: form-data; name=\"password\"\n\nkg69h\n------WebKitFormBoundaryho0CuHq2Z95lYYKz\nContent-Disposition: form-data; name=\"new_password\"\n\nkiran\n------WebKitFormBoundaryho0CuHq2Z95lYYKz\nContent-Disposition: form-data; name=\"retype_password\"\n\nkiran\n------WebKitFormBoundaryho0CuHq2Z95lYYKz--"
	headers = {
	    "cookie": "CookieConsent={stamp:%27-1%27%2Cnecessary:true%2Cpreferences:true%2Cstatistics:\
	    true%2Cmarketing:true%2Cver:1%2Cutc:1649778664838%2Cregion:%27NP%27}; XSRF-TOKEN=eyJpdiI6ImpmWkV2RDZadn\
	    VsZUdXUnh3MEpkS0E9PSIsInZhbHVlIjoib2h4Qjh0TVZWY0cwMmpUUk9zTFZvXC9admlucXo4NXZzNEd2Nm9Hb0Zjc1dGSTNyVTU0YVorT\
	    mhadnJKb0s2cXUiLCJtYWMiOiJhOTc0YzUwYjNkOTgwMGZhYjYyMDI2NzA3MDVkZWI3OTdmYmU2NWViYTY2OTBlYzY4OTNkNmJlOTE3MzVlM2JiIn0%3D; \
	    exploit_database_session=eyJpdiI6IjBxeGRvRWlIWVk0c2RmWlwvejF3c0ZnPT0iLCJ2YWx1ZSI6IktVYytvS1wvcG1XTWpVMnRPbW5ZY1hUVGlHS1g\
	    4K3JWUm1FZEU4NEtcL1FxSXFLazFjd2UyNkVTaTFnT0IzN3hsaCIsIm1hYyI6ImNlMjQ3MzY2YTUyOGNhMDQ1NzE2NGU5NTlmZDgxMjg5MzM1YWVkNTlkN2UyMD\
	    JlYmJmMDQ2NDM1ODc4ZGRlODcifQ%3D%3D",
	    "accept": "application/json, text/javascript, */*; q=0.01",
	    "accept-encoding": "gzip, deflate, br",
	    "accept-language": "en-US,en;q=0.9",
	    "dnt": "1",
	    "referer": "https://www.exploit-db.com/google-hacking-database",
	    "sec-fetch-dest": "empty",
	    "sec-fetch-mode": "cors",
	    "sec-fetch-site": "same-origin",
	    "sec-gpc": "1",
	    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.79 Safari/537.36",
	    "x-requested-with": "XMLHttpRequest"
	}

	response = requests.get(url, data=payload, params=querystring,headers=headers)


	for n,i in enumerate(response.json()['data']):
		soup =bs(i['url_title'],"html5lib")
		print(n+(120*k)," == ",soup.text)
		with open("dorks.txt","a") as fl:
			fl.write(soup.text+"\n")
			