import pandas as pd
from sklearn.model_selection import train_test_split



if __name__ == "__main__":
    # Train , Val, Test Function
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


if __name__ == "__main__":
    # Date Splitting Function
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


