import matplotlib
import matplotlib as pt
x=[1,2,3,4]
y=[3,6,4,8]

pt.plot(x,y)
pt.show()

fig=pt.figure()
rect=fig.patch()
rect.set_facecolor('red')

x1=[1,2,3,4]
y1=[3,6,7,9]
x2=[2,3,4,5]
y2=[4,7,8,10]

graph1=fig.add_subplot(2,1,1,axisbg='black')
graph1.plot(x1,y1,'white',linewidth=2.0)

graph1.tick_params(axis="x",color="white")
graph1.tick_params(axis="y",color="white")

graph1.spines["top"].set_color('w')
graph1.spines["bottom"].set_color('w')
graph1.spines["left"].set_color('w')
graph1.spines["right"].set_color('w')

graph1.set_title("random graph",color="white")
graph1.set_xlabel("X axis",color="white")
graph1.set_ylabel("Y axis",color="white")

graph2=fig.add_subplot(2,1,2,axisbg='black')
graph2.plot(x,y,'red',linewidth=2.0)

graph2.tick_parems(axis="x",color="white")
graph2.tick_parems(axis="y",color="white")

graph2.spines["top"].set_color('w')
graph2.spines["left"].set_color('w')
graph2.spines["right"].set_color('w')
graph2.spines["bottom"].set_color('w')

graph2.set_title("random graph",color="white")
graph2.set_xlabel("X axis",color="white")
graph2.set_ylabel("Y axis",color="white")

pt.show()
