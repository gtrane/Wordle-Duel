#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from datetime import date


# In[ ]:


# code used to initialize a dataframe.

# dict = {'Date': [],'Player': [],'Wordle':[],'Guesses':[],'Wins':[],'Losses':[], 'Ties': []} 
# df = pd.DataFrame(dict)
# df.to_csv("Wordle/wordle.csv", sep=",", index=False)


# In[2]:


df = pd.read_csv("wordle.csv")
df


# In[2]:


wordle = input("Today's wordle: ").upper()
if len(wordle) != 5:
    wordle = input("The word must be 5 letters! Today's wordle: ").upper()
    
#grace
try:
    grace_guess = int(input("How many guesses did it take for Grace? "))
except ValueError:
    print('You must enter a number between 1 and 6!')   
    grace_guess = int(input("Let's try this again ;) How many guesses did it take for Grace? "))

#jake    
try:
    jacob_guess = int(input("How many guesses did it take for Jacob? "))
except ValueError:
    print('You must enter a number between 1 and 6!')   
    jacob_guess = int(input("Let's try this again ;) How many guesses did it take for Jacob? "))


# In[3]:


today = date.today()
jwins = 0
gwins = 0
jloss = 0
gloss = 0
jtie = 0
gtie = 0
  
if jacob_guess < grace_guess:
    jwins = 1
    gloss = 1
elif jacob_guess > grace_guess:
    gwins = 1
    jloss = 1
elif jacob_guess == grace_guess:
    jtie = 1
    gtie = 1

df.loc[len(df.index)] = [today,'Jacob',wordle, jacob_guess, jwins, jloss, jtie] 
df.loc[len(df.index)] = [today,'Grace',wordle, grace_guess, gwins, gloss, gtie]


df_wins = df[['Player','Wins']].groupby('Player').sum()

grace_wins = df_wins.iloc[0, 0] 
jacob_wins = df_wins.iloc[1, 0] 

grace_rate = (grace_wins / (len(df)/2))*100 #percentage of wins
jacob_rate = (jacob_wins / (len(df)/2))*100

#ties
ties = df[df.Player == 'Grace'].Ties.sum()   

print(f"Currently, Grace's win rate is {round(grace_rate,2)}% and Jacob's is {round(jacob_rate,2)}%. We've tied {ties} times ({round((ties/(len(df)/2))*100,2)}% of the time)! Nerds.")
df
    


# In[4]:


df.to_csv("wordle.csv", sep=",", index=False)

