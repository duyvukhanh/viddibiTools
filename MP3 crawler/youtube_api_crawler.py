
# coding: utf-8

# In[1]:


import os
import google.oauth2.credentials


# In[2]:


from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow


# In[3]:


import pprint
import requests
import numpy as np
import pandas as pd


# In[4]:


# The CLIENT_SECRETS_FILE variable specifies the name of a file that contains
# the OAuth 2.0 information for this application, including its client_id and
# client_secret.
CLIENT_SECRETS_FILE = "client_secret.json"


# In[5]:


### SOME IMPORTANT REQUIRED ATTRIBUTES FOR CRAWLERS
api_key = 'AIzaSyD0aWiKawebxMLvV0wZLy9MZ7rCybm6P5M'
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'


# In[6]:


class Crawler_api_version(object):
    def __init__(self, api_key, api_service_name, api_version):
        self.api_key = api_key
        self.api_service_name = api_service_name
        self.api_version = api_version
      # Apply build method from googleapiclient.discovery
      # to build an youtube object
        self.youtube = build(self.api_service_name, self.api_version, developerKey = self.api_key)
    def __repr__(self):
        return ('Crawler build base on Youtube_API')
    
    # Prettry print response
    
    def print_response(self, response):
        return pprint.pprint(response)
    
    # Build a function to handle empty response list

    def none_results(self, response):
        if response['items'] == []:
            return np.nan
        else:
            response = response
            return response
    
    ### This part contains all the method to get information from api
    
    # Search by keyword
    def search_list_by_keyword(self, type = 'video',regionCode = 'US', test = False, **kwargs):

        response = self.youtube.search().list(
        **kwargs
        ).execute()
        if test == True:
            self.print_response(response)
            return self.none_results(response)
        else:
            return self.none_results(response)
        
    def search_list_by_keyword_http_request(self, search_word, part = 'snippet', search_type = 'video', region = 'US',test = False):
        
        ### https request url
        
        https_request = 'https://www.googleapis.com/youtube/v3/search?part={0}&q={1}&type={2}&regionCode={3}&key={4}'        .format(part, search_word, search_type, region,self.api_key)
        
        ### the response of the request
        response = requests.get(https_request).json()
        ### get text of request
        #text = response.text
        
        ### querry metadata
        #metadata = json.loads(text)
        
        ### return querry metadata if not test
        if test == True:
            self.print_response(response)
            return self.none_results(response)
        else:
            return self.none_results(response)

    def search_list_by_id(self, video_id, test = False, **kwargs):
        
        response = self.youtube.videos().list(id = video_id, **kwargs).execute()      
        if test == True:
            self.print_response(response)
            return self.none_results(response)
        else:
            return self.none_results(response)

    def search_list_by_channel(self, channelId, test = False, **kwargs):
        
        response = self.youtube.channels().list(id = channelId, **kwargs).execute()
        if test == True:
            self.print_response(response)
            return self.none_results(response)
        else:
            return self.none_results(response)
        
        
    


# In[7]:


#crawler = Crawler_api_version(api_key, API_SERVICE_NAME, API_VERSION)


# In[8]:


#crawler.search_list_by_id('hT_nvWreIhg',part = 'snippet', test = True)


# In[9]:


#search_list_by_id(youtube, 'hT_nvWreIhg',part = 'snippet', test = True)


# In[10]:


crawler_api = Crawler_api_version(api_key, API_SERVICE_NAME, API_VERSION)


# In[13]:


#(crawler_api.search_list_by_id(video_id='zaIsVnmwdqg', regionCode = 'US', part = 'snippet,statistics'))

