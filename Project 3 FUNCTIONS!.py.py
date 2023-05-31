"""
Created on Mon May 24 15:30:21 2023
mycap project 3 FUNCTIONS!
@author: Ayush Chourasia
"""
def most_frequent(string):
    freq_dict = {}
    for char in string:
        if char in freq_dict:
            freq_dict[char] += 1
        else:
            freq_dict[char] = 1

    sorted_freq = sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)
    
    for item in sorted_freq:
        print(item[0], ':', item[1])
input_string = input("Please enter a string: ")
most_frequent(input_string)
