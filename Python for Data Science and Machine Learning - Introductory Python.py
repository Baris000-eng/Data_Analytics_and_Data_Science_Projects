#!/usr/bin/env python
# coding: utf-8

# #Data types
# 
# #Integers
# 1

# In[2]:


#######Floats
1.0


# In[3]:


1+1


# In[4]:


2 * 3


# In[5]:


2 / 3.0


# In[6]:


2 ** 4 # 2 to the power of 4. '**' is the exponentiation operator.


# In[7]:


2 + 3 * 5 + 6 ##### Firstly, multiplication is evaluated. Then, the operations are evaluated from left to right.


# In[8]:


(2 + 6) * (33 - 21) #### = 8 * 12 = 96 ####


# In[11]:


##########Remainder operator = % ###############
4 % 2


# In[12]:


5%2


# In[13]:


8%3


# In[14]:


var = 11


# In[15]:


var


# In[16]:


x = 2
y = 3


# In[17]:


x * x + y * y ########we can call the variables in a seperate cell and do operations with them.


# In[18]:


12var = 13 ##########This will give error because the variable names cannot start with numeric


# In[19]:


x = 7


# In[20]:


x = x * x 


# In[21]:


x


# In[22]:


a = 5


# In[23]:


a = a + a


# In[24]:


a


# In[25]:


name_of_var = 18 ########proper syntax is to seperate with underscores.


# In[26]:


##############Python Strings

'single quotation mark'


# In[27]:


"double quotation mark"


# In[28]:


"I can't go outside today." ######Single quote inside double quote.


# In[29]:


x = 'hello'


# In[30]:


x


# In[31]:


y = 'Hello World'


# In[32]:


y


# In[33]:


print(x)
print(y)
print(x,y)


# In[34]:


number = 20
name = 'Mike'


# In[35]:


'My number is {} and my name is {}'.format(number, name) ######one way of formatting the string


# In[36]:


print('My number is {} and my name is {}'.format(number, name)) #######another way of formatting the string


# In[37]:


print('My number is {one} and my name is {two}'.format(one=number, two=name)) #######third way of formatting the string


# In[38]:


string = 'Hello World'


# In[39]:


string[0]


# In[40]:


string[1]


# In[41]:


string[10]


# In[46]:


print(string[0])
print(string[1])
print(string[2])
print(string[3])
print(string[4])
print(string[5])
print(string[6])
print(string[7])
print(string[8])
print(string[9])
print(string[10]) #same as print(string[-1])
print(string[-1])


# In[49]:


print(string[0], string[-11])
print(string[1], string[-10])
print(string[2], string[-9])
print(string[3], string[-8])
print(string[4], string[-7])
print(string[5], string[-6])
print(string[6], string[-5])
print(string[7], string[-4])
print(string[8], string[-3])
print(string[9], string[-2])
print(string[10], string[-1])


# In[53]:


alphabet_string = "abcdefghijklmnopqrstuvwxyz"

# Starting at index 0, grab everything beyond it within the alphabet_string.
print(alphabet_string[0:])


# Grab everything up to but not including index 5 (up to but including index 4) within the alphabet_string.
print(alphabet_string[:5])


# Grab everything starting at index 4 up to the index 9 not including the index 9
# (starting at index 4 and ending at index 8) within the alphabet_string.
print(alphabet_string[4:9])


# In[54]:


############################Python Lists###########################################


# In[55]:


lst1 = [1, 2, 3]
lst2 = ['a', 'b', 'c']
lst3 = [0, 1, 2]

print(lst1)
print(lst2)
print(lst3)
lst3.append(99)
lst3.append(17)
print(lst3)


# In[57]:


print(lst3[0:])  ### grab everything beyond the index 0 within the list called lst3 ###
print(lst3[1:4]) ### grab the list elements starting at index 1 and ending at index 3 (not including the index 4) ###


# In[61]:


print(lst3[0]) ### get the first element of the list called lst3 and print it
print(lst3[1]) ### get the second element of the list called lst3 and print it
print()
print(lst3) ##########previous version of the list called lst3
lst3[0] = 8888 #########update the first element of lst3 to 8888
print(lst3)  #########updated version of the list called lst3


# In[62]:


nested_list = [[1,2, [3,4,5], [6,7], [8,9,10,[11,12]], 13], 14]


# In[66]:


print(nested_list[0][2][0:])
print(nested_list[0][4][3][1])
print(nested_list[0][4][3])
print(nested_list[0][4])


# In[67]:


second_nested_list = ['hello', [1, 'targeted'], 3.14, [9, 17]]
print(second_nested_list[1][1]) #####grabs the second element in the second element of the outer list


# In[68]:


#############Python Dictionaries
d = {'key1': 'value1', 'key2': 345}
print(d['key1'])
print(d['key2'])
print(d['key1'], d['key2'])


# In[70]:


dictionary = {'k1': [7,8,9,10,11]}
print(dictionary['k1']) ## Accessing the value within the dictionary corresponding to the key 'k1'.
print(len(dictionary['k1'])) ###It will get the length of the value within the dictionary corresponding to the key 'k1'.


# In[73]:


print(dictionary['k1'][0])
print(dictionary['k1'][1])
print(dictionary['k1'][2])
print(dictionary['k1'][3])
print(dictionary['k1'][4])
print(dictionary['k1'][5]) #######This will throw an index error because it exceeds the valid index range for the list as the value.


# In[74]:


tuple_element = (1,2,3) #######defining a tuple


# In[75]:


print(tuple_element[0], tuple_element[1], tuple_element[2])


# In[76]:


tuple_element[1] = 'Hello World' ####It will throw error. Because, tuples are immutable.
print(tuple_element)


# In[77]:


set_structure = {1,2,3,4,5,6,7,8,1,1,1,1,7,8,7,6,6,6,6,5,5}
print(set_structure) ########### it will return the unique elements in the set called set_structure. Because by definition, a set contains unique elements.


# In[78]:


set_structure.add(7) ########already existing in the set, thus, it will not add 7 to the set called set_structure.
print(set_structure)

set_structure.add(9) ########non-existing in the set, thus, it will add 9 to the set called set_structure.
print(set_structure)


# In[79]:


1 > 5 ###########greater than operator


# In[80]:


5 >= 1 ###########greater than or equal to operator


# In[81]:


5 > 1 ############greater than operator


# In[82]:


1 >= 5 ###########greater than or equal to operator


# In[83]:


1 == 5 ###########equal to operator


# In[84]:


1 < 5  ############less than operator


# In[85]:


1 <= 5 ############less than or equal to operator


# In[86]:


3 != 3 #############checks the inequality. If both sides are not equal, it will return true. Otherwise, it will return false.


# In[87]:


print(3 != 3)


# In[88]:


11 != 5


# In[89]:


print(11 != 5)


# In[91]:


(3 < 9) and (5 >= 5) ####Usage of the and operator to combine multiple checks.


# In[92]:


(4 > 1) or (8 < 6) ####Usage of the or operator.


# In[93]:


print(True or True)
print(True or False)
print(True and True)
print(True and False)
print(False and False)
print(False or False)


# In[94]:


if 3 < 9:
    print("Hello World !")
    

if 2 == 2:
    print("The equality is satisfied.")
else:
    print("The equality is not satisfied.")
    
    
if 7 == 2:
    print("The equality is satisfied.")
else:
    print("The equality is not satisfied.")
    


# In[95]:


set([1,9,9,10,3,3,3,3,7,8,5,6,6,1,1,0,9,9,4,3,5,0]) ######it will grab the unique elements in the list


# In[97]:


print(set([2,8,8,3,3,3,3,7,8,5,6,6,1,1,0,9,9,4,3,5,0]))


# In[98]:


seq = [1,2,3,4,5,6,7,8,9,10]

###########iterate through the list by using a for loop and print each element of the list.
for item in seq:
    print(item)


# In[3]:


#########Usage of while loop in Python
w = 1
while(w < 5):
    print("w is "+str(w)+"")
    print("w is: {one}".format(one=w))
    print("------------------------------------")
    print()
    w+=1
    
print()
print()
    
print("---------------------------------------------------------------------------")
k = 1
while(k < 5):
    print("k is "+str(k)+"")
    print("k is: {one}".format(one=k))
    print("------------------------------------")
    print()
    k = k + 1


# In[4]:


###############range function in python
range(0,6)


# In[5]:


##Iterate through the range starting at 0 and ending at 5 (exclusive).
##The end value that is specified for the range function is not included.
##Perform iterations by using a for loop
for x in range(0, 6):
    print(x) 


# In[7]:


print(list(range(10))) #####construct a list consisting of numbers from 0 to 9, incrementing by 1  and not including 10.
print(list(range(2,8))) ####construct a list consisting of numbers from 2 to 7, incrementing by 1 and not including 8.
print(list(range(3,33,3))) ### construct a list consisting of numbers from 3 to 30, incrementing by 3 and not including 33.


# In[4]:


#####Python List Comprehension#######

##########Without list comprehension
my_list = [1,2,3,4,5,6]
out_list = []
for index, num in enumerate(my_list):
    if index % 2 == 0:
        out_list.append(num**2)
    else:
        out_list.append(num**3)
        
print(out_list)


##########With list comprehension
output_list = [num**2 if index%2==0 else num**3 for index, num in enumerate(my_list)]
print(output_list)


# In[5]:


output_list


# In[18]:


#################Defining a function in python
def my_function(param1: int,  param2: int, param3: int):
    return param1**2, param2**2, param3**2
    
print(my_function(param1 = 1,param2 = 2, param3 = 3))
print(my_function(1,2,3))

print()

def my_func(param1, param2):
    print(param1)
    print(param2)
    print()
    
    
my_func("Hello", 33)
my_func("World", 77)


# In[23]:


def greetings_func(name = "Mike"):
    return "Hello" + " " + str(name) + " "

print(greetings_func("Garry"))
print(greetings_func("Rachel"))


# In[27]:


def square_num(num):
    """
    This is a documentation for this function. This function takes an integer or float parameter 
    and returns the square of it.
    """
    if not (isinstance(num, int) or isinstance(num, float)):
        raise Exception("The square can only be computed for integer or float parameters.")
    
    return num**2

print(square_num(4))
print(square_num(-13.5))
print(square_num(0))
print(square_num(1.25))

output_number = square_num(9)
print(output_number)


# In[28]:


print(square_num("Hello")) ####Here, the parameter is a string. Thus, it will throw the error specified above.


# In[31]:


#################Lambda expressions, map and filter functions
def multiply_by_2(var):
    return var * 2

my_seq = [1,2,3,4,5,6,7,8,9,10]
map(multiply_by_2, my_seq) 
print(map(multiply_by_2, my_seq))  #####this will print the memory location of the map object.

#######usage of map function in Python
print(list(map(multiply_by_2, my_seq)))  #########do the mapping operation using multiply_by_2 function, convert map to a list, and print the list.


# In[34]:


####usage of map() function and lambda expression while creating a list in python.
result = list(map(lambda num: num**3, my_seq))
print(result)


# In[37]:


###########filter() function in python

#####Usage of filter() and list() functions and lambda expression while creating a filtered list in Python.
print(list(filter(lambda num: num%2==0, my_seq)))


# In[38]:


filter(lambda num: num%2==0, my_seq)
list(filter(lambda num: num%2==0, my_seq))


# In[40]:


my_string = "Hello World! My name is Baris."

lowered_string = my_string.lower()  # Converts all characters in a string to lowercase.

print(lowered_string)


# In[41]:


upper_string = my_string.upper()  # Converts all characters in a string to uppercase.

print(upper_string)


# In[44]:


splitted = my_string.split(' ') #It splits the text according to the empty space and creates an array of words.
splitted_arr = my_string.split() #It splits the text according to the empty space and creates an array of words.

print(splitted)
print(splitted_arr)


# In[46]:


tweet_string = "Go Sports! #Sports"

tweet_words_arr = tweet_string.split("#") ####It will split the tweet based on the #
print(tweet_words_arr)

print(tweet_words_arr[0])
print(tweet_words_arr[1])


# In[47]:


my_dictionary = {'key1': 10, 'key2': 20, 'key3': 30, 'key4': 40}
print(my_dictionary)


# In[48]:


my_dictionary


# In[51]:


######returns the keys of the dictionary
my_dictionary.keys()


# In[52]:


######returns the values of the dictionary
my_dictionary.values()


# In[50]:


######returns the items of the dictionary
my_dictionary.items()


# In[54]:


lst = [0, 1, 2, 3, 4, 5]

print(lst)
item = lst.pop()
print(item)
print(lst)
second_popped = lst.pop()
print(second_popped)
print(lst)
lst.append(3)
print(lst)


# In[55]:


print(lst)
popped_element = lst.pop(0) ####pop the element at index 0 from the list called lst.
print(popped_element)
pop_elm = lst.pop(1) ####pop the element at index 1 from the list called lst.
print(pop_elm)
print(lst)


# In[58]:


###################How to check whether a value is in a list
#####By using in function, we can achieve this.
print(1 in lst) #It will return true
print("Hello1" in ["Hello1", "Hello2", "Hello3"]) #It will return true
print(8 in [1, 2, "World"]) #It will return false


# In[64]:


############Tuple Unpacking in Python
my_tuple_lst = [(1,2), (3,4), (5,6)]
print(my_tuple_lst)


# In[65]:


print(my_tuple_lst[0])
print(my_tuple_lst[0][0])
print(my_tuple_lst[0][1])


# In[67]:


for item in my_tuple_lst:
    print(item)
    
print()
for a,b in my_tuple_lst:
    print(a, b)
    print(a)
    print(b)
    print()


# In[68]:


###########Python Exercises
#####What is 7 to the power of 9?
7**9


# In[69]:


print(7**9)


# In[70]:


##############Split "Hi there Barış"#################
s = "Hi there Barış"
split_arr = s.split(" ")
print(split_arr)


# In[88]:


################Write a function that returns the user name and domain name as a tuple given the following email address structure:
#############username@domain.com

def getUsernameAndDomainName(email_address):
    if (email_address is None) or (type(email_address) != str):
        raise ValueError("Email address should be a specified string!")

    split_array = email_address.split("@")
    if len(split_array) != 2:
        raise ValueError("Invalid email address format!")

    username = split_array[0]
    domain = split_array[1]
    return username, domain


print(getUsernameAndDomainName("baris@ku.edu.tr"))



#########Count how many times the string 'dog' occurs in a string################

import re


def countDog1(st):
    words = st.lower().split()
    dog_count = 0

    for word in words:
        # Remove punctuation from each word
        cleaned_word = ''.join(char for char in word if char.isalnum())

        # Check if the cleaned word is "dog"
        if cleaned_word == "dog":
            dog_count = dog_count + 1

    return dog_count 


def countDog2(st):
    # Usage of regular expression to find all occurrences of "dog" regardless of punctuation
    dog_count = len(re.findall(r'\bdog\b', st.lower()))
    return dog_count

print(countDog1("Hi dog come here my little dog!"))
print(countDog2("Hi dog come here my little dog!"))




# In[ ]:





# In[ ]:




