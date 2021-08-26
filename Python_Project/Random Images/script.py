import requests
from threading import Thread
import  queue
import uuid
import time
from os import getcwd

print("\n"*3)
down=[]
stat_time=time.time()
global error
error=""
global img_dimension
img_dimension="1920/1080" ## width/height  #width/ for square image
q = queue.Queue()
def urlgen():
    global error
    try:
        unsplash="https://source.unsplash.com/random"
        seed=uuid.uuid1()
        lorem=f"https://picsum.photos/seed/{seed}/{img_dimension}"
        res=requests.get(lorem,allow_redirects=False)
        q.put(res)
        return contgen()
    except Exception as e:
        error+=str(e)+"\n"
        
        

def contgen():
    har=q.get()
    url=har.headers['Location']
    #new_url=url.split("?")[0]
    final=requests.get(url)
    return  final.content
    

def saver(k):
    global error
    b=urlgen()
    #name=hashlib.md5(b)
    #name=name.hexdigest()
    name=uuid.uuid1()
    if b!=None:
        with open(f"l{name}.jpg","wb") as di:
            di.write(b)
            print("\r[-] DOWNLODED => ",f"{name}    ",end="")
            down.append(name)
    else:
        error+="Server Responded with Null value so skipped this image => "+str(name)+"\n"
    
threads_lis=[]

num_of_imgs=200
for i in range(0,num_of_imgs):
    print("\r[*]Downloading   ",end="")
    t=Thread(target=saver, args=(i,) , daemon=True)
    t.start()
    threads_lis.append(t)

#print("Afetr thread gen finihed,it took ",time.time()-stat_time)
for n,i in enumerate(threads_lis):
    #print("thread joining SN {n} statred..",time.time()-stat_time)
    i.join()

print("\n"*3)
print(f'''                ##############################################################################\n\n
                    TOOK {time.time()-stat_time} sec to download {len(down)} images of {img_dimension} dimension
                                            but given num of image was {num_of_imgs} sorry for some loss if any.
                ''')
print(f"                \t  [+] Image stored in {getcwd()}  ")
print("\n"*3)
print("\tTotal Error Occured are listed below \n\t",error)
