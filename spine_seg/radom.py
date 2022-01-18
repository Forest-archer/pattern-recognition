import random
from datetime import datetime
'''file=input("input file name")
num=input("class num")'''
file="mix01.pts"
num=6
f=open(file,'r')
points=f.read()
f.close()
classnum=[]
sample=[]
for i in range(0,int(num)):
    classnum.append([])
    sample.append([])

point=points.split("\n")
for i in range(0,len(point)-1):
    seg=point[i].split(" ")
    #print(seg[3])
    classnum[int(float(seg[3]))-1].append(i)

total=8000
point_sum = 0
length=0
for i in range(0,int(num)):
    bound=round(len(classnum[i])/48000,3)
    count=0
    if i+1==2 or i+1==3:
        bound_num=bound*total+4
    else:
        bound_num=bound*total
    #
    while len(sample[i])<bound_num:
        print("len of sample "+str(i)+":"+str(len(sample[i])))
        select=random.randint(0,1)
        if select == 1:
            if classnum[i][count]!=None:
                sample[i].append(classnum[i][count])
                classnum[i][count]=None
        if count < (len(classnum[i])-1):
            count+=1
        else:
            count=0
    #
    point_sum=point_sum+(bound_num)
    print("類別取點:"+str(int(bound_num)))
    print("總取點:"+str(int(point_sum)))
    print("剩餘點:"+str(int(total-point_sum)))
    #while len(sample)
    length=length+len(sample[i])
additional=8000-length
if length<8000:
    print("point is not enough!!")
    print("about :"+str(additional))
else:
    print("total num:"+str(length))
    print("check over")
#print(sample)
now = datetime.now()
dt_string = now.strftime("%Y%m%d_%H%M%S")
lines=[]
o=open("auto_8000/s_8000_"+dt_string+".pts",'w')
for i in range(0,int(num)):
    for j in range(0,len(sample[i])):
        lines.append(point[sample[i][j]]+"\n")
o.writelines(lines)
o.close()