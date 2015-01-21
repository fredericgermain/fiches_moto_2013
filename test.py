#/usr/bin/python
import os;
import sys;
import random;

random.seed(None) 
if len(sys.argv) == 1:
 test = random.randrange(1,13)
else:
 test = int(sys.argv[1])
 
with open("fiches/%d.txt"% (test) ) as f:
 sys.stdout.write("test-%d " % (test))
 for line in f.readlines():
  sys.stdout.write(line.rstrip())
  sys.stdin.read(1)

