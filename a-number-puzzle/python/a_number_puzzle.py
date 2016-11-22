'''
22 November 2016

Find a 10-digit number, with all digits unique, such that the first n digits of the number are divisible by n. For instance, 
in the 3-digit number 345, the 1-digit prefix, 3, is divisible by 1, the 2-digit prefix, 34, is divisible by 2, and the 3-digit prefix, 
345, is divisible by 3.

'''

def appendDigit(list):
    new_list = []
    for prefix in list:
        for i in range(0, 10):
            string = str(prefix) + str(i)
            number = int(string)
            length = len(string)
            if number % length == 0:
                new_list.append(number)

    return new_list

list = range(1, 10)
for n in range(1, 10):
    list = appendDigit(list)

print list

'''
or like this
print(appendDigit(appendDigit(appendDigit(appendDigit(appendDigit(appendDigit(appendDigit(appendDigit(appendDigit([1, 2, 3, 4, 5, 6, 7, 8, 9]))))))))))
'''
