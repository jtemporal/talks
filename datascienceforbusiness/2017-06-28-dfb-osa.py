
# coding: utf-8

# # Expenses in closed companies
# Recently we found out that there are many companies that are already closed or out of service, we are aiming to find if there are expenses made after the company situation as other than open.

# In[1]:

import pandas as pd
import numpy as np
from serenata_toolbox.datasets import fetch


#  

#  

#  

#  

#  

#  

#  

#  

# In[ ]:

fetch('2016-09-03-companies.xz', 'data/')
fetch('2016-11-19-reimbursements.xz', 'data/')


#  

#  

#  

#  

#  

#  

#  

#  

# In[2]:

companies = pd.read_csv('data/2016-09-03-companies.xz', low_memory=False)
reimbursements = pd.read_csv('data/2016-11-19-reimbursements.xz',
                      dtype={'applicant_id': np.str,
                             'cnpj_cpf': np.str,
                             'congressperson_id': np.str,
                             'subquota_number': np.str},
                      low_memory=False)


#  

#  

#  

#  

#  

#  

#  

#  

# In[3]:

companies.head(3)


#  

#  

#  

#  

#  

#  

#  

#  

# In[4]:

reimbursements.head(3)


#  

#  

#  

#  

#  

#  

#  

#  

# ## Formatting
# Formatting companies situation_date and reimbursements issue_date columns to correct date format (will be needed for a query later), and formatting the companies cpnj to a format without dash and dots.

# In[5]:

df = pd.DataFrame({'year': [2015, 2016],
                   'month': [2, 3],
                   'day': [4, 5],})
pd.to_datetime(df)


#  

#  

# In[6]:

reimbursements.iloc[0]['issue_date']


#  

#  

#  

#  

#  

#  

#  

#  

# In[7]:

reimbursements['issue_date'] = pd.to_datetime(reimbursements['issue_date'],
                                              errors='coerce')
companies['situation_date'] = pd.to_datetime(companies['situation_date'],
                                             errors='coerce')


# In[8]:

reimbursements.iloc[0]['issue_date']


#  

#  

#  

#  

#  

#  

#  

#  

# In[9]:

companies.iloc[0]['cnpj']


# In[10]:

companies['cnpj'] = companies['cnpj'].str.replace(r'\D', '')
companies.iloc[0]['cnpj']


#  

#  

#  

#  

#  

#  

#  

#  

# ## Not 'ABERTA'

# In[11]:

statuses = ['BAIXADA', 'NULA', 'SUSPENSA', 'INAPTA']
not_open = companies[companies['situation'].isin(statuses)]
not_open[['cnpj', 'situation_date','situation']].head(5)


#  

#  

#  

#  

#  

#  

#  

#  

# In[12]:

not_open.shape


#  

#  

#  

#  

#  

#  

#  

#  

# The column situation_date is the one that is interesting. Expenses made after that date should be considered suspicious.
# 
# The inner join on merge will give reimbursements that were requested for out of service companies.

# In[13]:

dataset = pd.merge(reimbursements,
                   not_open,
                   left_on='cnpj_cpf',
                   right_on='cnpj')


#  

#  

#  

# In[14]:

dataset.shape


#  

#  

#  

#  

#  

#  

#  

#  

# In[15]:

columns = ['congressperson_name',
           'issue_date','cnpj',
           'situation_date',
           'situation']
dataset[columns].head(10)


#  

#  

#  

#  

#  

#  

#  

#  

#  

# In[16]:

dataset.iloc[0]


#  

#  

#  

#  

#  

#  

#  

#  

# ## Filtering suspicious reimbursements
# We have all reibursements requested for expenses made in companies that have situation other than "open".
# It is still necessary to check the reimbursement issue_date is "bigger" than the situation_date.

# In[17]:

expenses_in_closed_companies = dataset.query('issue_date > situation_date')
expenses_in_closed_companies[columns].head()


#  

#  

#  

#  

#  

#  

#  

#  

# In[18]:

expenses_in_closed_companies.shape


# We can safely say that there are 5222 suspicious reimbursements.
