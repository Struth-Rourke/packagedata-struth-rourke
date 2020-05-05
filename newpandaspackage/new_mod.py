import pandas as pd
from sklearn.model_selection import train_test_split


# train_val_test Function
def train_val_test_func(df):
    ''' Takes in a dataframe and creates a training, validation, and test
    df from the existing and returns the three types'''

    # Creating a copy
    df = df.copy()
        
    # Creating a train/val/test split from df
    ## train and test split
    train, test = train_test_split(df, train_size = .9, test_size = .1, random_state = 42)

    ## train and val split
    train, val = train_test_split(train, train_size = .8, test_size = .2, random_state = 42)

    # Printing the shapes for each
    print(train.shape, val.shape, test.shape)

    # Returning the df's
    return train, val, test


# date_splitting Function
def date_splitting(Y):
    ''' Takes a column with dates and creates three new columns with different
    date types'''

    # Creating a column copy
    Y = Y.copy()
        
    # Inferring pandas datetime format
    Y['Date Column'] = pd.to_datetime(Y['a'], infer_datetime_format = True)

    # Creating new columns based on the date length (Y, M, D)
    Y['Year'] = Y['Date Column'].dt.to_period('Y')
    Y['Year_Month'] = Y['Date Column'].dt.to_period('M')
    Y['Year_Month_Day'] = Y['Date Column'].dt.to_period('D')

    return print(Y)


# add_state_names Function
def add_state_names(my_df):
    ''' Converts a dataframe with a column of state abbreviations,
    adding a corresponding column of state names

    Params:
        my_df a pandas.DataFrame with a column called "abbrev".

        Example:
        add_state_names(DataFrame({'abbrev': ['CA', 'CO', 'CT', 'DC', 'TX']}))

    Returns: a pandas.DataFrame with the original col as well as a name column
    '''

    # State Abbreviation -> Full name and Vice Versa
    # FL -> Florida

    # Creating a copy
    new_frame = my_df.copy()

    # need a list of dict with the abbrev/name mappings
    names_map = {'CA': 'Cali', 'CO': 'Colo', 'CT': 'Conn', 'DC': 'District of Columbia'}
        
    # create a new column which maps the existing column using our names map
    # breakpoint() ## Allows us to enter the script and adjust the things above it in the code
    # type(type(new_frame['abbrev'])) -> Series
    # Can use 'Dir(new_frame['abbrev'])' to see what functions/methods you can call on the particle datatype you're using

    new_frame['name'] = new_frame['abbrev'].map(names_map)

    return new_frame


# list_series_df_col Function
def list_series_df_col(lst, col_header):
    ''' Takes a list, converts it to a series and then adds it as a column
    inside a DataFrame.
    '''

    # taking in the list and converting it to a Series;
    # assigning it to variable x
    x = pd.Series(lst)

    # Creating a DataFrame
    df = pd.DataFrame(x, columns = col_header)

    return df


