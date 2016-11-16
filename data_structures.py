import pandas as pd
data={
    'students':["rakesh", "matt", "mark","james","clark"],
    'math': [98, 83, 66, 56, 78],
    'science': [96, 54, 75, 87, 57],
    'sports': ["basketball","swimming","table tennis","shuttle","tae kwon do"]
    }

students=pd.DataFrame(data, columns=["students","math","science","sports"])
print(students)
    
