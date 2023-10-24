#1

def hex_to_dec(s):
    return int(s, 16)

#2

def greet():
    return "hello world!"

#3

def positive_sum(arr):
    return sum(x for x in arr if x > 0)

#4

def make_negative( number ):
    return -abs(number)

#5

def findSmallestInt(arr):
    return min(arr)

#6

def get_age(age):
    return int(age[0])

#7

def find_needle(haystack):
    for i, x in enumerate(haystack):
        if x == 'needle': 
            return 'found the needle at position %d' % i

#8

def remove_char(s):
    return s[1 : -1]

#9

def digitize(n):
    return [int(x) for x in str(n)[::-1]]

#10

def sum_array(arr):
    if arr == None or len(arr) < 3:
        return 0
    return sum(arr) - max(arr) - min(arr)
