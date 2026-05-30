from typing import Union
def convert_value(value:str)-> Union[str,int,float]:
    if value=="":
        return ""
    #проверка на int
    if value.startswith('-'):
        nvalue=value[1:]
        if nvalue.isdigit():
            return int(value)
    else:
        if value.isdigit():
            return int(value)
    #проверка на float
    tmp = value
    if tmp.startswith('-'):
        tmp=tmp[1:]
    if tmp.count('.')==1:
        tmp=tmp.replace('.','')
        if tmp.isdigit():
            return float(value)
    return value
def removedataset(string:str):
    isNumber=False
    replacestr=''
    for i in string:
        if isNumber==False:
            if i!=' ':
                isNumber=True
            replacestr+=i
        else:
            break
    string=string.replace(replacestr,'')
    return string

with open ("PR25.IB051630_11.txt","r") as op:
    rr=op.readlines()
afterdatasets=False
aftertypes=False
mainblock=False
data=[]
for i in rr:
    if 'г.' in i:
        date = i.strip()
    if "; Datasets" in i:
        i=i.replace("; Datasets","")
        columnnames = i.split()
        afterdatasets=True
    elif afterdatasets:
        i=i.replace(";","").replace("[","").replace("]","")
        typenames=i.split()
        afterdatasets=False
        aftertypes=True
    elif aftertypes:
        tmp = i.split()
        if tmp[0].isdigit():
            mainblock=True
    if mainblock:
        tmp=i.split()
        ntmp=[]
        for j in tmp:
            ntmp.append(convert_value(j))
        data.append(ntmp)
ndata=[]
for i in data:
    i=i[1:]
    ndata.append(i)
info={"date":date,"names":columnnames,"types":typenames,"data":ndata}
print(info)
columns={}
for i in range(len(columnnames)):
    type=typenames[i]
    coldata=[]
    for j in ndata:
        coldata.append(j[i])
    columns[columnnames[i]]={"type":type,"values":coldata}
#получить по имени столбца единицы измерения и список значений можно через словарь columns
print(info["names"])
print(columns["Press2"])