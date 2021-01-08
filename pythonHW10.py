# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 19:54:07 2020

@author: roynu
"""
#1
# it randomly imports a number from 1 to 100
import random
number = random.randint(1, 100)
print(number)

#2
# user_input = int(input("Pick a number from 1-100"))
# if user_input == number:
#     print("correct!!!")
# else:
#     if user_input > number:
#         print("Too high!!!!")
#     else:
#         print("to low")

#3
# user_input = int(input("Pick a number from 1-100"))
# for i in range(100):
#     if user_input == number:
#         print("correct!!!")
#         if user_input != int: 
#             print("input has to be string")
#         else:
#             if user_input > number:
#                 print("Too high!!!!")
#             else:
#                 print("to low")
        
#4
counter = 0
user_input = int(input("Pick a number from 1-100"))
for i in range(100):

    if user_input == number:
        print("correct!!!")
        counter = counter + 1
        if user_input != int: 
            print("input has to be string")
            counter = counter + 1
        else:
            if user_input > number:
                print("Too high!!!!")
                counter = counter + 1
            else:
                print("to low")
                counter = counter + 1
                
#5
user_name = input("What is your name")
MyList = [user_name, counter, counter]
print(MyList)
