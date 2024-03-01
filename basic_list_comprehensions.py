
def main_fifteen(matrix):
    return [i[::-1] for i in matrix[::-1]]
def main_fourteen(matrix):
    return [[i[j] for i in matrix] for j in range(len(matrix[0]))]
def main_thirteen(numbers,fruits):
    return [(numbers, fruit) for name, fruit in zip(numbers, fruits)]

def calcSum(number):
    dsum = 0
    for letter in str(number):
        dsum += int(letter)
    return dsum
def main_twelve(numbers):
    return[calcSum(i) for i in numbers if i & 1]

def main_eleven (fruits):
    # _ is equals to submited
    # “Enumerate” means to mention or name things one by one in a list or series
    # The list just returns the value in each index
    return{fruit: [idx for _ in range(5)] for idx,fruit in enumerate(fruits)}

def is_consonant(letter):
    vowels = 'aeiou'
    #The isalpha() method returns True if all the characters are alphabet letters (a-z).
    #The lower() method takes no arguments and returns the lowercased strings from the given string by converting each uppercase character to lowercase.

    # t.isalpha()                      True
    # t.lower() not in vowels          True

    return letter.isalpha() and letter.lower() not in vowels
def main_ten (sentence):
    return[x for x in sentence if is_consonant(x)]
def main_nine(sentence):
    return [ x if x in 'aeiou' else 'aeiou' for x in sentence]
def main_eight(sentence):
    return [ x for x in sentence if x in 'aeiou']
def main_seven(numbers):
    return [ x*x if x*x <= 25 else x for x in numbers]
def main_six(fruits):
    return [ x=='apple' or x=='banana' for x in fruits]
def main_five(fruits):
    return ['hello' for x in fruits]
def main_four(fruits):
    return [x if x != "banana" else "orange" for x in fruits]

def main_three(numbers):
    return [x for x in numbers if x < 5]

def main_two(fruits):
    return [x for x in fruits if x != "apple"]

def main_one(fruits):
    return [x for x in fruits if "a" in x]

def main_zero(fruits):
    return [x for x in fruits]

if __name__ == "__main__":

    sentence = 'the rocket came back from mars'
    fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
    numbers1 = range(10)
    numbers2 = [367, 111, 562, 945, 6726, 873]
    matrix = [[10, 20, 30],[40, 50, 60],[70, 80, 90]]

    list_zero = main_zero(fruits)
    print(fr'Exercise zero: return a list with all the fruits in fruits. The result is : {list_zero}')
    list_one = main_one(fruits)
    print(fr'Exercise one: return a list with all the fruits with the letter a. The result is : {list_one}')
    list_two = main_two(fruits)
    print(fr'Exercise two: return a list with all the fruits excluding apple. The result is : {list_two}')
    list_three = main_three(numbers1)
    print(fr'Exercise three: return a list with all the number lower than 5. The result is : {list_three}')
    list_four = main_four(fruits)
    print(fr'Exercise four: return a list with all the fruits replacing banana for orange. The result is : {list_four}')
    list_five = main_five(fruits)
    print(fr'Exercise five: return a list with hello instead of the fruit names. The result is : {list_five}')
    list_six = main_six(fruits)
    print(fr'Exercise six: return a list return if the fruit is a apple or a banana. The result is : {list_six}')
    list_seven = main_seven(numbers1)
    print(fr'Exercise seven: return the square number if its lower than 25 otherwise return the number. The result is : {list_seven}')
    list_eight = main_eight(sentence)
    print(fr'Exercise eight: return a list with only the vowels. The result is : {list_eight}')
    list_nine = main_nine(sentence)
    print(fr'Exercise nine:  return a list with only the vowels and replace the consoants with aeiou. The result is : {list_nine}')
    list_ten = main_ten(sentence)
    print(fr'Exercise ten: return the consoants. The result is : {list_ten}')
    list_eleven = main_eleven(fruits)
    print(fr'Exercise eleven: return a list with dictionaries. The key are the fruits and The values is and array of 5 values with the idx. result is : {list_eleven}')
    list_twelve = main_twelve(numbers2)
    print(fr'Exercise twelve: return a list with the sum of all digits. The result is : {list_twelve}')
    list_thirteen = main_thirteen(numbers2,fruits)
    print(fr'Exercise thirteen: return a list with tupple of the numbers and fruits with same idx. The result is : {list_thirteen}')
    list_fourteen = main_fourteen(matrix)
    print(fr'Exercise fourteen: return a transposed matrix. The result is : {list_fourteen}')
    list_fitheen = main_fifteen(matrix)
    print(fr'Exercise fifteen: return a matrix but the elements are in inverted order. The result is : {list_fitheen}')