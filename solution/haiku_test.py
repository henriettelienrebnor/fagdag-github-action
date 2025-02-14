import unittest
from haiku_checker import count_syllables, is_haiku

class TestHaikuChecker(unittest.TestCase):

    def test_syllables(self):
        self.assertEqual(count_syllables("silence"), 2)
        self.assertEqual(count_syllables("beautiful"), 3)
        self.assertEqual(count_syllables("rhythm"), 1) 
        self.assertEqual(count_syllables("table"), 2)
        self.assertEqual(count_syllables("sky"), 1)
        self.assertEqual(count_syllables("hmm"), 1)  
        self.assertEqual(count_syllables("queue"), 1) 
        
    def test_is_haiku(self):
        haiku_valid = "An old silent pond - The frog jumps into the pond - Splash! Silence again."
        haiku_invalid = "An old silent pond - The frog jumps into the pond - Splash! Water everywhere."

        self.assertTrue(is_haiku(haiku_valid))   
        self.assertFalse(is_haiku(haiku_invalid)) 
        
if __name__ == '__main__':
    unittest.main()
