import unittest

from newpandaspackage.new_mod import StateWrangle

class TestStateWrangle(unittest.TestCase):

    # Defining the function
    def test_add_state_names(self):
        x = StateWrangle(
            lst1=['NY', 'NJ', 'CT', 'RI', 'VT'],
            lst2=[1, 2, 3, 4, 5], 
            col_headers=['Ab', 'Name', 'Number']
            )

        # Test add_state_names
        lst3 = x.add_state_names()
        self.assertEqual(len(lst3), 5)

        # Test list_series_df_col
        df = x.list_series_df_col()
        self.assertEqual(len(df.columns), 3)


if __name__ == '__main__':
    unittest.main()
