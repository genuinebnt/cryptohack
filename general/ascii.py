#!/usr/bin/python3

### PROBLEM DESCRIPTION
# ASCII is a 7-bit encoding standard which allows the representation of text using the integers 0-127.
# Using the below integer array, convert the numbers to their corresponding ASCII characters to obtain a flag.
# [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]
###

def ascii():
    arr = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]
    flag = "".join([chr(x) for x in arr])
    print(flag)
    

if __name__ == '__main__':
    ascii()