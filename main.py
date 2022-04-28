import time
import random
from links import youtube_links
link1 = 1
link2 = 0
def printLinks():
 while link1 > link2:
   time.sleep(10)
   print(random.choice(youtube_links))
 return
printLinks()