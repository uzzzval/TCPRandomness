#import csv
import MySQLdb
#from numpy.core.defchararray import str_len

fileString=""
with open("/Users/ujjawalsharma/Desktop/Dump/RandomOutput.txt", 'r') as fin:
    for line in fin:
        fileString=fileString+line  
fin.close()

conn = MySQLdb.connect(host= "localhost",user="root",passwd="root",db="randomhashes")
x = conn.cursor()


i=0;
j=255;
#print str_len(fileString)
while fileString[1:-1]:
    localHash = fileString[i:j]
    try:
        #print localHash
        #print localHash
        sql = ("SELECT hashes FROM random_hash_table WHERE hashes='"+localHash+"'")
        result = x.execute(sql)
        if result==1:
            print localHash + "Already Exists"
        else:
            sql="INSERT INTO random_hash_table VALUES ('"+localHash+"')"
            x.execute(sql)
            conn.commit()
    except:
        conn.rollback()
    i=i+256
    j=j+256
    #print i
    #print j
#print "2"
conn.close()
