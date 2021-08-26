import dpkt
import socket



#url="https://ip-geolocation.whoisxmlapi.com/api/web"
#payload={"search":"151.101.194.137","web-lookup-search":true,"g-recaptcha-response":null}
'''headers={'authority': 'ip-geolocation.whoisxmlapi.com',
         'method': 'POST',
         'path': '/api/web',
         'scheme': 'https',
         'accept': 'application/json, text/plain, */*',
         'accept-encoding': 'gzip, deflate, br',
         'accept-language': 'en-US,en;q=0.9',
         'content-length': '81',
         'content-type': 'application/json;charset=UTF-8',
         'cookie': 'cf_12389_id=aa199eae-2a72-4235-b22b-a348c60a9091; \
            whoisxmlapi-privacy-cookie=true; cf_12389_person_last_update=1629784655227;\
            XSRF-TOKEN=eyJpdiI6IlhYM21SVkV6ZVpCXC9Ld1VhSms2dDZnPT0iLCJ2YWx1ZSI6IlB0RTlc\
            L1cxMDNzZTgyNzBKcXkxNzIxQWhLQ2hqOGxuUzRVYm1XSXFDcjR0eUNwXC83RVRvT0JEbzFo\
            YXVJU2N4TyIsIm1hYyI6IjlmOGVkM2ZmYWI1NjlmYjc2YWEzYmFkNDcxMWJkNDE2MzdkNWU0Y\
            TQyZjE3NDY4ZjkyZmRlOWM1YmIwYzFlM2IifQ%3D%3D; emailverification_session=eyJpdiI6IlVCe\
            VdYM0gycFwvR0EzVUlsZ3lQdStnPT0iLCJ2YWx1ZSI6Ik9lRkUwbE5lTWtQXC9XOWc1S2p4S2I3UW\
            ZNdXJGVU14K3R1Q2VySnpFQ0FES3BmVVwvME9zQlNtN3M5OVVXcVlpS3h0blF5TlJyVUFBcitF\
            NmdQUHJSK25cL2JCbU5wdVpkck4zMGw5Z3BVcXFUOXJcL25ndnNHck1JaXZzaEx4NFVmMiIsIm\
            1hYyI6ImRlMDY2Mjk0ZTRiZDA2MGM3NjAzNmQ3YjVmNjRlYThhM2MzOGY3YTZkZjk5MTBjYjViMm\
            VhODNiNTJmOTg0MmYifQ%3D%3D',
         'origin': 'https',
         'referer': 'https',
         'sec-fetch-dest': 'empty',
         'sec-fetch-mode': 'cors',
         'sec-fetch-site': 'same-origin',
         'sec-gpc': '1',
         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36',
         'x-csrf-token': 'pKhj1fVHK8wUu7tDqTXArg6Vudnx8eBFfBuIzMf9',
         'x-requested-with': 'XMLHttpRequest'}

'''
def printPcap(pcap):
    src_lis=[]
    des_lis=[]
    for (ts,buf) in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            src = socket.inet_ntoa(ip.src)
            dst = socket.inet_ntoa(ip.dst)
            src_lis.append(src)
            des_lis.append(dst)
            #print ('Source: ' +src+ ' Destination: '  +dst)
            #ip='192.168.0.6'
            #if src==ip  or dst==ip:
                #print('Jenisha network activity',src,"\t=> ",dst)

        except:
            pass
    print(set(src_lis),set(des_lis))

def main():
	f = open('freefiree.pcap','rb')
	pcap = dpkt.pcap.Reader(f)
	printPcap(pcap)

if __name__ == '__main__':
	main()
