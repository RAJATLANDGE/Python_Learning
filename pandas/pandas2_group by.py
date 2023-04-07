import pandas as pd

df = pd.read_csv("Tutorial 7 - group by.csv")
print(df)

g = df.groupby("city")                      # give generator type object
print(g)

for city, city_df in g:                      # by using genrator type object we access g.
    print(city)                                #--  print city name
    print(city_df)                              #-- print given city dataframe

print(g.get_group("mumbai"))                  # print specific group

print(g.max())
# from top to bottam we called as split-apply-combine
import seaborn as sns
import matplotlib.pyplot as plt
print(g.mean())
print(g.describe())
print(sns.pairplot(g.max()))
plt.show()

# import pandas as pd
# import numpy as np
# print("______________________")
# p = pd.Series(np.random.normal(14, 6, 22))
# print(p)


