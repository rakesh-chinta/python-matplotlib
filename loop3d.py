from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as pt
import numpy as np

fig=pt.figure()

chart=fig.add_subplot(1,1,1,projection='3d')
x,y,z=axes3d.get_test_data(0.05)
chart.plot_wireframe(x,y,z,rstride=1,cstride=1) 

chart.set_xlabel("x axis")
chart.set_ylabel("y axis")
chart.set_zlabel("z axis")

pt.show()
 
