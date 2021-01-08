# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 10:29:50 2020

@author: roynu
"""
#1
countries = ["USA", "Canada", "Mexico"]
countriesCapitials = ["Washingtion", "Ottawa", "Mexico City"]
# for i in range(len(countries)):
#     print(f"The population of {countries[i]} is 38 million people and its capital is {countriesCapitials[i]}.")

#2
for i in range(len(countries)):
    print(f"The population of {countries[i]} is 38 million people and its capital is {countriesCapitials[i]}.")
    player_input = input("Is there anything you would like to add?")
    if player_input == "quit":
         print(f"The population of {countries[i]} is 38 million people and its capital is {countriesCapitials[i]}.")
         
        
# #3
player_input2 = ""
for i in range(len(countries)):
    player_input2 = input(f"What is the poulation for this countries capitial {countriesCapitials[i]}")
    for i in range(1):
        if player_input2 == float:
            player_input2 = player_input2
            print("thanks")
    
    
#4
countriespopulation = ["6.8mill","6.1mil","5.8mil"]

for i in range(len(countries)):
    print(f"{countries[i]} has a population {countriespopulation} and it's capitial is {countriesCapitials[i]}")

#5
#I am not sure
    

#6
player_input3 = ""
for i in range(1):
    player_input3 = input("Is there anything you would like to know?")
    if player_input3 == "yes":
        print(countries)
        print(countriespopulation)
        print(countriesCapitials)
    else:
        print("ok")        
       
    
