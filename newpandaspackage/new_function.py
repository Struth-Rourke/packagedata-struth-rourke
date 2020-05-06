from pandas import DataFrame


class Wrangler(object):
    '''
    Wrangler takes a dataframe and manipulates it
    '''
    def __init__(self, my_df):
        '''
        Params:
            my_df a pandas.DataFrame with a column called "abbrev".
            
            Example:
            add_state_names(DataFrame({'abbrev': ['CA', 'CO', 'CT', 'DC', 'TX']}))
        
        '''
        self.df = my_df

    # Defining the function
    def add_state_names(self):
        ''' Converts a dataframe with a column of state abbreviations,
        adding a corresponding column of state names

        Returns: a pandas.DataFrame with the original col as well as a name column
        '''

        # State Abbreviation -> Full name and Vice Versa
        # FL -> Florida

        # need a list of dict with the abbrev/name mappings
        names_map = {'CA': 'Cali', 'CO': 'Colo', 'CT': 'Conn', 'DC': 'District of Columbia'}
            
        # create a new column which maps the existing column using our names map
        # breakpoint() ## Allows us to enter the script and adjust the things above it in the code
        # type(type(new_frame['abbrev'])) -> Series
        # Can use 'Dir(new_frame['abbrev'])' to see what functions/methods you can call on the particle datatype you're using

        self.df['name'] = self.df['abbrev'].map(names_map)


    # Defining a function
    def inspect_columns(self):
        print(self.df.columns)





if __name__ == "__main__":

    # # Dataframe with State Abbrevs -- Type = Series
    # df = DataFrame({'abbrev': ['CA', 'CO', 'CT', 'DC', 'TX']})
    # print(df.head())

    # # Calling function and assigning it to a variable
    # df2 = add_state_names(df)
    # print(df2.head())


    df = DataFrame({'abbrev': ['CA', 'CO', 'CT', 'DC', 'TX']})
    print(df.head())

    
    wrangler = Wrangler(df)
    print(type(wrangler))
    wrangler.inspect_columns()
    wrangler.add_state_names()
    print(wrangler.df.head())