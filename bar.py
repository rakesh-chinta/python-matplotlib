import matplotlib.pyplot as pt
import numpy as np

pos=np.arange(6) + 0.5

names= ['raki','sam','jose','mat','bob','jack']

pt.barh(pos,(3,14,8,12,5,19),align='center',color='blue')

pt.xlabel('Height in inches',color='blue')
pt.ylabel('Students',color='blue')
pt.title('Height of the Students in inches',color='red')

pt.tick_params(axis='x',colors='black')
pt.tick_params(axis='y',colors='black')

pt.yticks(pos,names)

pt.subplots_adjust(left=.11,bottom=.12,right=.94)

pt.show()
