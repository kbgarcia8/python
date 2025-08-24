import re
"""
##WARMUP QUESTIONS
#LESSER OF TWO EVENS

def lesser_of_two_evens(a,b):
    number_match_a = re.search(r'[0-9]', str(a))
    number_match_b = re.search(r'[0-9]', str(b))

    if number_match_a and number_match_b:
        num_a = int(a)
        num_b = int(b)
        
        if num_a % 2 == 0 and num_b % 2 == 0:
            return min(num_a,num_b)
        else:
            return  max(num_a,num_b)
    else:
        return "a and b must be a number"

print(lesser_of_two_evens(2,4))

#ANIMAL CRACKERS
def animal_crackers(text):
    words = text.split(' ')

    if len(words) > 2:
        return "This function only accepts two-word string"

    word_1 = words[0]
    word_2 = words[1]

    if word_1[0] == word_2[0]:
        return True
    else:
        return False

print(animal_crackers('Crazy Kangaroo'))

#MAKES TWENTY
def makes_twenty(n1,n2):
    number_match_n1 = re.search(r'[0-9]', str(n1))
    number_match_n2 = re.search(r'[0-9]', str(n2))

    if number_match_n1 and number_match_n2:
        num1 = int(n1)
        num2 = int(n2)

        if num1 == 20 or num2 == 20:
            return True
        elif num1+num2 == 20:
            return True
        else:
            return False

print(makes_twenty(2,3))


##LEVEL 1 PROBLEMS
def old_macdonald(name):
    capitalized = []
    i = 0
    for letter in name:
        i=i+1
        if i == 1 or i == 4:
            capitalized.append(letter.capitalize())
        else:
            capitalized.append(letter)
    
    final_capitalized = ''.join(capitalized)

    return final_capitalized

print(old_macdonald('macdonald'))

#MASTER YODA
def master_yoda(text):
    words = text.split(' ')
    new_words = ' '.join(words[::-1])

    return new_words

print(master_yoda('We are ready'))

#ALMOST THERE
def almost_there(n):
    if type(n) != int:
        return "Please provide a number/integer only"
    
    if abs(n-100) <= 10 or abs(n-200) <= 10:
        return True
    else:
        return False

print(almost_there(211))

##LEVEL 2 PROBLEMS
#FIND 33
def has_33(nums):
    i = 0
    j = 1
    while i < len(nums) and j < len(nums):
        i=i+1
        j=j+1
        if(nums[i] == 3 and nums[j] ==3):
            return True
        else:
            return False
    
print(has_33([1, 3, 3]))


#PAPER DOLL
def paper_doll(text):
    repeat = range(3)
    repeated_letters = []
    for letter in text:
        for x in repeat:
            repeated_letters.append(letter)
    
    final_word = ''.join(repeated_letters)

    return final_word

print(paper_doll('Mississippi'))

#BLACKJACK
def blackjack(a,b,c):
    if (not all(isinstance(x, int) for x in [a, b, c]) or not all(1 <= x <= 11 for x in [a, b, c])):
        return "Please supply an integer only from 1 to 11"
    
    total = a+b+c

    if total <= 21:
        return total
    elif total > 21 and (a == 11 or b == 11 or c == 11):
        new_total = total-10
        if new_total <= 21:
            return new_total
        else:
            return 'BUST'
    else:
        return 'BUST'
        
print(blackjack(9,9,11))

#SUMMER OF 69
def summer_69(arr):
    total = 0
    index_6 = None
    index_9 = None
    if 6 in arr:
        index_6 = arr.index(6)
    
    if 9 in arr:
        index_9 = arr.index(9)

    if len(arr) == 0:
        return 0

    if index_9 != None and index_6 != None:
        for x in range(len(arr)):
            if x >= index_6 and x <= index_9:
                continue
            else:
                total=total+arr[x]
    elif index_9 == None and index_6 == None:
        for x in range(len(arr)):
            total=total+arr[x]
    
    return total

print(summer_69([4, 5, 6, 7, 8, 9]))


def spy_game(nums):
    indexes_0 = [idx for idx, val in enumerate(nums) if val == 0]
    index_7 = nums.index(7)

    if (indexes_0[0] > index_7 and indexes_0[1] > index_7)or (indexes_0[0] < index_7 and indexes_0[1] > index_7) or (indexes_0[0] > index_7 and indexes_0[1] < index_7):
        return False
    elif (indexes_0[0] < indexes_0[1]) and (indexes_0[1] < index_7):
        return True
    
print(spy_game([1,7,2,0,4,5,0]))

#COUNT PRIMES
def count_primes(num):
    prime_nums = []
    if type(num) != int:
        return "Please provide an integer only"
    
    for x in range(num+1):
        if x in [0,1]:
            continue
        elif x in [2,3]:
            prime_nums.append(x)
        elif x % 2 == 0 and x > 3:
            continue
        elif x % 2 != 0 and x > 3:
            i = 3
            is_prime = True
            while i <= int(x ** 0.5):
                if x % i == 0:
                    is_prime = False
                    break

                i+=2 #since even numbers as divisors are covered in 2nd elif

            if is_prime == True:
                prime_nums.append(x)

    return len(prime_nums)


print(count_primes(100))
"""
def print_big(letter):
    pattern = {
        "a": ["  *  ", " * * ", "*****", "*    *", "*    *"],
        "b": ["*****", "*    *", "*****", "*    *", "*****"],
        "c": ["*****", "*    ", "*    ", "*    ", "*****"],
        "d": ["*****", "*   *", "*   *", "*   *", "*****"],
        "e": ["*****", "*    ", "*****", "*    ", "*****"]
    }

    for element in pattern[letter]:
        print(element)

print_big('e')