"""
Created on Sun May 26 22:52:46 2023

@author: Ayush Chourasia
"""
print('Please enter a integer number set of 5 terms to segregate the positive numbers.')
def print_positive_numbers_in_range(numbers, start, end):
    positive_numbers = []
    
    for num in numbers:
        if num==0:
            print("I sensed a neutral number i.e. 0 aka shunya")
            
        if start < num <= end:
            positive_numbers.append(num)
    print("Positive numbers in the data filled in are:")
    
    if positive_numbers:
        for num in positive_numbers:
            print(num)
    else:
        print("No positive numbers found within the range.")


numbers = []
for i in range(5):
    number = int(input("Enter number {}: ".format(i+1)))
    numbers.append(number)


start = 0
end = 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
print_positive_numbers_in_range(numbers, start, end)

print('Task Complted... :)')
"PS: I wanted to make the end be infinite but could'nt, tried infinite loops using boolean too..."