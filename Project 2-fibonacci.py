"""
Created on Thu May 19 22:04:34 2023
Author: Ayush Chourasia
Project 2 (MyCaptain)
"""
print("Greetings,")
num = int(input("Please enter the number of Fibonacci series you want :"))
num1, num2 = 0, 1
sum = 0
if num <= 0:
    print('Oops! Please enter a number greater than 0, & also avoid decimal numbers please ')  
    
else: 
    for i in range(0, num):
        print(sum, end=" , ")
        num1 = num2
        num2 = sum
        sum = num1 + num2
        
    print('Task completed.. :)')


















