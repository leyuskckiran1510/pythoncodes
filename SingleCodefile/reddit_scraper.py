import requests as req


subreddit_name='nepal'
typ=['new','hot']
after=''

dirt=''':authority: gateway.reddit.com
:method: GET
:scheme: https
accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
accept-encoding: utf-8
accept-language: en-US,en;q=0.9
dnt: 1
sec-fetch-dest: document
sec-fetch-mode: navigate
sec-fetch-site: none
sec-fetch-user: ?1
sec-gpc: 1
upgrade-insecure-requests: 1
user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.79 Safari/537.36'''


headers={}
for i in dirt.split("\n"):
	#print(i.split(":")[-2].strip())
	headers[i.split(":")[-2].strip()]=i.split(":")[-1].strip()

def get(name,typ,after):
	urly=f'https://gateway.reddit.com/desktopapi/v1/subreddits/{subreddit_name}?allow_over18=1&sort={typ[0]}&after={after}'
	b = req.get(urly,headers=headers).json()
	print(urly)
	for i in b['posts'].keys():
			try:
				c = b['posts'][i]['media']['content']
				print(c)#c)
			except Exception as e:
				print(e)

	token = b['token']
	return
	get(name,typ,token)
	



get(subreddit_name,typ,after)