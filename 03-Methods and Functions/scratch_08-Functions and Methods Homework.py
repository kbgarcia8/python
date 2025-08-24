"""
#VOLUME OF SPHERE
import math
def vol(rad):
    vol = (4/3)*(math.pi)*(rad**3)

    return vol

print(vol(2))

#NUM IN GIVEN RANGE
def ran_check(num,low,high):
    for x in [num,low,high]:
        if type(x) != int:
            return "Please provide integers only"
    
    if num >= low and num <= high:
        return f"{num} is in the range between {low} and {high}"
    else:
         return f"{num} is not in the range between {low} and {high}"
    
print(ran_check(2,5,7))

#NUM IN GIVEN RANGE BOOLEAN RETURN
def ran_bool(num,low,high):
    for x in [num,low,high]:
        if type(x) != int:
            return "Please provide integers only"
    
    if num >= low and num <= high:
        return True
    else:
         return False

print(ran_bool(3,1,10))

#UPPER-LOWER COUNTER
import re
def up_low(s):
    low_case = 0
    up_case = 0
    characters = re.findall(r"\w+", s)
    letters = ''.join(characters)

    for letter in letters:
        if letter.isupper():
            up_case +=1
        else:
            low_case +=1

    print(f"No. of Upper case characters : {up_case}")
    print(f"No. of Lower case characters : {low_case}")

s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
up_low(s)

#UNIQUE LIST
def unique_list(lst):
    unique = []
    if type(lst) != list:
        return "Please provide a list of numbers only"
    
    for x in lst:
        if x in unique:
            pass
        else:
            unique.append(x)

    return unique


print(unique_list([1,1,1,1,2,2,3,3,3,3,4,5]))

#MULTIPLY ALL NUMBERS
def multiply(numbers):
    product = None
    if type(numbers) != list:
        return "Please provide a list of numbers only"
    
    for num in numbers:
        if product == None:
            product = num
        else:
            product *= num

    return product

print(multiply([1,2,3,-4]))

#PALINDROME
def palindrome(s):
    if type(s) != str:
        return "Please provide string only"
    
    characters = list(s)
    reversed_list = characters[::-1]
    reversed_word = ''.join(reversed_list)
    
    if s == reversed_word:
        return True
    else:
        return False

print(palindrome('helleh'))
"""
#PANGRAM
import string

def ispangram(str1, alphabet=string.ascii_lowercase):
    characters_set = set(list((str1.replace(' ', '')).lower()))
    alphabet_set = set(list(alphabet))
    
    if characters_set == alphabet_set:
        return True
    else:
        return False

print(ispangram("The quick brown fox jumps over the lazy dog"))