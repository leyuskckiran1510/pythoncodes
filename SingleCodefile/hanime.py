import requests as req
import subprocess as sb








def vis_ids(page):
	vids='https://search.htv-services.com/' #method post
	json={"search_text":"","tags":[],"tags_mode":"AND","brands":[],"blacklist":[],"order_by":"created_at_unix","ordering":"desc","page":page}
	b=req.post(vids,json=json).json()['hits']
	d = b.split('slug":"')
	slugs=[]
	for i in d[1:]:
		slugs.append(i.split('","description"')[0])
	return slugs


def pics(offset):
	image_api=f'https://community-uploads.highwinds-cdn.com/api/v9/community_uploads?channel_name__in[]=media&query_method=offset&__offset={offset}&__count=50'
	res= req.get(image_api).json()
	print("Total datas => ",res['meta']['total'])
	print("Dta Showing from => ",offset," => to ",offset+res['meta']['count'] )
	for n,i in enumerate(res['data']):
		print(f"S.N *=* {offset+n} ||| Url *=* {i['url']}")
	pics(offset+96)
#pics(0)


def download(name):
	url = 'https://hanime.tv/api/v8/video?id=inkou-kyoushi-no-saimin-seikatsu-shidouroku-2&'
	res=req.get(url).json()
	return res['videos_manifest']['servers'][0]['streams'][1]['url']

b=vis_ids(1)
v=download(b[0])
with open('file.m3u8','wb') as fl:
	fl.write(req.get(v).content)
sb.call("ls")
sb.call(f"vlc file.m3u8")
