from pandas import DataFrame

# Defining the function
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


if __name__ == "__main__":

    # Dataframe with State Abbrevs -- Type = Series
    df = DataFrame({'abbrev': ['CA', 'CO', 'CT', 'DC', 'TX']})
    print(df.head())

    # Calling function and assigning it to a variable
    df2 = add_state_names(df)
    print(df2.head())
