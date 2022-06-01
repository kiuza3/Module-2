#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#string in lower case 
name = 'KIUZA'
print(name.lower())

#string in uppercase 
last_name = 'Neves'
print(last_name.upper())

#string for a variable that is all in lowercase 
fav_fruit = 'banana'
print(fav_fruit.capitalize())

#string to find a combination of letters 
fav_book = 'atomic habits'
#check the index for 'mic'
print(fav_book.rfind('mic'))

#check if all characters in the text are in upper case 
school = 'The city College of New York'
print(school.isupper())

#string with atleast 10 characters 
fav_ice_cream = 'cookies and creams'
print(fav_ice_cream.title())

#numbers of characters in a string 
course = 'data science'
print(len(course))

#removing the 'white space' form the begining of a string 
fav_car = 'Tesla'
print(fav_car.strip())

#replacing letters in string 
vacation = 'Hawaii'
print(vacation.replace('H', 'J'))

#checking for 'basket'
fav_sport = 'basketball'
print('basket' in fav_sport)


# In[16]:


#creating numerical variables

#sum of 3 variables
mom = 43
dad = 52
son = 13 
total = mom+dad+son
print(total)

#subtract two variable
cat = 17.5
dog = 12.6
print (float(cat - dog))

#multiply 5 variables (average ages of people in class)
avg1 = 21
avg2 = 19
avg3 = 17
avg4 = 18
avg5 = 20
print(avg1 * avg2 * avg3 * avg4 * avg5)

# taking the power of a variable with another variable 
print(int(pow(dog,son)))

#taking the square root of the largest variable
import math 
num = math.isqrt(25)
print(num)








# In[ ]:




