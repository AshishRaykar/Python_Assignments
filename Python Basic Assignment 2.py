#!/usr/bin/env python
# coding: utf-8

# #### 1.What are the two values of the Boolean data type? How do you write them?
# 
# --> The two values of boolean data type is `True` and `False`.

# In[1]:


print(10==10)
print(10!=10)


# #### 2. What are the three different types of Boolean operators?
# 
# The three basic boolean operators are: `AND`, `OR`, and `NOT`.

# #### 3. Make a list of each Boolean operator's truth tables (i.e. every possible combination of Boolean values for the operator and what it evaluate ).

# In[3]:


#NOT
print(not True)
print(not False)


# In[8]:


#AND
print(True & True)
print(False & True)
print(True & False)
print(False & False)


# In[10]:


#OR
print(True or True)
print(False or True)
print(True or False)
print(False or False)


# #### 4. What are the values of the following expressions?

# In[11]:


(5 & 4) and (3 == 5)


# In[13]:


not (5 & 4)


# In[14]:


(5 & 4) or (3 == 5)


# In[16]:


not ((5 & 4) or (3 == 5))


# In[18]:


(True and True) and (True == False)


# In[19]:


(not False) or (not True)


# #### 5. What are the six comparison operators?
# 
# `==` Equal
# 
# `!=` Not Equal
# 
# `>` Greater Than
# 
# `<` Less Than
# 
# `>=` Greater Than Equal To
# 
# `<=` Less Than Equal To

# #### 6. How do you tell the difference between the equal to and assignment operators?Describe a condition and when you would use one.
# 
# --> The `==` equal to is an comparison operator used to compare two values and assignment operators are used to assign values to varibles. 

# In[ ]:


#assignment operator
a=10 #I assigned variable a value 10 using assignment operator
b=10


#comparison operator
a==b #Here we compared values a and b


# #### 7. Identify the three blocks in this code:

# In[ ]:


spam = 0
if spam == 10: # block 1
print('eggs')
      
      
if spam > 5:
print('bacon') # block 2

else:          # block 3
print('ham')
print('spam')
print('spam')


# #### 8. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.

# In[10]:


spam=int(input("Enter Any no."))

if spam == 1:
    print("Hello")
elif spam == 2:
    print("Howdy")
else:
    print("Greetings")
    


# #### 9.If your programme is stuck in an endless loop, what keys you’ll press?
# 
# --> To break the endless loop I will press `ctrl + c`.

# #### 10. How can you tell the difference between break and continue?
# 
# --> The `break` statement terminates the loop and the `continue` statement is used to skip the code inside the loop

# In[17]:


for x in 'python':
    if x == 't':
        break
    print(x)   


# In[19]:


for x in 'python':
    if x == 'n':
        continue
    print(x)  


# #### 11. In a for loop, what is the difference between range(10), range(0, 10), and range(0, 10, 1)?
# 
# --> Range is a function which returns sequence of numbers which takes 3 parameters `start` `stop` `step`
# 
# `range(10)` It will return 0 to 9 sequence were 10 is the stop parameter and by default the start parameter starts from 0 and step increments by 1.
# 
# `range(0,10)` We have start and stop parameter so it will return sequence from 0 to  9.
# 
# `range(0,10,1)` We have all the parameters mention with a step which will also return sequence from 0 to 9.

# #### 12. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using a while loop.

# In[21]:


for i in range(1,11):
    print(i)
    


# In[25]:


i=1
while i < 11:
    print(i)
    i+=1


# #### 13. If you had a function named bacon() inside a module named spam, how would you call it after importing spam?
# 
# `spam.bacon()`
