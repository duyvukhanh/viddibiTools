
# coding: utf-8
import requests
import pprint
# In[13]:


class Basic_crawler(object):
    import requests
    import json
    print(type(requests))
    def __init__(self, api):
        self.api = api
        
    ### create a function for future description
    def __repr__(self):
        return "The crawler description"
    
    def search_by_keyword(self, search_word, part = 'snippet', search_type = 'video', region = 'US',test = False, maxResults = 10):
        
        ### https request url
        
        https_request = 'https://www.googleapis.com/youtube/v3/search?part={0}&q={1}&type={2}&regionCode={3}&key={4}&maxResults={5}'        .format(part, search_word, search_type, region,self.api,maxResults)
        
        ### the response of the request
        metadata = requests.get(https_request).json()
        ### get text of request
        #text = response.text
        
        ### querry metadata
        #metadata = json.loads(text)
        
        ### return querry metadata if not test
        if test == True:
            return https_request
        else:
            return metadata
    
    def search_by_id(self, search_id, part = 'snippet', region = 'US', test = False):
        
        ### https request url
        
        https_request = 'https://www.googleapis.com/youtube/v3/videos?part={0}&id={1}&regionCode={2}&key={3}'        .format(part, search_id, region, self.api)
        
        ### the response of the request
        metadata = requests.get(https_request).json()
        
        ### get text of request
        #text = response.text
        
        ### querry metadata
       # metadata = json.loads(text)
        
        ### return querry metadata if not test
        if test == True:
            return https_request
        else:
            return metadata
    
    
    def get_channel_by_id(self, channel_id, part = 'snippet', test = False):
        ### https request url
        https_request = 'https://www.googleapis.com/youtube/v3/channels?part={0}&id={1}&key={2}'        .format(part, channel_id, self.api)
        
        ### get response metadata
        metadata = requests.get(https_request).json()
        
        if test == True:
            return https_request
        else:
            return metadata



# bot = Basic_crawler('AIzaSyD0aWiKawebxMLvV0wZLy9MZ7rCybm6P5M')
# result = bot.search_by_keyword('24k magic bruno mar')
# print(result)
# exit()

#%%
