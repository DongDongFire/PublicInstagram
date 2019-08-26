#!/usr/bin/env python
# coding: utf-8

# In[1]:


import selenium
from selenium import webdriver as wd
from selenium.webdriver.chrome.options import Options

__all__=['IG_Business']

class IG_Business:
    
    def get_public(channel_name):
        options = Options()
        options.add_argument('headless')
        options.add_argument('window-size=1920x1080')
        options.add_argument("disable-gpu")

        driver=wd.Chrome(executable_path ='C:/chromedriver.exe',chrome_options=options)
        url='https://www.instagram.com/'+channel_name
        driver.get(url)
        
        driver.implicitly_wait(10)
        source=driver.page_source
        if 'is_business_account":true' in source:
            print(channel_name," is a public account")
            return 'Public Account',url
        else:
            return 'Not Public Account',url






