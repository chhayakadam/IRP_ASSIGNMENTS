#!/usr/bin/env python
# coding: utf-8

# In[11]:


text_file = open("C:/Users/Gateson/Downloads/c.txt")
text = text_file.read()
print(text)


# In[2]:


get_ipython().system('pip install nltk')


# In[12]:


#sentence Tokenization
import nltk
nltk.download('punkt')


# In[13]:


from nltk import sent_tokenize
sentence_tokenized = sent_tokenize(text)
print(sentence_tokenized)


# In[5]:


nltk.download('stopwords')


# In[14]:


from nltk import word_tokenize
text_tokenized = word_tokenize(text)
print(text_tokenized)


# In[15]:


#normalization
lower_text = text.lower()
print(lower_text)


# In[16]:


# import these modules
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
 
ps = PorterStemmer()
 
# choose some words to be stemmed
words = ["Innovation"
,"Critical Thinking"
,"Problem-Solving"
,"Technology Integration"]
 
for w in words:
    print(w, " : ", ps.stem(w))


# In[17]:


#remove stopwords
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
stopwords = stopwords.words('english')
print(stopwords)

text_nostop = "".join([char for char in text_tokenized if char not in stopwords])
print(text_nostop)
 


# In[ ]:




