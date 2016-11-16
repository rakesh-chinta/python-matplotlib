import matplotlib.pyplot as pt
sizes=[40,27,20,10,3]
labels=['android','apple','windows','nokia','xiami']
colors=["yellow","orange","red","blue","green"]


pt.pie(sizes,colors=colors,startangle=90,labels=labels)
pt.title("pie chart")
pt.legend(title='Legend',loc='lower left')
pt.axis('equal')
pt.show()
