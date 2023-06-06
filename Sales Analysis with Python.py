#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Importing Python Libraries 

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


# Loading data into a Jupyter Notebook

sales = pd.read_excel("D:\Business Analytics\Python Projects\Deepavali Sales Analysis\Sales Data.xlsx")


# In[4]:


# Understanding the Data and defining the data

sales.shape # shape will provide the numbers of row and columns are there in dataset


# In[5]:


sales.head() # head() will return the first five rows including all variables, if we mention specific number it will return all the specified numbers of rows.


# In[6]:


sales.tail() # tail() will return the last 5 rows, as like head() function.


# In[7]:


sales.head(10)


# In[8]:


sales.info() # it display the information about the dataset


# In[9]:


sales.columns # it display all the columns in the dataset


# In[10]:


# in our dataset we have 2 unwanted columns so we can drop them

sales.drop(['Status', 'unnamed1'], axis=1, inplace=True) # axis=1 means it works on vertical level, inplace=True means we want this modification apply permanently


# In[11]:


# now we can check those columns in dataset in 2 way

sales.columns


# In[12]:


sales.info()


# In[13]:


# now we can check is there any null values is present in dataset

pd.isnull(sales).sum()


# In[14]:


# In our dataset has 12 null values in amount column that means,
# Customer has selected the product and kept in cart but not done payment so order process not completed
# We have very less null values we can avoid them by deleting

sales.dropna(inplace=True)


# In[15]:


# we can confirm them wheather the null values are deleted or not

sales.info()


# In[16]:


pd.isnull(sales).sum()


# In[17]:


# In our dataset we can see the data type of the 'Amount' variable is 'float64', 
# we are not going to deal with any decimal value so can chenge into 'integer'

sales['Amount'] = sales['Amount'].astype('int32')


# In[18]:


sales.info()


# In[19]:


# We can also check each individual dtypes 

sales['Amount'].dtypes


# In[20]:


sales.describe() # it display the description of the data in a DataFrame


# In[21]:


# we can also check this description with numerical data by mentioning them in square bracket

sales[['Age','Orders','Amount']].describe()


# # now our data is ready to perform EDA 

# # Exploratory Data Analysis

# # Gender Category

# In[22]:


# plot the bar chart on gender category with total count

barchart=sns.countplot(x='Gender', data=sales)
for bars in barchart.containers:
    barchart.bar_label(bars)


# In[24]:


# plotting the bar chart on Gender category and the amount they have spend in shopping

sales_gender = sales.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
sns.barplot(x='Gender', y='Amount', data=sales_gender)


# from the above graph we can see that most of the buyers are females and the purchasing power of the females are greater than men.

# # Age Group

# In[25]:


age_group = sns.countplot(data=sales, x='Age Group', hue='Gender')
for bars in age_group.containers:
    age_group.bar_label(bars)


# In[26]:


# now we can see that total amount spent by each age group

sales_age = sales.groupby(['Age Group'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
sns.barplot(x='Age Group', y='Amount', data=sales_age)


# From above graphs we can see that most of the buyers are of age group between 26-35 yrs female

# # State wise total orders and sales

# In[29]:


# now can calculate the top 10 states have made total number of orders

sales_state = sales.groupby(['State'], as_index=False)['Orders'].sum().sort_values(by='Orders',ascending=False).head(10)

sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(x='State', y='Orders',data=sales_state)


# from the above graph we can see that highest orders are from UP followed by MH and KA

# In[32]:


# total amount/sales from top 10 states

sales_amount = sales.groupby(['State'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(x='State', y='Amount', data=sales_amount)


# from the total numbers of orders have made by top 10 state graph we can see that Kerala has 8th place but, in the total amount 
# spent by top 10 graph Kerala has not even in the 10th place.

# # Marital Status

# In[34]:


marital_status = sns.countplot(x="Marital_Status", data=sales)
sns.set(rc={'figure.figsize':(3,5)})
for bars in marital_status.containers:
    marital_status.bar_label(bars)


# In[35]:


sales_status = sales.groupby(['Marital_Status','Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)
sns.set(rc={'figure.figsize':(6,5)})
sns.barplot(data=sales_status, x='Marital_Status', y='Amount',hue='Gender')


# from the above graph we can see that most buyers are married(women)and they have high purchasing power.

# # Occupation

# In[37]:


sns.set(rc={'figure.figsize':(20,5)})
ocp = sns.countplot(data=sales, x='Occupation')
for bars in ocp.containers:
    ocp.bar_label(bars)


# In[38]:


Ocp_total_sales = sales.groupby(['Occupation'], as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)
sns.barplot(data=Ocp_total_sales, x='Occupation',y='Amount')


# from the above graph we can see that most of the buyers are working in IT Sector followed by Healthcare and Aviation

# # Product Category

# In[41]:


sns.set(rc={'figure.figsize':(20,5)})
products = sns.countplot(data=sales, x='Product_Category')

for bars in products.containers:
    products.bar_label(bars)


# In[44]:


product_total_sales = sales.groupby(['Product_Category'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)
sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data=product_total_sales, x='Product_Category', y='Amount')


# from the above graph can see that most of the sold products from the Food Category followed by Clothing ad Electronics

# In[45]:


# top10 most sold products

fig1, ax1= plt.subplots(figsize=(12,7))
sales.groupby('Product_ID')['Orders'].sum().nlargest(10).sort_values(ascending=False).plot(kind='bar')


# # Conclusion:

# Who are more likely to buy:
#     
# * Married women age group 26-35 yrs and they have high purchasing power  
# * They are from UP, Maharastra and Karnataka
# * They are working in IT, Healthcare and Aviation
# * Most sold products are from Food, Clothing and Electronics category
