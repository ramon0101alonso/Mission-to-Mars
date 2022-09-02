#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
#module 10.3.5
import pandas as pd


# In[2]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[3]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)

#searching for elements with a specific combination of tag div and attribute list_text
#time.sleep(1) pass seconds you want 1 seconds  the own line this line is first
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[4]:


#why are there two searches for the same thing div list_text???????????
html = browser.html
news_soup = soup(html, 'html.parser')
#selcet_one returns the first matching element. this variable holds a lot of info
slide_elem = news_soup.select_one('div.list_text')


# In[5]:


slide_elem.find('div', class_='content_title')


# In[6]:


#we are looking for the title of the article
# Use the parent element to find the first `a` tag and save it as `news_title`
#adding get_text, returns only the the text of the element
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[7]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# #module 10.3.4 go to Markdown below widgets to change back to Code
# ### Featured Images

# In[8]:


# Visit URL so we can start searching for images
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[9]:


# Find and click the full image button we do this because theres less than 3 buttons and index 1 gives us the second pic
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[10]:


#looking for the full image after we pressed the full image button and choose index 1 pic
# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[11]:


#we are telling beautifulsoup to look inside the img tag with a class of fancybox.  Here is where the pic lives
# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[12]:


#after getting the img_url_rel (this pic will always change but the route is the same) add the url to get latest pic
# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# In[13]:


#module 10.3.5
#create a new df with pandas function read_html, looks for all tables and gives them an index 0 is the first table
df = pd.read_html('https://galaxyfacts-mars.com')[0]
#adding columns
df.columns=['description', 'Mars', 'Earth']
#set_index makes the description column into the df's index inplace=true wont create a new table 
df.set_index('description', inplace=True)
df


# In[14]:


#now we take this df and convert it back into HTML with .to_html()
df.to_html()


# In[15]:


browser.quit()


# In[ ]:




