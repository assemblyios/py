
import qrcode
from PIL import ImageGrab

def pic():
	for x in xrange(1,1000000):
		img  = qrcode.make('rewqrewfdafdafjlwjoeueourqoueuroeq44324')
		img.save('./image/rewqresss%s.png'%x)
		print 'di====%s=====ge'%x
	print 'finish'

def screen():
	bbox = (760, 0, 1160, 1080) 
	for x in xrange(1,1000):
		img  = ImageGrab.grab(bbox)
		img.save('./image/rewqresss%s.png'%x)
		print 'di====%s=====ge'%x
	print 'finish'



if __name__ == '__main__':
   #pic()
   screen()

