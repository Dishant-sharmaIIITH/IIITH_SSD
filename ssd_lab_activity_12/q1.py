from datetime import datetime

fp=open("matdata.txt","r")

foot=[]
time=[]
lastpoint=-5



done=0
t=0
def findpoint(matrix,ip):
    # print(ip)
    
    global lastpoint
    global done
    global t
    for j in range(0,42):
        done=0
        for i in range(1,26):
            if(matrix[j][i]!='0'):
                if(i+1<=25 and j+1<=41 ):
                    if(matrix[j][i+1]!='0' and matrix[j+1][i]!='0'):

                        if(lastpoint<0):
                            lastpoint=j
                            t=matrix[20][0]
                           
                            

                        else:
                            if(j==lastpoint-1  ):
                                if(len(foot)==0):
                                    lastpoint=lastpoint-1
                                    foot[-1]=j
                                    time[-1]=matrix[20][0]

                                
                                elif(foot[-1]==lastpoint):
                                    lastpoint=lastpoint-1
                                    foot[-1]=j
                                    time[-1]=matrix[20][0]
                                

                            elif(j==lastpoint-2  ):
                                if(len(foot)==0):
                                    lastpoint=lastpoint-2
                                    foot[-1]=j
                                    time[-1]=matrix[20][0]
                                elif(foot[-1]==lastpoint):
                                    lastpoint=lastpoint-2
                                    foot[-1]=j
                                    time[-1]=matrix[20][0]
                                else:
                                    lastpoint=lastpoint-2
                                    foot.append(j)
                                    time.append(matrix[20][0])

                            elif(j==lastpoint-3  ):
                                if(len(foot)==0):
                                    lastpoint=lastpoint-3
                                    foot[-1]=j
                                    time[-1]=matrix[20][0]
                                elif(foot[-1]==lastpoint):
                                    lastpoint=lastpoint-3
                                    foot[-1]=j
                                    time[-1]=matrix[20][0]
                                else:
                                    lastpoint=lastpoint-3
                                    foot.append(j)
                                    time.append(matrix[20][0])

                            elif(j!=lastpoint-1 and j!=lastpoint):
                                if(len(foot)==0):
                                    foot.append(lastpoint)
                                    time.append(t)

                                elif(foot[-1]!=lastpoint):
                                    foot.append(lastpoint)
                                    time.append(t)
                                lastpoint=j
                                t=matrix[20][0]
                                
                           
                                

                                
                                
                            
                                # 
                                # print(ip)
                        done=1
                        break
            

        if(done):
            break

                    


count=0
#print("##########################################################")
str=fp.readline()
count=0
while(True):
    matrix=[]
    l=[]
    count+=1
    
    if not str:
        break
    while(len(str)!=1):
        l=str.split("\t")
        matrix.append(l)
        str=fp.readline()
        if not str:
            break
    findpoint(matrix,count)
    while(len(str)==1):
       
        str=fp.readline()
        if not str:
            break



    
    


# matrix=readmatrix()
# for line in matrix:
# print(line)
# print(ip)
# findpoint(matrix,ip)
#print(" ")

foot.append(lastpoint)
time.append(t)

# for cnt in foot:
# print(cnt)
# for cnt in time:
# print(cnt)


for i in range(len(foot)-2):
    dis=foot[i]-foot[i+2]
    sttime=time[i][0:8]
    entime=time[i+2][0:8]
    start_time = datetime.strptime(sttime, "%H:%M:%S")
    end_time = datetime.strptime(entime, "%H:%M:%S")
    timediff=end_time-start_time
    sec=timediff.total_seconds()
    if(i%2==0):
        print("stride length of left foot: ",(dis))
        print("stride velocity : ",(dis/sec)," unit/sec")
        print("cadance : ",
        (round(60/sec)*3)," steps/minute")
    else:
        print("stride length of right foot: ",(dis))
        print("stride velocity : ",(dis/sec)," unit/sec")
        print("cadance : ",
        (round(60/sec)*3)," steps/minute")

   

    







    