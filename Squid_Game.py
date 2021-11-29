import time
import random
from multiprocessing import Process
import keyboard

def Start(t):
	t=int(t)
	key=[]
	
	while t:
		rand=random.randint(0,t)
		mins, secs = divmod(int(t), 60)
		timer = '{:02}:{:02}'.format(mins, secs)
		print(timer, end="\r")
		if keyboard.read_key() == 'alt':  
	 			key.append('q')
		if rand == t:
				print('stoping')
				time.sleep(0.25)
				if keyboard.read_key() == 'alt':  
					print('You Lose : ' + str(len(key)))
					break
				else:
					continue
		
		if (len(key)/5) == 5:
			print('You Win :' + str(len(key)))
			break

		time.sleep(1)
		t -= 1

	print('stop')

if __name__ == '__main__':

	p1= Process(target=Start,args=(10,))
	p1.start()
	p1.join()