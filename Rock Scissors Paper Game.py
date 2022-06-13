#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

print("Rules of the game include: \n Rock vs Paper--Paper Wins!!\n Rock Vs Scissors--Rock Wins!!\n Paper Vs Scissors--Scissors Wins!!")
      
#UserLine

while True:      
    print('Enter Rock or Paper or Scissors in the choice box');
    value_list=["ROCK", "PAPER", "SCISSORS"];
    User_value= input('Choice:').upper()
    while User_value not in value_list:
        print('enter a valid choice')
        break 
    print('now its computer turn!!!')     
#ComputerLine
    Comp_value = random.choice(value_list);
    print(Comp_value);
    if User_value == Comp_value:
        print("Draw=>", end="");
        result = Draw
    if (User_value == "ROCK" and Comp_value == "PAPER") or (User_value == "PAPER" and Comp_value == "ROCK"):
        print("PAPER WINS =>", end="");
        result = "PAPER"
    if (User_value == "ROCK" and Comp_value == "SCISSORS") or (User_value == "SCISSORS" and Comp_value == "ROCK"):
        print("ROCK WINS=>", end="");
        result = "ROCK"
    if (User_value == "SCISSORS" and Comp_value == "PAPER") or (User_value == "PAPER" and Comp_value == "SCISSORS"):
        print("SCISSORS WINS =>", end="");
        result = "SCISSORS"
#Conclusion
    ans = input("Do yo want to play again(Y/N)?")
    if ans == N:
        break;
    print('Thanks for playing!!')
    
        
    
    


# In[20]:


print(value)

