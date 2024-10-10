#!/usr/bin/env python
# coding: utf-8

# In[349]:


# Coffee Shop simulator program


# In[350]:


# Author: Christian Garcia


# In[351]:


# This program displays a menu of food items which the user may then select any amount


# In[352]:


# The program will add the items value together with a tax of 6% 


# In[353]:


# The print statements below are the opening of the program


# In[ ]:


# Prices of the Coffee and and Muffins


# In[ ]:


COFFEE_PRICE = 5.00


# In[ ]:


MUFFIN_PRICE = 4.00


# In[ ]:


TEA_PRICE = 2


# In[ ]:


SCONE_PRICE = 3


# In[ ]:


TAX_RATE = 0.06


# In[ ]:


print("My Coffee and Muffin Shop")


# In[ ]:


# Asks user for amount of coffee & muffins they want


# In[ ]:


num_coffees = int(input("Number of coffees bought?"))


# In[ ]:


num_muffins = int(input("Number of muffins bought?"))


# In[ ]:


num_tea = int(input("Number of tea bought?"))


# In[ ]:


num_scone = int(input("Number of scones bought?"))


# In[ ]:


# Calculates the subtotal of the order


# In[ ]:


subtotal_coffee = num_coffees * COFFEE_PRICE


# In[ ]:


subtotal_muffin = num_muffins * MUFFIN_PRICE


# In[ ]:


subtotal_tea = num_tea * TEA_PRICE


# In[ ]:


subtotal_scone = num_scone * SCONE_PRICE


# In[ ]:


subtotal = subtotal_coffee + subtotal_muffin + subtotal_tea + subtotal_scone


# In[ ]:


# Calculates the subtotal with tax


# In[ ]:


tax = subtotal * TAX_RATE


# In[ ]:


# Adds up the total amount with subtotal and tax


# In[ ]:


total = subtotal + tax


# In[ ]:


# Shows the receipt to user


# In[ ]:


print("*"*50)


# In[ ]:


print("My Coffee and Muffin Shop")


# In[ ]:


print("*"*50)


# In[ ]:


print("*"*50) 


# In[ ]:


print("My Coffee and Muffin Shop Receipt")


# In[ ]:


print(f"{num_coffees} Coffee(s) at ${COFFEE_PRICE:.2f} each: ${subtotal_coffee:.2f}")


# In[ ]:


print(f"{num_muffins} Muffin(s) at ${MUFFIN_PRICE:.2f} each: ${subtotal_muffin:.2f}")


# In[ ]:


print(f"{num_tea} Tea(s) at ${TEA_PRICE:.2f} each: ${subtotal_tea:.2f}")


# In[ ]:


print(f"{num_scone} Scone(s) at ${SCONE_PRICE:.2f} each: ${subtotal_scone:.2f}")


# In[ ]:


print(f"6% tax: ${tax:.2f}")


# In[ ]:


print("*"*50)


# In[ ]:


print(f"Total: ${total:.2f}")


# In[ ]:


print("*"*50)


# In[ ]:


print('Thank you for coming out to the Coffee and Muffin shop! Please come again soon.')


# In[ ]:





# In[ ]:




