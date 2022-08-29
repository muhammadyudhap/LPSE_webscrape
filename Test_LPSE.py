#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# # Title Page

# In[2]:


df_title = pd.read_html('https://lpse.atrbpn.go.id/eproc4')


# In[3]:


df_title[0].head()


# In[4]:


df_title[1].head()


# # Tender/Lelang Page

# In[5]:


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


# In[6]:


website_lelang = "https://lpse.atrbpn.go.id/eproc4/lelang"


# In[7]:


import os


# In[8]:


path = ".\chromedriver"
options = Options()
options.headless = True
service = Service(executable_path = path)
driver = webdriver.Chrome(service = service, options = options)


# In[9]:


driver.get(website_lelang)


# In[10]:


from time import sleep


# In[11]:


sleep(2)


# In[12]:


from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


# In[13]:


select = Select(driver.find_element(By.NAME, 'tbllelang_length'))
select.select_by_visible_text('Semua')


# In[14]:


sleep(10)


# In[15]:


df_lelang = pd.read_html(driver.page_source, attrs = {'id': 'tbllelang'})[0]


# In[16]:


df_lelang


# In[17]:


from datetime import datetime
import sys


# In[18]:


application_path = os.getcwd()


# In[19]:


now = datetime.now()
day_month_year = now.strftime("%d-%m-%Y")
file_name = f'Lelang_{day_month_year}.csv'
final_path = os.path.join(application_path, file_name)


# In[20]:


df_lelang.to_csv(final_path)


# # NonTender Page

# In[21]:


website_nontender = "https://lpse.atrbpn.go.id/eproc4/nontender"


# In[22]:


driver.get(website_nontender)


# In[23]:


sleep(2)


# In[24]:


select = Select(driver.find_element(By.NAME, 'tbllelang_length'))
select.select_by_visible_text('Semua')


# In[25]:


sleep(10)


# In[26]:


df_nontender = pd.read_html(driver.page_source, attrs = {'id': 'tbllelang'})[0]


# In[27]:


df_nontender


# In[28]:


file_name = f'NonTender_{day_month_year}.csv'
final_path = os.path.join(application_path, file_name)


# In[29]:


df_nontender.to_csv(final_path)


# # Pencatatan NonTender

# In[30]:


website_pencatatannontender = "https://lpse.atrbpn.go.id/eproc4/pencatatan"


# In[31]:


driver.get(website_pencatatannontender)


# In[32]:


sleep(2)


# In[33]:


select = Select(driver.find_element(By.NAME, 'tbllelang_length'))
select.select_by_visible_text('Semua')


# In[34]:


sleep(10)


# In[35]:


df_pencatatannontender = pd.read_html(driver.page_source, attrs = {'id': 'tbllelang'})[0]


# In[36]:


df_pencatatannontender


# In[37]:


file_name = f'PencatatanNonTender_{day_month_year}.csv'
final_path = os.path.join(application_path, file_name)


# In[38]:


df_pencatatannontender.to_csv(final_path)


# # Swakelola 

# In[39]:


website_swakelola = "https://lpse.atrbpn.go.id/eproc4/swakelola"


# In[40]:


driver.get(website_swakelola)


# In[41]:


sleep(2)


# In[42]:


select = Select(driver.find_element(By.NAME, 'tblswakelola_length'))
select.select_by_visible_text('Semua')


# In[43]:


sleep(10)


# In[44]:


df_pencatatannontender = pd.read_html(driver.page_source, attrs = {'id': 'tblswakelola'})[0]


# In[45]:


df_pencatatannontender


# In[46]:


file_name = f'Swakelola_{day_month_year}.csv'
final_path = os.path.join(application_path, file_name)


# In[47]:


df_pencatatannontender.to_csv(final_path)


# # Pencatatan Pengadaan Darurat

# In[48]:


website_pengadaandarurat = "https://lpse.atrbpn.go.id/eproc4/darurat"


# In[49]:


driver.get(website_pengadaandarurat)


# In[50]:


sleep(2)


# In[51]:


select = Select(driver.find_element(By.NAME, 'tbllelang_length'))
select.select_by_visible_text('Semua')


# In[52]:


sleep(10)


# In[53]:


df_Darurat = pd.read_html(driver.page_source, attrs = {'id': 'tbllelang'})[0]


# In[54]:


df_Darurat


# In[55]:


file_name = f'PengadaanDarurat_{day_month_year}.csv'
final_path = os.path.join(application_path, file_name)


# In[56]:


df_Darurat.to_csv(final_path)


# In[57]:


sleep(10)


# In[58]:


driver.quit()

