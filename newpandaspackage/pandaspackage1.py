import pandas as pd

#import my_mod import enlarge
from newpandaspackage.my_mod import enlarge



print("Hello World")

print(2 + 2)

df = pd.DataFrame({'a':[1,2,3], 'b':[4,5,6]})
print(df.head())

z = input('Please choose a number to enlarge: ')
print(enlarge(z))