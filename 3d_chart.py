from mpl_toolkits.mplot3d import axis3d
import matplotlib.pyplot as pt

fig=pt.figure()
chart=fig.add_subplot(1,1,1,projection='3d')

X,Y,Z=[1,2,3,4,5,6,7,8,],[2,4,6,7,8,9,7,3],[4,5,6,8,9,2,3,1]
X1,Y1,Z1=[-1,-2,-3,-4,-5,6,7,8],[-2,-4,-6,-7,-8,9,7,3],[-4,-5,-6,-8,-9,2,3,1]
chart.scatter(X,Y,Z,color='red',marker='o')
chart.scatter(X1,Y1,Z1,color='blue',marker='^')

chart.set_xlabel("x axis")
chart.set_ylabel("y axis")
chart.set_zlabel("z axis")


pt.show()
