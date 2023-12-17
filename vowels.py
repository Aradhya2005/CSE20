# assignment: quiz
# author: Aradhya Kapoor
# date: 11/12/23
# file: Implement that emulates a simple SI unit conversion calculator that can convert Fahrenheit into Celsius, miles to kilometers (km), and pounds into kilograms (kg).
# input: strings and numbers (integers)
# output:interactive messages strings
def count_vowels(word, vowels):
    
    vowels = 0

    for char in word:
        if char in ('a', 'A', 'e', 'E', 'I', 'i', 'o', 'O', 'u', 'U'):
            vowels += 1
    return vowels
       
        
        



# main
if __name__ == '__main__':
    vowels = 'AEIOUaeiou'
    word = input("Enter a word: ") 
    num_vowels = count_vowels(word, vowels)
    print(f"{word} {len(word)} letters, {num_vowels} vowels")
