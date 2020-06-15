import pandas as pd

df = pd.read_csv('popular-names.txt', delim_whitespace=True, header=None)
df.to_csv('ans11.txt', sep=' ', index=False, header=None)

# df = pd.read_csv('ans11.txt', delim_whitespace=True, header=None)