import requests as  req
from threading import Thread
import concurrent.futures

lis=[]

def image(i):
	for j in range(i-6000,i):
		url="https://gql-realtime-2.reddit.com/query"
		json={"operationName":"frameHistory","variables":{"input":{"actionName":"get_frame_history","GetFrameHistoryMessageData":{"timestamp":j}}},"query":"mutation frameHistory($input: ActInput!) {\n  act(input: $input) {\n    data {\n      ... on BasicMessage {\n        id\n        data {\n          ... on GetFrameHistoryResponseMessageData {\n            frames {\n              canvasIndex\n              url\n              __typename\n            }\n            __typename\n          }\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n"}
		res = req.post(url,headers={"authorization": "Bearer 706738791396-3XlL8ehW59q9OL8gqz4C7XVemhhiTw"},json=json)
		url = res.json()['data']['act']['data'][0]['data']['frames'][0]['url']

		with open(f"rplace/{i}.png","wb") as fl:
			fl.write(req.get(url).content)


def tr(i):
	




executor = concurrent.futures.ProcessPoolExecutor(10)
futures = [executor.submit(tr, group) 
           for group in range(1648817050351,1649116967221,6000*2)]
concurrent.futures.wait(futures)

print(len(lis))