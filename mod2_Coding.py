import statistics as stat
import numpy as np
from scipy import stats as st

lst = [103,105, 176,188,146,184,175, 112,115,163]

mn = np.mean(lst)
md = st.mode(lst)
mdn = np.median(lst)

sd = round(np.std(lst,ddof = 1),2)
v = round(np.var(lst,ddof = 1),2)
r = np.ptp(lst)

print("Mean: ", mn)
print("Mode: ", md)
print("Median: ", mdn)
print("Standard Deviation: ", sd)
print("Variance: ", v)
print("Range: ", r)

"""
lst = [89,90,91,90,85,91,88,87,80,81,76,85,87,88,82,95,88,82,85,84]
a = stat.mean(lst)
b = stat.median(lst)
c = stat.mode(lst)

print("Your average expense is: " , a)
print("Your median expense is: " , b)
print("Your mode expense is: " , c)
for num in range(5):
     s = int(input("your expenses for each day of the week:"))
     lst.append(s)
    

def ave(i):
    print("Your average expense is: " , i)

res = 0
for num in lst:
    res += num
avg = res/5

ave(avg)

"""

