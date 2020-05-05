import pandas as pd
from newpandaspackage.new_mod import train_val_test_func, date_splitting, add_state_names, list_series_df_col

## Function 1 (train_val_test_func)
# Mock df
dfx = pd.DataFrame({'a': [1,2,3,4,5,6,7,8,9,10], 'b': [1,2,3,4,5,6,7,8,9,10]})

# Calling function
train_val_test_func(dfx)



## Function 2 (date_splitting)
# Mock df
dfy = pd.DataFrame({'a': ['01/01/2019', '01/02/2019', '01/03/2019']})

# Calling function
date_splitting(dfy)



## Function 3 (add_state_names)
# Mock df
dfz = DataFrame({'abbrev': ['CA', 'CO', 'CT', 'DC', 'TX']})
print(df.head())

# Calling and assigning function
df2 = add_state_names(df)
print(df2.head())


## Function 4 (list_series_df_col)
# Mock df
dfq = [1, 2, 3, 4, 5]
# Mock header
header = 'Numbers'

# Calling and printing the Function
print(list_series_df_col(dfq, header))


## Class / Methods / Functions