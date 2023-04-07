import pandas as pd
# help in generate contingency table or crosstabs that is provide frequency distribution by crosstab

df = pd.read_excel("pandas_crosstab.xlsx")
print(df)

# df = df.rename(columns={'Nationality ': 'Nationality'})

ctab = pd.crosstab(df.Sex, [df.Handedness,df.Nationality],margins=True)            # margin give total in row and columns
print(ctab)

ctab1 = pd.crosstab(df.Sex,df.Handedness)
print(ctab1)

ctab2 = pd.crosstab(df.Sex,df.Handedness,normalize="index")                          #pycham shortcut for documentation = cntl + Q
print(ctab2)                                                                   # normalize give percentage value of give element
'''
normalize= index - normalize over all values
normalize= True or all - normalize over each row
normalize = columns - normalize over each columns
margin = True - will also normalize margin values'''

import numpy as np
ctab3 = pd.crosstab(df.Sex,df.Handedness, values = df.Age, aggfunc=np.average)
print(ctab3)                            #aggfunc give average of element pass in "values"