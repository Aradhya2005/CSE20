# assignment: trianlge.py
# author: Aradhya Kapoor
# date: 10/27/23
# file: asks the user to input an integer that corresponds to a triangle height and then generates an ASCII art triangle with the width equals to its height. 
# input: interactive messge
# output: ASCII art 
n = int(input("enter a number \n"))
for k in range(n):
        print(' ' * k + '*' * (n-k))
