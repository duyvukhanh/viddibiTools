from selenium import webdriver
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.chrome.options import Options 
import time
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException 
from selenium import webdriver
from selenium.common import exceptions
from fuzzywuzzy import fuzz


# Import
data = pd.read_excel (r'test.xlsx',sheet_name='Sheet3')
df = pd.DataFrame(data, columns= ['Concat','TrackTitle','ArtistName'])
keywords = df.values.tolist()


CHROMEDRIVER_PATH = r"/Users/duy/Desktop/vibbidi/chromedriver"
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(CHROMEDRIVER_PATH)

# options.add_extension('./extension_1_155_325_0.crx')
# driver = webdriver.Chrome(CHROMEDRIVER_PATH, chrome_options=options)
url = "https://www.youtube.com/"
driver.get(url)
driver.execute_script("document.body.style.zoom='33'")
# time.sleep(5)

def clearTitle(Title):
    returnedTitle = ""
    position = Title.find("(")
    if position != -1:
        if Title[position+1].lower() == "f" and Title[position+2].lower() == "e":
            for i in range(position):
                returnedTitle = returnedTitle + Title[i]
            return returnedTitle
    return Title

def searchLink(keyword):
    try:
        search_keyword = keyword[0].split(" ")
        url = "https://www.youtube.com/results?search_query="
        for word in search_keyword:
            url = url + "+" + word
        driver.get(url) 
        time.sleep(3)
        results = driver.find_elements_by_id("dismissable")
        print(len(results),end="     ")
        number_of_result = 0
        for result in results:
            title = result.find_element_by_id("video-title").text
            link = result.find_element_by_id("video-title").get_attribute('href')
            description = result.find_element_by_id("description-text").text
            channel_name = result.find_element_by_id("channel-name").find_element_by_tag_name("a").text
            # print(clearTitle((str(keyword[1])).lower()))
            # print(title.lower())
            if (( clearTitle(str(keyword[1])).lower() in title.lower()) and ("video" in title.lower())   and   (int(fuzz.ratio(channel_name.lower(),keyword[2].lower()))>40) and ("lyric" not in title.lower()))\
            or ( description.lower().startswith('music video') and (clearTitle(str(keyword[1])).lower() in title.lower())    and   (int(fuzz.ratio(channel_name.lower(),keyword[2].lower()))>40      ))\
            or ((clearTitle(str(keyword[1])).lower() in title.lower()) and ("official video" in title.lower()))\
            or ((clearTitle(str(keyword[1])).lower() in title.lower()) and ("official music video" in title.lower()))\
            or ((clearTitle(str(keyword[1])).lower() in title.lower()) and ("oficial video" in title.lower()))\
            or ((clearTitle(str(keyword[1])).lower() in title.lower()) and ("oficial video video" in title.lower())):                               
                return [keyword[0],link,description,str(keyword[1]),title,keyword[2],channel_name,1]
            number_of_result += 1
            if number_of_result == 5:
                break
        return [keyword[0],"","",str(keyword[1]),"",keyword[2],"",0]
    except:
        return [keyword[0],"","",str(keyword[1]),"",keyword[2],"",0]


index = 1
founded = 0
row_list = {
        'Topic':[],
        'Link':[],
        'Description':[],
        'Title':[],
        'TitleFound':[],
        'Artist':[],
        'ArtistFound':[],

}
for keyword in keywords:
    array = searchLink(keyword)
    Topic = array[0]
    Link = array[1]
    Description = array[2]
    Title = array[3]
    TitleFound = array[4]
    Artist = array[5]
    ArtistFound = array[6]

    row_list['Topic'].append(Topic)
    row_list['Link'].append(Link)
    row_list['Description'].append(Description)
    row_list['Title'].append(Title)
    row_list['TitleFound'].append(TitleFound)
    row_list['Artist'].append(Artist)
    row_list['ArtistFound'].append(ArtistFound)

    if array[7] == 1:
        x = "Added"
        founded += 1
    else: 
        x = "Not found"

    print(index,"/",len(keywords)," - ",x,"   ",founded," was found")
    index += 1

print("EXPORTING")
df1 = pd.DataFrame(row_list, columns=['Topic', 'Link', 'Description', 'Title','TitleFound','Artist','ArtistFound'])
export_excel = df1.to_excel (r'test_result.xlsx', index = None, header=True) #Don't forget to add '.xlsx' at the end of the path
print("-------------DONE-------------")

