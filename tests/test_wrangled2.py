import pytest

# Importing the necessary packages
from newpandaspackage.new_function import WrangledFrame


def test_add_state_names():
    wf = WrangledFrame({'abbrev': ['CA', 'CO', 'CT', 'DC', 'TX']})
    #self.assertEqual(len(list(wf.columns)), 1)
    assert list(wf.columns), ['abbrev']

    wf.add_state_names()
    # ensure there is a 'name' column
    #self.assertEqual(len(list(wf.columns)), 2)
    assert list(wf.columns), ['abbrev', 'name']

    # ensure the value of the WF are specific classes or values (str, 'Cali')
    #self.assertEqual(wf['name'][0], 'Cali')
    #self.assertEqual(wf['abbrev'][0], 'CA')
    assert wf['name'][0] == 'Cali'
    assert wf['abbrev'][0] == 'CA'


