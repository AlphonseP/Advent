import os
import string

if __name__ == '__main__':
    file = open(r"C:\Users\virgi\Desktop\lines.txt", "r")
    print(type(file))
    sum = 0
    for line in file:
        first_dig = '0'
        second_dig = '0'
        for char in line:
            if char.isdigit():
                if first_dig == '0':
                    first_dig = char
                    second_dig = char
                else:
                    second_dig = char
        print(first_dig+second_dig)
        sum = sum + int(first_dig+second_dig)
    print (sum)
    file.close()
