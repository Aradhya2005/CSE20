def is_palindrome(word):
    backword_word = (word[::-1])

    
    if backword_word  == word:
         return True
    else:
        return False

if __name__ == '__main__':

    assert is_palindrome('madam') == True
    assert is_palindrome('hello') == False

    
