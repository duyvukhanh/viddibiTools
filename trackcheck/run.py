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

        # "AIzaSyCNgO1S-8Nn9DwdiPHD4paPoEniEyFwKDo",
        # "AIzaSyAQwTQ6CgXd7Z9ZmVxKgqvnMkU1Tke35PE",
        # "AIzaSyCOfUJQgDnsdb0eyKRgfoytiZo2N8FeImE",    
        # "AIzaSyBIUSkpCVXwZBvnUxW26liHByz_zxE1ZGI",
        # "AIzaSyAJDALvmlWunsTFJ-so8yA7QhPq4yoRTqI",
        # "AIzaSyB0umgMQvC7N9p9RWCUMtvYNU43kClPtuQ",
        # "AIzaSyChLu97wnI5EC9nJhlb4ek0JsotGiAyL8k",
        # "AIzaSyB0k4SJFiuIOVAqvSWTB1bfTR1CEf87HWE",
        # "AIzaSyDeVkwchNTeb7vnfDPuPUOO6EVuYyoch2E",
        # "AIzaSyDoo6tXrlc18etLR5ZwR9newycGYJ-jzMI",
        # "AIzaSyA7ajixHMEYXjshnyzIQEC-UzFn_Yl7Pls",
        # "AIzaSyAFd-CcbJoVeRxY8w_5CUa4BHe02jXyrPo",
        # "AIzaSyB4pCbJqpWKqDrkpBbFUFfjkU39f0xp2Zs",
        # "AIzaSyCiUka3fyu56q1ThMfJVloE28lks8JraMM",
        # "AIzaSyCMtcatlOHmN2DmO5P03GScZ2dxoHQr2wA",
        # "AIzaSyDMtheyCNG0Od7CybnLYd9Yu421ZOXAc9I",
        # "AIzaSyCBS776qj8yT6TG0-KRStRpmEdr2gl8S9E",
        # "AIzaSyDgbujeXULAoEhZcK266RD99FqDdN2ywJc",
        # "AIzaSyC0fsR_JiTOftnMHtUxDW-hnEDFJ-onWx0",
        # "AIzaSyDVCWfa_m9bGzUOo8tKOuIKPdMrvdPf5Wc",
        # "AIzaSyD4iXdRApe9dFwpC1tcx-sEFBqwR4DRXjo",
        # "AIzaSyBr4rGGiuAty6TSUqU6lJy6M0MNS7hTQkE",
        # "AIzaSyCn8nLDCPmf8kbVRXclwJiJoV64AaxeJkw",
        # "AIzaSyBDKJeHopQmnigzEBOEc4IKHwMRG7ZwuEk",


        "AIzaSyDXoANm2oXL5LIZyzaZHiaXa_l1zc29uEc",
        "AIzaSyC2iohMZmM01337qjzwzzCHYvjIVd43sEQ",
        "AIzaSyCTW_S0LSHPYDlkO777bdlzk0kukVwAcmg",
        "AIzaSyB1eN3Ko7K62WzYgCCzidUElY41yqANi7Y",
        "AIzaSyDRLvy-Ge4b__7JyxAh41AqhgIjDEiAZuk",
        "AIzaSyCSkaJee3CNhKPF5CTUd5OfL1-mklDWq20",
        "AIzaSyBCnM8mJajfKFf65UFoUP4Std00ujiJg1A",
        "AIzaSyCYodae9-Z9U2Q-Z1kNReXgmkqt1Zd4_R4",
        "AIzaSyAYI19M7NI0bba4n9cz3pdeTuDQeVHZtI4",
        "AIzaSyC3wKYTGTcJjSQAXdZk3ugmdLPiSNXbark",
        "AIzaSyDMabu-7Cvt3bVdfqFx6NcSNAZUYL8Nr_s",
        "AIzaSyD3ImB-QqcKBTv330-1uAP2P7D8tT0U1yU",
        "AIzaSyBQPI28ct7YUlcZ8iZzzbfNDFy6mCBjq2g",
        "AIzaSyAT1Pdlc7gb1XU-IyiNBQHREiJsx60NASI",
        "AIzaSyCoXZwQMRPfQC1Lcbds-dzsZBtXjQbnBBQ",
        "AIzaSyCMhQLMMPcmk3Mi3-W5Ta5Lv_0blad7KaE",
        "AIzaSyDi3mreCdiRawv76rjRo-clPjL11J_E7nY",
        "AIzaSyAApYqS-ZvGvFgBrIg5Q05moteEXoSP4Gs",
        "AIzaSyDDGHELz2rphYtrMU1jnnHrL5AvYIeKI10",
        "AIzaSyAkSEHQX6maMHT-s4KDvmjI9D1qh7d5AA0",
        "AIzaSyAf1Qdm5T9lVEuynzO0OcVYY0kbPoyKSfc",
        "AIzaSyD1nrtxJJv2_eYfsK2s53i226PU8uOFypI",
        "AIzaSyDaKBU_zUhBefvdgknzMimvV_3eF1ExqEQ",
        "AIzaSyBbfLs03vmYU1DL_FDjTE3WHf3-norfxpw",
]


# Import
data = pd.read_excel (r'test.xlsx',sheet_name='Sheet3')
df = pd.DataFrame(data, columns= ['Concat','TrackTitle','ArtistName'])
keyword = df.values.tolist()


def add_link(inputlink):
        result = bot.search_by_keyword(inputlink[0])
        print(result)
        exit()
        if 'items' in result:
                list_ = result['items']
                
                for link in list_:
                        videoID = link['id']['videoId']
                        des = link['snippet']['description']
                        title = link['snippet']['title']
                        artist = link['snippet']['channelTitle']
                        if des.startswith('Provided to YouTube') and int(fuzz.ratio(str(inputlink[1]).lower(),str(title).lower())) > 70:
                                return [inputlink[0],"https://www.youtube.com/watch?v="+videoID,des,title,inputlink[1],inputlink[2],artist]
        return ['','','','',inputlink[1],inputlink[2],'']



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
        print(index,'/',len(keyword),"         ",api_keys[i],"    ",array[0])
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
                        

# df['MP3 link'] = df['topic'].apply(lambda row: add_link(row))
# df['title'] = df['topic'].apply(lambda row: add_title(row))
# df['MP3 lMP3 link'] = df['topic'].apply(lambda row: add_link(row))


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