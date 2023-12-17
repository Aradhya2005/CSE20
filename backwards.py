
def reverse_word(word):
    return(word[::-1])

if __name__ == '__main__':
  
   backward_word = reverse_word('hello')
   assert backward_word == 'olleh'
   
   backward_word = reverse_word('madam')
   assert backward_word == 'madam'
