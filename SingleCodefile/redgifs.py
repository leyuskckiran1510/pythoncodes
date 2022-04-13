import requests as req

url = "https://api.redgifs.com/v2/gifs/darkinternationalmastiff/related"
url2="https://api.redgifs.com/v2/home/feeds"
url3="https://api.redgifs.com/v1/featured/categories/populated"




def related(urly):
	a = req.get(urly).json()
	#print(a)
	for i in a["gifs"]:
		aa = i['urls']['hd']
		print(aa)
	#res = req.get(aa)
	#with open("file.mp4","wb") as fl:
	#	fl.write(res.content)


def feeds(urly):
	a = req.get(urly).json()
	for j in a.keys():
		for i in a[j]:
			try:
				aa = i['urls']['hd']
				print(aa)
			except KeyError:
				pass
	return aa

def categories(urly):
	a = req.get(urly).json()
	for i in a['tags']:
		b = i['gifs'][0]['urls']['hd']
	return b
	

#related(url.replace('darkinternationalmastiff',feeds(url2).split("/")[-1].split(".")[0]))
related(url.replace('darkinternationalmastiff',categories(url3).split("/")[-1].split(".")[0]))