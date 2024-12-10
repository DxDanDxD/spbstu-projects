import pandas as pd
from matplotlib import pyplot as plt

'''dz nomer 1

l = ["a", "a", "c", "d", "e", "f", "g"]
ls = pd.Series(l)
print(ls)'''

'''dz  nomer 2

a= pd.DataFrame({
    'l1': ["a", "b", "c", "d"],
    'l2': [ "x", "y", "z"]})
print(a)
print( a[a != a.loc[a['l1'].isin(df['l2']), 'l1'].values].dropna())'''

'''dz nomer 3

b = pd.Series(["a","a","c","d","e", "f", "g", "a", "a", "d", "d", "d", "c", "g", "g"])
print(sr)

plt.bar(sr.value_counts().index, sr.value_counts().values)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()'''

'''dz nomer 4'''

fl = pd.DataFrame({
    'l': ["a", "b", "c", "d", "e"],
    'n': [ "1", "2", "3", "4", "5"]})
print(fl)
fn = pd.DataFrame({
    'n': ["1", "2", "3", "4", "5"],
    'l': [ "a", "b", "c", "d", "e"]})
print(fn)
fnl= pd.DataFrame({
    'nl': [ "a1", "b2", "c3", "d4", "e5", "f6", "g7"]})
fnl.index.name = 'Number'
print(fnl)
fxlxn = pd.concat([fl,fn]).reset_index(drop=True)
fxnxl.index.name = 'Number'
print(fxlxn)
fxlxnxnl= pd.merge(fxlxn,fnl,how = "outer",on='Number')
print(fxlxnxnl)
