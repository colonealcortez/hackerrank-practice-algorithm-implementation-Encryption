#exclusive solution by HIMANSHU!
import math
import textwrap
a=input()
b=len(a)
x=math.floor(math.sqrt(b))
y=math.ceil(math.sqrt(b))
if (abs(x**2-b)<abs(y**2-b)):
  e=x
else:
  e=y

d=list(textwrap.wrap(a,e))
k=''.join(d)
l=[]
for i in range(0,len(d)):
  l.append(k[i::(len(d))])
print(' '.join(l))

