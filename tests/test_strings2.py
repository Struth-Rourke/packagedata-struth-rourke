import pytest

def test_upper(self):
    #self.assertEqual('foo'.upper(), 'FOO')
    assert ('foo'.upper() == 'FOO')
    # assert 'foo'.upper() == 'FOO' -- equivalent to above

def test_isupper(self):
    #self.assertTrue('FOO'.isupper())
    #self.assertFalse('Foo'.isupper())
    assert 'FOO'.isupper()
    assert 'FOO'.isupper() == False

def test_split(self):
    s = 'hello world'
    #self.assertEqual(s.split(), ['hello', 'world'])
    assert s.split() == ['hello', 'world']

    ## check that s.split fails when the separator is not a string
    #with self.assertRaises(TypeError):
    #    s.split(2)

    with pytest.raises(TypeError):
        s.split(2)



## Make your test fail first before you make them work so that 
## you know that the test is passing for the right reasons