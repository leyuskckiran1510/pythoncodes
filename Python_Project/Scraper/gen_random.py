from concurrent.futures import ThreadPoolExecutor

class Gen:

    def __init__(self,randomness=True,dim="1920/1080",num=10,key='dog'):
        import requests
        from threading import Thread
        import  queue
        import uuid
        from os import getcwd
        self.down=[]
        global error
        error=""
        global img_dimension
        q = queue.Queue()
        self.uuid=uuid
        self.queue=queue
        self.Thread=Thread
        self.error=error
        self.q=q
        self.requests=requests
        self.randomness=randomness
        self.dim=dim
        self.num=num
        self.key=key
        self.main(self.randomness,self.dim,self.num,self.key)
        
    def truerandom(self,img_dimension):
        global error
        try:
            seed=self.uuid.uuid1()
            lorem=f"https://picsum.photos/seed/{seed}/{img_dimension}"
            res=self.requests.get(lorem,allow_redirects=False)
            self.q.put(res)
            return self.contgen()
        except Exception as e:
            self.error+=str(e)+"\n"
            print(error)

    def unsplash(self,term):
        global error
        try:
            #unsplash="https://source.unsplash.com/random"
            i=f'https://source.unsplash.com/featured/?{term}'
            res=self.requests.get(i,allow_redirects=False)
            self.q.put(res)
            return self.contgen()
        except Exception as e:
            self.error+=str(e)+"\n"
            print(error)
            
            

    def contgen(self):
        har=self.q.get()
        url=har.headers['Location']
        final=self.requests.get(url)
        return  final.content
        

    def saver(self,k,random,dim,num_of_imgs,key):
        global error
        if random:
            b=self.truerandom(dim)
        else:
            b=self.unsplash(key)
        name=self.uuid.uuid1()
        if b!=None:
            with open(f"l{name}.jpg","wb") as di:
                di.write(b)
                self.down.append(name)
        else:
            self.error+="Server Responded with Null value so skipped this image => "+str(name)+"\n"


    def download(self,random,dim,num_of_imgs=10,key=''):
        threads_lis=[]
        for i in range(0,num_of_imgs):
            t=self.Thread(target=self.saver, args=(i,random,dim,num_of_imgs,key,) , daemon=True)
            t.start()
            threads_lis.append(t)
        


    def main(self,randomness,dim="1920/1080",num=10,key='dog'):
        self.download(randomness,dim,num,key)



if __name__=="__main__":
    import requests
    from threading import Thread
    import  queue
    import uuid
    import time
    from os import getcwd
    down=[]
    stat_time=time.time()
    global error
    error=""
    global img_dimension
    q = queue.Queue()
    a=input("Download from 1)Keyword\n\t2)Radnom  ")
    if a=='1':
        rand=False
        key=input("Input key Word  ")
        b="1920/1080"
    else:
        rand=True
        b=input('Image Dimension eg:::--  1920/1080  ')
        key=''
    np=input('Number of images  ')
    Gen(rand,b,int(np),key)
    
