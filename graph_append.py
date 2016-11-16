import matplotlib
import matplotlib.pyplot as pt

x=[]
y=[]

readFile=open("coordinates.txt","r")
data=readFile.read().split("\n")

for i in data:
     val=i.split(",")
     x.append(int(val[0]))
     y.append(int(val[1]))
     


pt.plot(x,y)
pt.show()

