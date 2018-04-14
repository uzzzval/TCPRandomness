#!/usr/bin/python
# -*- coding: utf-8 -*-


fileString=""
with open("/Users/ujjawalsharma/Desktop/Dump/Dump.csv", 'r') as fin:
    for line in fin:
        if "0x" in line:
            line=line.replace(" ","").lstrip().rstrip()
            line=line[7:39]
            line=line.replace("0","").replace(".","").replace("f","").replace("{","").replace("}","").replace("[","").replace("]","").replace(",","").replace("'","")
            fileString=fileString+line   
fin.close()


f = open('/Users/ujjawalsharma/Desktop/Dump/RandomOutput.txt', 'w')
f.write(fileString)
f.close()

#print fileString
