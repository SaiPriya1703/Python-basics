#!/usr/bin/env python
# coding: utf-8

# In[1]:


my_list=[1, 'hello', 3.14, True]
print("Original List:",my_list)


# In[2]:


my_list.append('world')
print("List after appending world:",my_list)


# In[4]:


my_list.remove('world')
print("List after removing world:",my_list)


# In[5]:


my_tuple=(1, 'apple', 3.14, False)
print("Original Tuple:",my_tuple)


# In[7]:


#Accesing elements in tuple
print("1st element:",my_tuple[0])
print("Last element:",my_tuple[-1])


# In[12]:


for i in range(1, 6):
    print(i)


# In[15]:


i=2
while i<=5:
    print(i)
    i+=1


# In[16]:


number=int(input("Enter a number: "))
if number>0:
    print("positive number")
elif number<0:
    print("negative number: ")
else:
    print("number is zero")


# In[17]:


def greet(name):
    print(f"Hello,{name}!")
greet("alice")


# In[23]:


def sum(name,age):
    print(f"name and age:{name,age}")
sum("sai priya",20)


# In[ ]:




