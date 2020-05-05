import pandas as pd
from newpandaspackage.new_mod import train_val_test_func, date_splitting

## Function 1
# Mock df for train_val_test_func function
dfx = pd.DataFrame({'a': [1,2,3,4,5,6,7,8,9,10], 'b': [1,2,3,4,5,6,7,8,9,10]})

# Calling function on above df
train_val_test_func(dfx)


## Function 2
# Mock df for date_splitting function
dfz = pd.DataFrame({'a': ['01/01/2019', '01/02/2019', '01/03/2019']})

# Calling function on above df
date_splitting(dfz)

