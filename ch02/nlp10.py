import pandas as pd

df = pd.read_table('popular-names.txt', sep='\t', header=None)

print(len(df))