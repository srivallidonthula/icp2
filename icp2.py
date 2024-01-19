#!/usr/bin/env python
# coding: utf-8

# In[6]:


#Question1
first_name= input("enter first name : ")
last_name= input("enter last name : ")

#full_name is both first name and last name
def full_name(first_name,last_name):
    return first_name +" "+last_name
#string_alternative function will prints the data alternatively
def string_alternative(full_name):
    new_str = ""
    for index in range(0,len(full_name),2):
                       new_str+=full_name[index]        
    return new_str               

print("User full name : ",full_name(first_name,last_name))

print("Alternate String : ",string_alternative(full_name(first_name,last_name)))


# In[1]:


#Question2
text=open("input.txt","r")
d=dict()
for line in text:
    line=line.strip()
    line=line.strip()
    words=line.split(" ")
    for word in words:
        
        if word in d:
            d[word]=d[word]+1
        else:
            d[word]=1
for key in list(d.keys()):
    print(key,":",d[key])


# In[4]:


#Question3
#Read the input data of customer heights in inches
data =input("enter customer heights : ")
#convert the height of customer in inches to centimeters
def inchToCent(value):
    return value*2.54

heights = data.split()

new_list = []

for x in heights:
    value = int(x)
    new_list.append(inchToCent(value))
    
print("show list : ",new_list)


# In[ ]:




