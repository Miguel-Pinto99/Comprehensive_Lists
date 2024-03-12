

def find_next_number(number,idx):

    now_number =  str(number)[idx]
    sum_number = 0
    number_len = len(str(number))

    for x in str(number)[idx+1:number_len]:
        if int(x) % 2 == 0:
            sum_number = x
            break

    return int(sum_number)

def main_nine(number):

    return int(''.join([str(int(digit)+find_next_number(number,idx)) for idx, digit in enumerate(str((number)),start=0) if int(digit) % 2 == 0]))

def main_eight(number):

    return int(''.join([str(int(digit)+int(digit)) for idx,digit in enumerate(str((number))) if int(digit) % 2 == 0]))

def main_seven(sentence):
    return [True if 'a' in word.lower() else False for word in sentence.split()]
def main_six(fruits):
    return [True if fruit in ['apple','orange'] else False for fruit in fruits]

def main_five(fruits):
    return [True if 'p'in fruit or 'l'in fruit or 'k'in fruit or 'r' in fruit else False for fruit in fruits]
def main_four(fruits):
    return [True if 'ap' in fruit else False for fruit in fruits]
def main_three(fruits):
    #  if 'a' = if it is a string!
    #  'a' not in x = doesnt not contain a 'a'
    return [x for x in fruits if 'a' and 'a' not in x]
def main_two(fruits):
    return [x for x in fruits if ('a' and 'e') not in x]
def main_one(fruits):
    return [x for x in fruits if 'a' not in x and 'e' not in x]
def main_zero(numbers2):
    #str(x)[-1] = last digit
    return [x*x if int(str(x)[-1]) in [4,8] else 0 for x in numbers2 if (x % 2) == 0]

if __name__ == "__main__":

    sentence = 'the rocket came back from mars'
    fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

    numbers1 = range(10)
    numbers2 = [1,2,3,4,5,6,7,8,9,10,20,24,30,66]
    number3 = 12341929457172840919283417162749501029384

    matrix = [[10, 20, 30],[40, 50, 60],[70, 80, 90]]

    list_zero = main_zero(numbers2)
    print(fr'Exercise zero: return a list with all pair numbers. In adition only return the ones that have a 4 or 8. If not replace with zero The result is : {list_zero}')
    list_one = main_one(fruits)
    print(fr'Exercise one: return a list with the fruits without a and e. If not replace with zero The result is : {list_one}')
    list_two = main_two(fruits)
    print(fr'Exercise two: return a list with the fruits without a and e at the same time. If not replace with zero The result is : {list_two}')
    list_three = main_three(fruits)
    print(fr'Exercise three: test')
    list_four = main_four(fruits)
    print(fr'Exercise four: return a list with True or False if the fruit has "ap". The result is : {list_four}')
    list_five = main_five(fruits)
    print(fr'Exercise five: return a list with True or False if the fruit has "p","l","k" or "r". The result is : {list_five}')
    list_six = main_six(fruits)
    print(fr'Exercise six: return a list with True or False if the fruit is an apple or an orange. The result is : {list_six}')
    list_seven = main_seven(sentence)
    print(fr'Exercise seven: return a list with True or False if the each word in the sentence has an lower "a". The result is : {list_seven}')
    list_eight = main_eight(number3)
    print(fr'Exercise eight: return a number with all the pair digits multiplied by two. The result is : {list_eight}')
    list_nine = main_nine(number3)
    print(fr'Exercise nine: return a number with all pair digits summed with the next pair digit. The result is : {list_nine}')