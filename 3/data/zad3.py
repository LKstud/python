import os
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
def readfiles(filepath:str,delimiter:str=",",has_header:bool=True):
    with open (filepath,"r") as op:
        rr=op.readlines()
    for i in range(len(rr)):
        rr[i]=rr[i].strip()
    if has_header:
        headers=rr[0].split(delimiter)
        rr=rr[1:]
    #определим тип каждого столбца
    exmp=rr[0].split(delimiter)
    typelist=[]
    stringlist=[]
    for i in exmp:
        typelist.append(type(convert_value(i)))
    for i in rr:
        nstring=i.split(delimiter)
        changedstring=[]
        for j in nstring:
            changedstring.append(convert_value(j))
        stringlist.append(changedstring)
    if has_header:
        return{
            "header":headers,
            "data":stringlist,
            "types":typelist
        }
    else:
        return {
            "data": stringlist,
            "types": typelist
        }
print(readfiles("csv_20260206_08a514.txt"))