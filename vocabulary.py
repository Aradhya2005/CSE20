# assignment: programming quiz 4
# author: Aradhya Kapoor
# date: Nov/29/22
# file: vocabulary.py 
# input: User inputs statements and lines. 
# output: gives an dictionary with all the words.  

import re

def make_vocabulary(text):

    text = re.sub(r'[^\w\s]', '', text.lower())
    words = text.split()
    vocabulary = {}   
    for word in words:
        vocabulary[word] = vocabulary.get(word, 0) + 1
    
    return vocabulary

# main
if __name__ == '__main__':
    text = '''In secret we met -
    In silence I grieve,
    That thy heart could forget,
    Thy spirit deceive.
    If I should meet thee
    After long years,
    How should I greet thee? -
    With silence and tears'''
    
    vocabulary = make_vocabulary(text)
    print(f'Total words in the dictionary: {len(vocabulary)}')
    for key in sorted(vocabulary):
        print(f'{key} : {vocabulary[key]}')
