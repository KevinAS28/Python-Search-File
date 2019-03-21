import os
import sys
from getopt import getopt
import re




def usage():
 print("Program By Kevin Agusto")
 print("usage: ")
 print("python search.py [to-find] [location] [e or l]")
 print("python search.py [to-find]")
 print("e is mean exactly, l is mean likes")
 sys.exit(0)

try:
 location = str(sys.argv[2])
except:
 location = os.getcwd()
try:
 mode = sys.argv[3]
except:
 mode = "l"
try: 
 tofind = str(sys.argv[1])
except:
 usage()



result = []
for root, dirs, files in os.walk(location, topdown=False):
 for fname in files:
  if mode == "e":
   if fname == tofind:
    result.append(os.path.join(root, fname))
  if mode == "l":
   if re.match(tofind, fname):
    result.append(os.path.join(root, fname))
    continue
   if re.findall(tofind, fname):
    result.append(os.path.join(root, fname))
    continue
   if re.search(tofind, fname):
    result.append(os.path.join(root, fname))
    continue
 
for i in result:
 print(i)




