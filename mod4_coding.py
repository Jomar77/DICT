import pandas as pd
import matplotlib.pyplot as plt

ds = pd.read_csv('population_by_country_2020.csv')

sb = ds[ds["Country"].isin(['China', 'Macau', 'Hong Kong', 'Taiwan', 'South Korea', 'Japan', 'Mongolia', 'North Korea', 'Tibet', ])]

cntry = sb["Country"]
pop = sb["Population (2020)"]

fig = plt.figure(figsize=(16,10))

plt.barh(cntry, pop, color='green')
plt.title("Population of East Asia")

plt.show()