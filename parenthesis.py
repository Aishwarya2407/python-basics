a=input()
t=0
for i in a:
    if(i=="{"):
       t+=1
    if(i=="["):
       t+=1
    if(i=="("):
       t+=1
    if(i=="}"):
       t-=1
    if(i=="]"):
       t-=1
    if(i==")"):
       t-=1
if(t==0):
   print("p")
else:
   print("n")
