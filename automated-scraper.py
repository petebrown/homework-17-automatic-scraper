#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import pandas as pd
import requests


# In[2]:


url = 'https://buckeyereporter.com/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36',
}

r = requests.get(url, headers=headers)

doc = BeautifulSoup(r.text)


# In[3]:


articles = []


# # Get FEATURED SECTION

# In[4]:


main_section = doc.select_one('.main__part')

section_title = 'Featured'


# ## Get top story

# In[5]:


top_story = main_section.select_one('.first-featured-title')

headline = top_story.select_one('h2.card-title').text.strip()

url = top_story.select_one('h2.card-title a')['href']
url = 'https://buckeyereporter.com' + url

preview_text = top_story.select_one('p.card-text').text.strip()

subsection = top_story.select_one('p.news-preview__label').text.strip()

subsection_url = top_story.select_one('p.news-preview__label a')['href']
subsection_url = 'https://buckeyereporter.com' + subsection_url

author = top_story.select_one('.card-author a').text.strip()
    
author_url = top_story.select_one('.card-author a')['href']
author_url = 'https://buckeyereporter.com' + author_url

article = {
    'section': section_title,
    'headline': headline,
    'url': url,
    'subsection': subsection,
    'subsection_url': subsection_url,
    'author': author,
    'author_url': author_url,
    'article_status': 'top_story',
    'preview_text': preview_text
}

articles.append(article)


# ## Get second story

# In[6]:


second_story = main_section.select_one('.second-featured-title')

headline = second_story.select_one('h2.card-title').text.strip()

url = second_story.select_one('h2.card-title a')['href']
url = 'https://buckeyereporter.com' + url

preview_text = second_story.select_one('p.card-text').text.strip()

subsection = second_story.select_one('p.news-preview__label').text.strip()

subsection_url = second_story.select_one('p.news-preview__label a')['href']
subsection_url = 'https://buckeyereporter.com' + subsection_url

author = second_story.select_one('.card-author a').text.strip()
    
author_url = second_story.select_one('.card-author a')['href']
author_url = 'https://buckeyereporter.com' + author_url

article = {
    'section': section_title,
    'headline': headline,
    'url': url,
    'subsection': subsection,
    'subsection_url': subsection_url,
    'author': author,
    'author_url': author_url,
    'article_status': 'second_featured_story',
    'preview_text': preview_text
}

articles.append(article)


# ## Get other featured stories

# In[7]:


top_stories = main_section.select('div.news-preview')

for story in top_stories:
    if 'first-featured-title' in story['class']:
        pass
    elif 'second-featured-title' in story['class']:
        pass
    else:
        headline = story.select_one('h2.card-title').text.strip()

        url = story.select_one('h2.card-title a')['href']
        url = 'https://buckeyereporter.com' + url

        preview_text = story.select_one('p.card-text').text.strip()

        subsection = story.select_one('p.news-preview__label').text.strip()

        subsection_url = story.select_one('p.news-preview__label a')['href']
        subsection_url = 'https://buckeyereporter.com' + subsection_url
        
        article = {
            'section': section_title,
            'headline': headline,
            'url': url,
            'subsection': subsection,
            'subsection_url': subsection_url,
            'author': '',
            'author_url': '',
            'article_status': '',
            'preview_text': preview_text
        }

        articles.append(article)


# ## Get rest of featured stories

# In[8]:


stories = main_section.select('li a')

for story in stories:
    headline = story.text
    url = story['href']
    url = 'https://buckeyereporter.com' + url
    
    article = {
        'section': section_title,
        'headline': headline,
        'url': url,
        'subsection': '',
        'subsection_url': '',
        'author': '',
        'author_url': '',
        'article_status': '',
        'preview_text': ''
    }

    articles.append(article)


# # Get OPINIONS

# In[9]:


opinion_section = doc.select_one('.sidebar')

section_title = opinion_section.select_one('.section-title').text.strip()

opinion_articles = opinion_section.select('li')

for article in opinion_articles:
    headline = article.select_one('h4 a').text.strip()
    
    url = article.select_one('h4 a')['href']
    url = 'https://buckeyereporter.com' + url
    
    author = article.select_one('.card-author a').text.strip()
    
    author_url = article.select_one('.card-author a')['href']
    author_url = 'https://buckeyereporter.com' + author_url
    
    article = {
        'section': section_title,
        'headline': headline,
        'url': url,
        'subsection': '',
        'subsection_url': '',
        'author': author,
        'author_url': author_url,
        'article_status': '',
        'preview_text': ''
    }

    articles.append(article)


# # Get DATA POINTS

# In[10]:


data_points_section = doc.select_one('section.data-points')

section_title = data_points_section.select_one('h2.section-title').text.strip()

data_point_stories = data_points_section.select('li')

for story in data_point_stories:
    headline = story.select_one('h4.title a').text.strip()
    
    url = story.select_one('h4.title a')['href']
    url = 'https://buckeyereporter.com' + url
    
    subsection = story.select_one('p.news-preview__label').text.strip()
    
    subsection_url = story.select_one('p.news-preview__label a')['href']
    subsection_url = 'https://buckeyereporter.com' + subsection_url
    
    article = {
        'section': section_title,
        'headline': headline,
        'url': url,
        'subsection': subsection,
        'subsection_url': subsection_url,
        'author': '',
        'author_url': '',
        'article_status': '',
        'preview_text': ''
    }

    articles.append(article)


# # Get LATEST NEWS

# In[11]:


latest_news = doc.select_one('section .main__part')

section_title = latest_news.select_one('.section-title').text.strip()

latest_news_stories = latest_news.select('.card-body')

for story in latest_news_stories:
    subsection = story.select_one('.news-preview__label').text.strip()
    
    headline = story.select_one('.card-title a').text.strip()
    
    url = story.select_one('.card-title a')['href']
    url = 'https://buckeyereporter.com' + url
    
    preview_text = story.select_one('.card-text').text.strip()
    
    article = {
        'section': section_title,
        'headline': headline,
        'url': url,
        'subsection': subsection,
        'subsection_url': '',
        'author': '',
        'author_url': '',
        'article_status': '',
        'preview_text': preview_text
    }

    articles.append(article)


# # Get 'NEWS' sections

# In[12]:


news_sections = doc.select('div.home-tag-news')
section_title = 'News'

for news_section in news_sections:
    subsection = news_section.select_one('h4').text.strip()
    
    stories = news_section.select('.news-preview li a')
    for story in stories:
        headline = story.text.strip()
        
        url = 'https://buckeyereporter.com' + story['href']
        
        article = {
            'section': section_title,
            'headline': headline,
            'url': url,
            'subsection': subsection,
            'subsection_url': '',
            'author': '',
            'author_url': '',
            'article_status': '',
            'preview_text': ''
        }

        articles.append(article)


# In[13]:


df = pd.DataFrame(articles)


# In[14]:


df.to_csv('scraped_articles.csv', index=False)


# In[ ]:




