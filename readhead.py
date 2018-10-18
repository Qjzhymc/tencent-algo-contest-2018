import os
filename=r"C:\Users\22467\Desktop\腾讯2018广告算法大赛\preliminary_contest_data\userFeature.data"
f=open(filename)
index=0
for line in f.readlines():
	index+=1
	line=line.replace("\n","")
	print(line)
	if index==100:
		break
f.close()