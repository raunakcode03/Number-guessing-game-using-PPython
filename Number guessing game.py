#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
name=input("Hello Enter your name to start a game:- ")
print(name,"Game is started and you have only 5 chances and you have to guess number betweeen 1 and 20")
number=random.randint(1,20)
number_of_guesses=0
while number_of_guesses<5:
    guess=int(input("Enter a number: "))
    number_of_guesses+=1
    if(guess > number):
        print(name,"You are too high")
    elif(guess < number):
        print(name,",You are too low")
    elif(guess==number):
        break
if guess==number:
    print("You guessed the number in",number_of_guesses,"tries")
else:
    print("Your 5 chances are over and the numebr was",number)

