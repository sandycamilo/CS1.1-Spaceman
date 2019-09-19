from spaceman import *
import unittest
 
 # TEST FUNCTIONS 
class spaceman_test(unittest.TestCase):

    def test_is_guess_in_word(self):
        assert is_guess_in_word("a", "sand") == True   # compares two arguments and checks if its true or false
        self.assertFalse(is_guess_in_word("f", "sand"))

    def test_get_guessed_word(self):
        assert get_guessed_word("sand", ["s", "a", "n", "d"]) == "sand"
        # self.assertFalse(get_guessed_word("sand", ["c", "k", "y"]))

    def test_is_word_guessed(self):
        # test_list = ["s", "a", "n", "d"]
        assert is_word_guessed("sand", "sand") is True
        self.assertFalse(is_word_guessed("fox", "sand"))
        
   
