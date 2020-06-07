#!/usr/bin/env python
# coding: utf-8

# # reduce

# In[14]:


from functools import reduce
 
def do_sum(x1, x2):
    return x1 + x2
 
 
reduce(do_sum, [1, 2, 3, 4])


# In[15]:


def do_sum(x1, x2): 
    return x1 + x2

def my_reduce(func, seq):
    first = seq[0]
    for i in seq[1:]:
        first = func(first, i)
    return first

print(my_reduce(do_sum, [2,6,7,8,9]))


# # Implement List comprehensions to produce the lists

# In[16]:


word = "ACADGILD"
alphabet_list = [ alphabet for alphabet in word ]
print ("ACADGILD => " + str(alphabet_list))


# In[17]:


input_list = ['x','y','z']
result = [ item*num for item in input_list for num in range(1,5)  ]
print("['x','y','z'] => " +   str(result))


# In[18]:


input_list = ['x','y','z']
result = [ item*num for num in range(1,5) for item in input_list  ]
print("['x','y','z'] => " +   str(result))


# In[19]:


input_list = [2,3,4]
result = [ [item+num] for item in input_list for num in range(0,3)]
print("[2,3,4] =>" +  str(result))


# In[20]:


input_list = [2,3,4,5]
result = [ [item+num for item in input_list] for num in range(0,4)  ]
print("[2,3,4,5] =>" +  str(result))


# In[21]:


input_list=[1,2,3]
result = [ (b,a) for a in input_list for b in input_list]
print("[1,2,3] =>" +  str(result))


# # Implement a function longestWord() that takes a list of words and returns the longest one.

# In[25]:


def find_longest_word(words_list):
    word_len = []
    for n in words_list:
        word_len.append((len(n), n))
    word_len.sort()
    return word_len[-1][1]
b=["PHP", "Exercises", "Backend","vikas","charaanana"]

print(find_longest_word(b))


# # Write a Python Program(with class concepts) to find the area of the triangle using the below formula.

# In[26]:


# Python Program to find the area of triangle

a = 5
b = 6
c = 7

# Uncomment below to take inputs from the user
# a = float(input('Enter first side: '))
# b = float(input('Enter second side: '))
# c = float(input('Enter third side: '))

# calculate the semi-perimeter
s = (a + b + c) / 2

# calculate the area
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print('The area of the triangle is %0.2f' %area)


# # Write a function filter_long_words() that takes a list of words and an integer n and returns the list of words that are longer than n 

# In[27]:


def filterlongword(string,number):

    for i in range(len(string)):
        listwords = []
        if len(string[i]) > number:
            listwords.append(string[i])

        return listwords 


def main():
    words = input("Please input the list of words: ")
    integer = eval(input("Please input an integer: "))

    words1 = filterlongword(words,integer)

    print("The list of words greater than the integer is",words1)

main()  


# # Write a Python program using function concept that maps  list of words into a list of integers representing the lengths of the corresponding words​. 

# In[29]:



listOfWords = ['vikas','vinay','anil','aryan','krishna']
 
listOfInts = []
 
for i in range(len(listOfWords)):
    listOfInts.append(len(listOfWords[i]))
 
print ("List of words:"+str(listOfWords))    
print ("List of wordlength:"+str(listOfInts))


# In[ ]:




