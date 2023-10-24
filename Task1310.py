1#1

def unusual_five():
    return len("five!")

#2

def double_char(s):
    return ''.join(c * 2 for c in s)

#3

def is_anagram(test, original):
    return sorted(original.lower()) == sorted(test.lower()) 

#4

def double_integer(i):
    return i * 2

#5

def paperwork(n, m):
    if n < 0 or m < 0:
        return 0
    else: 
        return n * m

#6

def solution(str):
  return str[::-1]

#7

def string_to_array(s):
    return s.split(' ')

#8

def find_short(s):
    x = s.split(' ')
    l = len(x[0])
    for i in x:
        if len(i) < l:
            l = len(i)
    return l
            

#9

def sum_mix(arr):
    return sum(int(i) for i in arr)

#10

def count_sheeps(sheep):
    x = 0
    for i in sheep:
        if i == True:
            x = x + 1
    return x

