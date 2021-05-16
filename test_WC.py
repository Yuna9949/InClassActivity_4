#For the following questions write tests in unittest and pytest.
#In a pdf, document the outputs from both the testing frameworks.
#Make your code available on Github.
#Ask the user for a sentence and determine the number of words in that sentence.
#Example = "This is an activity", Output - 4.
#Write tests for the above specification using unittest and pytest.
#Document the outputs in a pdf - (screenshots of the output from unittest and pytest)
import unittest
from WordCount import WordCount

class test_pal(unittest.TestCase):
    def test_work(self):
        self.assertEqual(WordCount.counting('I am living in OSU'), 5)

#if __name__ == '__main__':
#    unittest.main()