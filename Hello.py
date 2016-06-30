import threading
import time
import sys

def printit():
	print "Hello"
	
def runthread():
	cnt=0
	while cnt < 5:
		t=threading.Thread(target=printit);
		t.start()
		cnt=cnt+1
		time.sleep(5)
	sys.exit()
		
runthread()

#commit 222
