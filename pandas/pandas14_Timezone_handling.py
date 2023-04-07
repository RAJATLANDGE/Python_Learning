import pandas as pd


df = pd.read_csv("microsoft data - Copy.csv", header=2, index_col="Date Time", parse_dates=True)
print(df)
df.columns = ["Date Time"]





