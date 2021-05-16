#For the following questions write tests in unittest and pytest.
#In a pdf, document the outputs from both the testing frameworks.
#Make your code available on Github.
#Ask the user for a string and determine whether it is a palindrome or not.
#Write tests for the above specification using unittest and pytest.
#Document the outputs in a pdf - (screenshots of the output from unittest and pytest)
class Palindrome:
    def determine_palindrome(palin_):
        lst_pal = []
        for txt in palin_.lower():
            if txt in "abcdefghijklmnopqrstuvwxyz":
                lst_pal.append(txt)

        if list(lst_pal) == list(reversed(lst_pal)):
            return True
        else:
            return False

    #palin_ = input('Input word or sentence: ')
    #if determine_palindrome(palin_):
    #    print("\'"+palin_+"\' is a palindrome")
    #else:
    #    print("\'"+palin_+"\' is not a palindrome")