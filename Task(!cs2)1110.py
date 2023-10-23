#1

def solution(nums):
    return sorted(nums) if nums else []

#2

def repeat_str(repeat, string):
    return string * repeat

repeat_str(3, 'loh')

#3

def make_upper_case(strng):
    return strng.upper()

#4

def number_to_string(num):
   return str(num)

#5

def get_grade(s1, s2, s3):
    
    sum = (s1 + s2 + s3) / 3
    
    if sum >= 90 :
        return "A"
    elif sum >= 80:
        return "B"
    elif sum >= 70:
        return "C"
    elif sum > 60:
        return "D"
    else:
        return "F"

#6

def small_enough(array, limit):
    return max(array)<=limit

#7

def sum_array(a):
    if a != 0:
         return sum(x for x in a)
    else:
        return 0

#8

def better_than_average(class_points, your_points):
  if sum(class_points)/len(class_points) < your_points:
    return true
  else:
    return false

#9

def area_or_perimeter(l , w):
    if l == w:
        return l * w
    else:
        return (l * w) * 2

#10

def square(n):
    return n ** 2
