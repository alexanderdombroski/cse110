import pandas as pd

df = pd.read_csv("life-expectancy.csv")

first_10 = df.head(10)

avg_life_each_country = df.drop(columns=['Code','Year']).groupby(["Entity"]).mean()
avg_life = df.drop(columns=['Code','Year','Entity']).mean()

print(avg_life_each_country)
# print(first_10)