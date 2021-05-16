#For the following questions write tests in unittest and pytest.
#In a pdf, document the outputs from both the testing frameworks.
#Make your code available on Github.
#Ask the user for a string and determine whether it is a palindrome or not.
#Write tests for the above specification using unittest and pytest.
#Document the outputs in a pdf - (screenshots of the output from unittest and pytest)

from Palindrome import Palindrome

def test_work_pal_pt():
    assert Palindrome.determine_palindrome('Ned, I am a maiden.') == True