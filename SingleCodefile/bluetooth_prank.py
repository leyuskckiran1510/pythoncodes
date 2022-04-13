import subprocess
import time
import os,sys,time,pexpect



def main():
	print("Now playing audio or any other things")
	try:
		card = 'bluez_sink.'+subprocess.Popen('pactl list',shell=True,stdout=subprocess.PIPE).stdout.read().decode().split('bluez_card.')[1].split('\n')[0]+'.a2dp_sink'
		code=f'paplay -p --device={card} /home/kiran/Music/Beat/aliens_game_over2.wav'
	except IndexError:
		print("Please Run `bluetoothctl scan on`")



	def play():
		subprocess.call(code,shell=True)



	def run():
		for i in range(0,10):
			play()
		
	run()
	end = subprocess.Popen('bluetoothctl disconnect',shell=True,stdout=subprocess.PIPE).stdout.read().decode()


	id = end.split('Device ')[1].split(' ServicesResolved')[0]

	while True:
		a=input('Continue the attack  ')
		if a!='y':
			break
		subprocess.call(f'bluetoothctl connect {id}',shell=True)
		time.sleep(3)
		run()


def findaddress():
  address=''
  p = pexpect.spawn('bluetoothctl scan on', encoding='utf-8')
  p.logfile_read = sys.stdout
  mylist = ['(Device )[0-9A-F].[:][0-9A-F].[:][0-9A-F].[:][0-9A-F].[:][0-9A-F].[:][0-9A-F].',pexpect.EOF]
  p.expect(mylist)
  address=p.after
  if address==pexpect.EOF:
    return ''
  else:
    return address.split('Device ')[1]

def setbt(address):
  response=''
  p = pexpect.spawn('bluetoothctl', encoding='utf-8')
  p.logfile_read = sys.stdout
  p.expect('#')
  p.sendline("remove "+address)
  p.expect("#")
  p.sendline("scan on")

  mylist = ["Discovery started","Failed to start discovery","Device "+address+" not available","Failed to connect","Connection successful"]
  while response != "Connection successful":
    p.expect(mylist)
    response=p.after
    p.sendline("connect "+address)
    time.sleep(1)
  p.sendline("quit")
  p.close()
  #time.sleep(1)
  return


address='' 
while address=='':
  address=findaddress()
  #time.sleep(1)
  
print (address," found")
setbt(address)
print("Verifying the connection...")
time.sleep(3)
main()