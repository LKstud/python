import os
import math
def readfile(filename):
    x=[]
    with open (filename,'r') as op:
        rr = op.readlines()
    for i in rr:
        x.append(float(i))
    return x
def min1(m):
    mn=m[0]
    for i in m:
        if i<mn:
            mn=i
    return mn
def max1(m):
    mx=m[0]
    for i in m:
        if i>mx:
            mx=i
    return mx
def mid(m):
    s=0
    for i in m:
        s+=i
    md=s/len(m)
    return md
def med(m):
    sorted_m=sorted(m)
    if len(m)%2!=0:
        median = sorted_m[len(m)//2]
        return median
    else:
        ind1 = len(m)//2-1
        ind2=ind1+1
        num1=sorted_m[ind1]
        num2=sorted_m[ind2]
        median = mid([num1,num2])
        return median
def stats(m):
    mn = min1(m)
    mx = max1(m)
    md=mid(m)
    median=med(m)
    return {"mean":md,"max":mx,"min":mn,"median":median}
#создадим папку
if not os.path.isdir('stats'):
    os.mkdir('stats')
#напишем функцию, которая позволдит получить список файлов в папке в массив
def getfilenames(dir):
    inm=os.listdir(dir)
    m=[]
    for i in inm:
        fullpath = os.path.join(dir,i)
        if os.path.isfile(fullpath) and i.endswith('.dat'):
            m.append(i)
    return m
datfiles = getfilenames('.')
num=0
#для каждого отдельного файла создадим отдельный файл и поместим его в нужную папку
for file in datfiles:
    num+=1
    newfilename = str(num)+'_'+file
    newfilecontent = []
    newfilecontent.append(file)
    oldfilecontent=[]
    with open(file) as op:
        rr = op.readlines()
        for i in rr:
            oldfilecontent.append(float(i))
    filestats=stats(oldfilecontent)
    for key,value in filestats.items():
        newfilecontent.append(f"{key}: {value}")
    newfile = open(f'stats/{newfilename}','w')
    for i in newfilecontent:
        newfile.write(i+'\n')


