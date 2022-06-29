# DemoFile1.py
import sys

print("welcom to",'pyton',sep='~', end='!',file=sys.stderr)

f=open("c:\\work\demo.txt",'wt')
print('file write', file=f)
f.close()

