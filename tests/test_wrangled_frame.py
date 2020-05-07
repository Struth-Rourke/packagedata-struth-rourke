import unittest

# Importing the necessary packages
from newpandaspackage.new_function import WrangledFrame

class TestStateWrangled(unittest.TestCase):

    def test_add_state_names(self):
        wf = WrangledFrame({'abbrev': ['CA', 'CO', 'CT', 'DC', 'TX']})
        self.assertEqual(list(wf.columns), ['abbrev'])
        self.assertEqual(len(list(wf.columns)), 1)


        wf.add_state_names()
        # ensure there is a 'name' column
        self.assertEqual(list(wf.columns), ['abbrev', 'name'])
        self.assertEqual(len(list(wf.columns)), 2)
        # ensure the value of the WF are specific classes or values (str, 'Cali')
        self.assertEqual(wf['name'][0], 'Cali')
        self.assertEqual(wf['abbrev'][0], 'CA')
        #self.assertEqual(___, ___)
    

if __name__ == '__main__':
    unittest.main()
