import re 
import unittest 

def normalize_and_count(s, token): 
    ns = s.lower() 
    ns = re.sub(r'[^\w\s]', '', ns) 
    tokens = ns.split() 
    
    return tokens.count(token.lower())

class TestStringMethods(unittest.TestCase):
    # this test makes sure it works as it is supposed to
    def test_one(self):
        self.assertEqual(normalize_and_count("The quick brown fox jumps over the lazy dog. The dog is very lazy.", "the"), 3)

    # meant to fail, which is why it's not equal instead of just equal
    def test_two(self):
        self.assertNotEqual(normalize_and_count("Twinkle twinkle little star.", "stare"), 1)

    def test_three(self):
        self.assertNotEqual(normalize_and_count("There once was a boy named Adam.", "one"), 1)

if __name__ == '__main__':
    unittest.main()