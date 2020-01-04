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


url = "https://beta-www.vibbidi.net/album?id=5E4C920BB06D4805A184DF497EB02826"

# Import
data = pd.read_excel (r'test.xlsx',sheet_name='loa')
df = pd.DataFrame(data, columns= ['title','url'])
keywords = df.values.tolist()

CHROMEDRIVER_PATH = r"/Users/duy/Desktop/vibbidi/chromedriver"

driver = webdriver.Chrome(CHROMEDRIVER_PATH)



row_list = {
        'Title':[],
        'URL':[],
        'Check':[],
        # 'aaaa':[]
}
dem=0
for k in keywords:
    row_list['Title'].append(k[0])
    row_list['URL'].append(k[1])
    list_titles = []
    driver.get(k[1])
    # time.sleep(1)
    check = False
    hihi = ""
    d = driver.find_elements_by_class_name("TrackItemVersion__TrackInfo-ul89hd-6")
    for i in d:
        x = i.text
        list_titles.append(x)
    for titleee in list_titles:
        if titleee == k[0]:
            row_list['Check'].append('yes')
            check = True
            hihi = "yes"
            # row_list['aaaa'].append(titleee)
            break
        elif fuzz.ratio(str(titleee),str(k[0])) > 50:
            row_list['Check'].append('yes')
            check = True
            hihi = "yes"
            # row_list['aaaa'].append(titleee)
            break
    if check == False:
        row_list['Check'].append('no')
        hihi = "no"

    print(dem,"/",len(keywords),"------",hihi)
    dem += 1
    
   



print("EXPORTING")
df1 = pd.DataFrame(row_list, columns=['Title', 'URL', 'Check'])
export_excel = df1.to_excel (r'test_result.xlsx', index = None, header=True) #Don't forget to add '.xlsx' at the end of the path
print("-------------DONE-------------")


