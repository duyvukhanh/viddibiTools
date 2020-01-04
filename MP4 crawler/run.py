import crawlers
from fuzzywuzzy import fuzz
import pandas as pd
import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import ssl
import json
import ast
import json
import os
from urllib.request import Request, urlopen
import pprint
import time
import random

api_keys = [
        "AIzaSyCNgO1S-8Nn9DwdiPHD4paPoEniEyFwKDo",
        "AIzaSyAQwTQ6CgXd7Z9ZmVxKgqvnMkU1Tke35PE",
        "AIzaSyCOfUJQgDnsdb0eyKRgfoytiZo2N8FeImE",    
        "AIzaSyBIUSkpCVXwZBvnUxW26liHByz_zxE1ZGI",
        "AIzaSyAJDALvmlWunsTFJ-so8yA7QhPq4yoRTqI",
        "AIzaSyB0umgMQvC7N9p9RWCUMtvYNU43kClPtuQ",
        "AIzaSyChLu97wnI5EC9nJhlb4ek0JsotGiAyL8k",
        "AIzaSyB0k4SJFiuIOVAqvSWTB1bfTR1CEf87HWE",
        "AIzaSyDeVkwchNTeb7vnfDPuPUOO6EVuYyoch2E",
        "AIzaSyDoo6tXrlc18etLR5ZwR9newycGYJ-jzMI",
        "AIzaSyA7ajixHMEYXjshnyzIQEC-UzFn_Yl7Pls",
        "AIzaSyAFd-CcbJoVeRxY8w_5CUa4BHe02jXyrPo",
        "AIzaSyB4pCbJqpWKqDrkpBbFUFfjkU39f0xp2Zs",
        "AIzaSyCiUka3fyu56q1ThMfJVloE28lks8JraMM",
        "AIzaSyCMtcatlOHmN2DmO5P03GScZ2dxoHQr2wA",
        "AIzaSyDMtheyCNG0Od7CybnLYd9Yu421ZOXAc9I",
        "AIzaSyCBS776qj8yT6TG0-KRStRpmEdr2gl8S9E",
        "AIzaSyDgbujeXULAoEhZcK266RD99FqDdN2ywJc",
        "AIzaSyC0fsR_JiTOftnMHtUxDW-hnEDFJ-onWx0",
        "AIzaSyDVCWfa_m9bGzUOo8tKOuIKPdMrvdPf5Wc",
        "AIzaSyD4iXdRApe9dFwpC1tcx-sEFBqwR4DRXjo",
        "AIzaSyBr4rGGiuAty6TSUqU6lJy6M0MNS7hTQkE",
        "AIzaSyCn8nLDCPmf8kbVRXclwJiJoV64AaxeJkw",
        "AIzaSyBDKJeHopQmnigzEBOEc4IKHwMRG7ZwuEk",
]
# bot = crawlers.Basic_crawler(api_key)


# pprint.pprint(a)

# Import
data = pd.read_excel (r'test.xlsx',sheet_name='Sheet3')
df = pd.DataFrame(data, columns= ['Concat','TrackTitle','ArtistName'])

# df_name = pd.DataFrame(data, columns= ['d2'])
 
keyword = df.values.tolist()



# song_title = df_name.values.tolist()
def add_link(inputlink):
        result = bot.search_by_keyword(inputlink[0])
        if 'items' in result:
                list_ = result['items']
                
                for link in list_:
                        videoID = link['id']['videoId']
                        des = link['snippet']['description']
                        title = link['snippet']['title']
                        artist = link['snippet']['channelTitle']
                        des_lowcase = des.lower()
                        if (CheckTitle(title) and int(fuzz.ratio(str(inputlink[1]).lower(),str(title).lower())) > 30)\
                        or (des_lowcase.startswith('music video') and int(fuzz.ratio(str(inputlink[1]).lower(),str(title).lower())) > 30):
                                return [inputlink[0],"https://www.youtube.com/watch?v="+videoID,des,title,inputlink[1],inputlink[2],artist]
        return ['','','','',inputlink[1],inputlink[2],'']

def CheckTitle(Title):
        if "audio" in Title.lower():
                return False
        listKeywords = ["official video","video official","video","official music video","oficial video","video oficial","oficial music video"]
        for keyword in listKeywords:
                if keyword in Title.lower():
                        return True
        return False


index = 0
count = 0
i=0
row_list = {
        'Topic':[],
        'Mp3 link':[],
        'Des':[],
        'Title':[],
        'Title in sheet':[],
        'Artist':[],
        'Artist in sheet':[],

}
while True:
        # if index == len(keyword) :
        index += 1
        if index == len(keyword) :
                break 
        bot = crawlers.Basic_crawler(api_keys[i])
        array = add_link(keyword[index-1])
        topic = array[0]
        Mp3link = array[1]
        Des = array[2]
        Title = array[3]
        Titleinsheet = array[4]
        Artist = array[5]
        Artistinsheet = array[6]

        
        

        row_list['Topic'].append(topic)
        row_list['Mp3 link'].append(Mp3link)
        row_list['Des'].append(Des)
        row_list['Title'].append(Title)
        row_list['Title in sheet'].append(Titleinsheet)
        row_list['Artist'].append(Artist)
        row_list['Artist in sheet'].append(Artistinsheet)



        if count == 90:
                i += 1
                count = 0
        # if index == len(keyword) -1 :
        count += 1
        # print(index,'/',len(keyword),"           ",api_keys[i])
        print(index,'/',len(keyword),"         ",api_keys[i])
        time.sleep(random.randint(2,5))
        

print("EXPORTING")





df1 = pd.DataFrame(row_list, columns=['Topic', 'Mp3 link', 'Description', 'Title','Title in sheet','Artist','Artist in sheet'])

export_excel = df1.to_excel (r'test_result.xlsx', index = None, header=True) #Don't forget to add '.xlsx' at the end of the path


# def add_des(inputlink):
#         result = bot.search_by_keyword(inputlink)
#         list_ = result['items']
#         for link in list_:
#                 des = link['snippet']['description']
#                 if des.startswith('Provided to YouTube'):
#                         return des

# def add_title(inputlink):
#         result = bot.search_by_keyword(inputlink)
#         list_ = result['items']
#         for link in list_:
#                 title = link['snippet']['title']
#                 des = link['snippet']['description']
#                 if des.startswith('Provided to YouTube'):
#                         return title
                        



# df.to_csv('result.csv')
print("-------------DONE-------------")
# for link in list_:
#     videoID = link['id']['videoId']
#     des = link['snippet']['description']
#     title = link['snippet']['title']
#     if des.startswith('Provided to YouTube'):
#         print(videoID)
#         print(des)
#         print(title)

#         break