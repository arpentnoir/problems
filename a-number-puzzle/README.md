# Problem

## A Number Puzzle

### July 21, 2015

In last week’s exercise we had a word puzzle, so today’s exercise will be a number puzzle:

Find a 10-digit number, with all digits unique, such that the first n digits of the number are divisible by n. For instance, in the 3-digit number 345, the 1-digit prefix, 3, is divisible by 1, the 2-digit prefix, 34, is divisible by 2, and the 3-digit prefix, 345, is divisible by 3.

Your task is to write a program that finds a 10-digit number as defined above.

Original problem can be found here:
https://programmingpraxis.com/2015/07/21/a-number-puzzle/

# Solution 

* construct a list of possible first digits - 1 to 9
* write a function that takes a list of integers and returns another list, which is each member in the original list, with each of the digits from 0 to 9 
appended, provided that result is divisible by the length of the resulting number. 
* keep doing this until each list item is 10 digits long. 

