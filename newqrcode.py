
import qrcode

def pic():
	for x in xrange(1,1000):
		img  = qrcode.make('rewqrewfdafdaf33333jlwjoeueourqoueuroeq44324')
		img.save('../image/rewqresss%s.png'%x)
		print 'di====%s=====ge'%x
	print 'finish'



if __name__ == '__main__':
   pic()


