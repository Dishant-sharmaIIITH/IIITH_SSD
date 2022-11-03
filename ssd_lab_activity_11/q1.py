import csv
from functools import reduce           #######################Q1

stockrecord=[]
with open('lab_11_data.csv', mode ='r')as file:
        csvFile = csv.reader(file)
        for lines in csvFile:
            stockrecord.append(lines[0:7])


###############################################################..............Q2
stockrec=[]

stockrec=list(filter(lambda x:(float(x[6])>-3.0),stockrecord[1:]))

for i in range(len(stockrec)):
    print(stockrec[i])
print(len(stockrec))
#################################################################..............Q3

Open=[]
for it in stockrec:
    Open.append(float(it[1].replace(",","")))
OpenSum = reduce(lambda a,b:a+b,Open)

oavg=OpenSum/len(Open)

High=[]
for it in stockrec:
    High.append(float(it[2].replace(",","")))
HighSum = reduce(lambda a,b:a+b,High)
havg=HighSum/len(High)

Low=[]
for it in stockrec:
    Low.append(float(it[3].replace(",","")))
LowSum = reduce(lambda a,b:a+b,Low)
lavg=LowSum/len(Low)

res="Open "+str(oavg)+"\n"+"High "+str(havg)+"\n"+"Low "+str(lavg)+"\n"

text_file = open("avg_output.txt", "w")
text_file.write(res)

text_file.close()

#########################################################################........Q4,,Q5

searchres=[]
ip=input()
for it in stockrec:
    if(it[0][0]==ip):
        searchres.append(it)

text_file = open("stock_output.txt", "w")
for itr in searchres:
    resstr=' '.join([str(elem) for elem in itr])
    resstr+="\n"
    text_file.write(resstr)

text_file.close()



##################################################################
