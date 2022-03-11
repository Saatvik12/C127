from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
START_URL='https://exoplanets.nasa.gov/discovery/exoplanet-catalog/'
browser = webdriver.Chrome(executable_path=r'C:\Users\Ananda nilayam\Desktop\C127\chromedriver.exe')
time.sleep(10)
def scrap():
    headers=[ 'NAME', 'LIGHT-YEARS FROM EARTH','PLANET MASS', 'STELLAR MAGNITUDE','DISCOVERY DATE']
    planet_data=[]
    for i in range(0,198):
        soup=BeautifulSoup(browser.page_source, 'html.parser')
        for ul_tag in soup.find_all('ul',attrs={'class','exoplanet'}):
            litags=ul_tag.find_all('li')
            temp_list=[]
            for index,li_tags in enumerate(litags)
            if index==0:
                temp_list.append(li_tags.find_all('a')[0].contents[0])
            else:
                try:
                    temp_list.append(li_tags.contents[0])
                except:
                    temp_list.append('')
        planet_data.append(temp_list)
        browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
    with open('save.csv','w')as f:
        csvwriter=csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(planet_data)
scrap()