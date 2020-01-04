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

lyric = "https://genius.com/Dozi-jodedor-de-chinatown-remix-lyrics"
# lyric = "https://www.google.com/search?q=lyric+Delux+To+Live+%26+Die+in+Tj&rlz=1C1CHBF_enVN873VN873&oq=lyric+Delux+To+Live+%26+Die+in+Tj&aqs=chrome..69i57j33.163j0j9&sourceid=chrome&ie=UTF-8"

add = "https://ops.vibbidi.com/singles/2F68D8C2893E46ABA8CBC0599BE1B96B"
# add = "https://ops.vibbidi.com/singles/CE7ACE429BDF467D8EB6A0954F4CAABF"


CHROMEDRIVER_PATH = r"/Users/duy/Desktop/vibbidi/chromedriver"
options = webdriver.ChromeOptions()
options.add_extension('./extension_4_0_1_0.crx')
driver = webdriver.Chrome(CHROMEDRIVER_PATH, chrome_options=options)



# driver.get(lyric)
# driver.find_element_by_xpath("/html/body/div[7]/div[3]/div[10]/div[1]/div[2]/div/div[2]/div[2]/div/div/div[1]/div/div[1]/div[1]/div/div").click()
# time.sleep(2)
# songLyric = driver.find_element_by_xpath('/html/body/div[7]/div[3]/div[10]/div[1]/div[2]/div/div[2]/div[2]/div/div/div[1]/div/div[1]/div[1]/span/div/div/div[2]/div/div/div/div[1]').text
# songLyric = songLyric.replace("DỊCH SANG TIẾNG VIỆT","")

# driver.get(add)
# driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div[2]/div/form/div/div[4]/div[2]/textarea").send_keys(songLyric)
# # driver.find_element_by_xpath("/html/body/div/div[2]/div/div/div/div[2]/div/form/div/div[6]/div/input").click()


def addLyricGoogle(googleLink,vibbidiLink):
    driver.get(googleLink)
    driver.find_element_by_xpath("/html/body/div[7]/div[3]/div[10]/div[1]/div[2]/div/div[2]/div[2]/div/div/div[1]/div/div[1]/div[1]/div/div").click()
    time.sleep(2)
    songLyric = driver.find_element_by_xpath('/html/body/div[7]/div[3]/div[10]/div[1]/div[2]/div/div[2]/div[2]/div/div/div[1]/div/div[1]/div[1]/span/div/div/div[2]/div/div/div/div[1]').text
    songLyric = songLyric.replace("DỊCH SANG TIẾNG VIỆT","")
    driver.get(vibbidiLink)
    driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div[2]/div/form/div/div[4]/div[2]/textarea").clear()
    driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div[2]/div/form/div/div[4]/div[2]/textarea").send_keys(songLyric)
    driver.find_element_by_xpath("/html/body/div/div[2]/div/div/div/div[2]/div/form/div/div[6]/div/input").click()
    time.sleep(1)



def addLyricGenius(geniusLink,vibbidiLink):
    driver.get(geniusLink)
    songLyric = driver.find_element_by_xpath("/html/body/routable-page/ng-outlet/song-page/div/div/div[2]/div[1]/div/defer-compile[1]/lyrics/div/div/section/p").text
    driver.get(vibbidiLink)
    driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div[2]/div/form/div/div[4]/div[2]/textarea").clear()
    driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div[2]/div/form/div/div[4]/div[2]/textarea").send_keys(songLyric)
    driver.find_element_by_xpath("/html/body/div/div[2]/div/div/div/div[2]/div/form/div/div[6]/div/input").click()
    time.sleep(1)




# Import
data = pd.read_excel (r'input.xlsx',sheet_name='input')
df = pd.DataFrame(data, columns= ['lyric','add'])
keywords = df.values.tolist()


dem = 0
for k in keywords:
    if "genius" in k[0]:
        addLyricGenius(k[0],k[1])
    elif "google" in k[0]:
        addLyricGoogle(k[0],k[1])
    dem += 1
    print(dem,'/',len(keywords))

print("---DONE---")