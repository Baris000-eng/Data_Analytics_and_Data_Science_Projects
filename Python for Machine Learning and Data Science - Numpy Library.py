#!/usr/bin/env python
# coding: utf-8

# In[4]:


my_list = [1,2,3,4,5,6,7,8,9,10]
print(my_list)


# In[5]:


import numpy as np
print(np.array(my_list))

my_arr = np.array(my_list)
print(my_arr)


# In[6]:


my_arr


# In[7]:


my_matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(my_matrix)
print(my_matrix[0],my_matrix[1],my_matrix[2])
print(np.array(my_matrix))


# In[8]:


np.array(my_matrix)


# In[9]:


########usage of np.arange() function
np.arange(0,10)


# In[10]:


np.arange(0, 11)


# In[11]:


np.arange(0,11,2)


# In[12]:


np.zeros(5) ###creating a numpy array of 5 floats all of which are set to 0.0


# In[13]:


print(np.zeros(10)) ###creating a numpy array of 10 floats all of which are set to 0.0, and printing this array


# In[14]:


np.random.rand(7)


# In[15]:


np.random.randn(10)


# In[16]:


np.random.rand(7,7) ##generates a 7 by 7 matrix where each element is drawn from a uniform distribution over [0,1).


# In[17]:


print(np.random.randn(11,11)) ##generates a 11 by 11 matrix where each element is drawn from a standard normal distribution.


# In[18]:


print(np.ones(5))


# In[19]:


print(np.random.randint(1, 100, 10)) ####gets 10 random integers from the range starting at 1 and ending at 99.


# In[20]:


arr = np.arange(0, 100)
print(arr)


# In[21]:


##########Reshape method of Numpy
arr.reshape(10,10) #####reshaping the array into 10 by 10 array.


# In[22]:


rand_arr = np.random.randint(1, 100, 10)
rand_arr.min()


# In[23]:


rand_arr.max()


# In[24]:


print(rand_arr.argmax()) ###gets the index of the maximum element
print(rand_arr.argmin()) ###gets the index of the minimum element


# In[25]:


##########usage of shape() function to determine the number of rows and columns in an array
arr.shape


# In[26]:


rand_arr.shape


# In[27]:


arr.shape[0]


# In[28]:


rand_arr.shape[0]


# In[29]:


from numpy.random import randint
randint(2,10)


# In[30]:


###Numpy Indexing and Selection
import numpy as np


# In[31]:


my_array = np.arange(0,11)
print(my_array)


# In[32]:


my_array


# In[33]:


print("First element of the my_array: "+str(my_array[0])+"")
print("Second element of the my_array: "+str(my_array[1])+"")
print("Third element of the my_array: "+str(my_array[2])+"")

print(my_array[3:9]) ###get the elements starting at index 3 and ending at index 8 (index 9 is exclusive)


# In[34]:


slice_of_arr = my_array[0:6]
print(slice_of_arr)


# In[35]:


slice_of_arr[:] = 99


# In[36]:


print(slice_of_arr)
print(my_array)


# In[37]:


#######usage of copy() method
copy_arr = my_array.copy()

copy_arr[:] = 111 ###make all elements in the copy array 111
print(copy_arr) 
print(my_array)


# In[38]:


#####Indexiing a 2D Numpy Array

array_2d = np.array([[10,15,20],[25,30,35],[40,45,50]])


# In[39]:


array_2d


# In[40]:


###Double Bracket Format to reach elements in a 2D Numpy array
array_2d[0][1]


# In[41]:


print(array_2d[0][0])  ##10
print(array_2d[0][1])  ##15
print(array_2d[0][2])  ##20

print()

print(array_2d[1][0])  ##25
print(array_2d[1][1])  ##30
print(array_2d[1][2])  ##35

print()

print(array_2d[2][0])  ##40
print(array_2d[2][1])  ##45
print(array_2d[2][2])  ##50


# In[42]:


######Comma notation to reach elements in a 2D Numpy array
print(array_2d[0,0]) #10
print(array_2d[0,1]) #15
print(array_2d[0,2]) #20


# In[43]:


# Selects elements in the 2D array 'array_2d' from the first two rows (up to the 2nd row)
# and starting from the second column (column 1 onwards).
array_2d[:2,1:] 


# In[44]:


print(array_2d[:2]) ##grab the first two rows


# In[45]:


arr = np.arange(1,21)


# In[46]:


arr


# In[47]:


bool_arr = arr < 15


# In[48]:


bool_arr


# In[49]:


arr[bool_arr] ##get the slice of the arr where bool_arr is true.


# In[50]:


print(arr[bool_arr]) ##get the slice of the arr where bool_arr is true.


# In[51]:


arr[arr > 7]


# In[52]:


arr[arr <= 11]


# In[53]:


arr_2d = np.arange(50).reshape(5,10)
print(arr_2d)


# In[54]:


print(arr_2d[1:3,3:5]) ##from row1 to row2 and from column3 to column4.


# In[55]:


####Numpy Operations
import numpy as np

my_arr = np.arange(0,11)


# In[56]:


my_arr


# In[57]:


my_arr + my_arr


# In[58]:


3 * my_arr - 9 * my_arr


# In[59]:


my_arr + 1000


# In[60]:


arr / arr


# In[61]:


my_arr / my_arr


# In[62]:


1/0


# In[63]:


1/my_arr


# In[64]:


print(my_arr**3)


# In[65]:


print(my_arr**2)  # Squares each element in my_arr.


# In[66]:


np.sqrt(my_arr**3)


# In[67]:


np.sqrt(my_arr)


# In[68]:


print(np.sqrt(my_arr**5)) ##usage of np.sqrt function to get the square root of each element in the array.


# In[69]:


print(np.exp(my_arr)) ###calculates the exponential of each element in the array.


# In[70]:


np.max(my_arr)


# In[71]:


print(np.max(my_arr))


# In[72]:


print(np.sin(my_arr))
print()
print(np.cos(my_arr))
print()
print(np.tan(my_arr))
print()
print(1/np.tan(my_arr))


# In[73]:


np.log(my_arr)


# In[74]:


print(np.add(1,2))


# In[75]:


result = np.subtract(np.max([5, 3]), np.min([77, 9]))
print(result)


# In[76]:


np.random.rand(25) #Generates 25 random numbers from a uniform distribution (numbers are between 0 and 1).


# In[77]:


np.random.randn(30)  #30 random numbers drawn from a standard normal distribution.


# In[78]:


np.linspace(0,1,20) #creates 20 linearly spaced points between 0 and 1.


# In[79]:


mat = np.arange(1,26).reshape(5,5)
print(mat)


# In[80]:


print(mat[2:5,1:])
print()
print(mat[2:5])


# In[82]:


##axis = 0 (columnwise summation)##
##axis = 1 (rowwise summation)##


sum_of_all = mat.sum()
print("Summation of all values in the matrix mat is:  "+str(sum_of_all)+"")

columnwise_summations = mat.sum(axis = 0)
print("Columnwise summations for the matrix mat are: "+str(columnwise_summations)+"")

rowwise_summations = mat.sum(axis = 1)
print("Rowwise summations for the matrix mat are: "+str(rowwise_summations)+"")

standard_dev = mat.std()
print("The standard deviation of the values in the matrix mat is: "+str(standard_dev)+"")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




