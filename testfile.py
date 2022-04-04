from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd

df = pd.DataFrame(columns=['Title','Company','Salary','Location','Job Description','Date of Posting','Rating'])
a=0
for param in range(0,50):
    url='https://in.indeed.com/jobs?q=data%20scientist&start='+str(a)
    a+=10
    driver = webdriver.Chrome("C:/Users/RAKSHITA/Downloads/chromedriver_win32 (1)/chromedriver.exe")
    driver.get(url)
    time.sleep(10)

    soup = BeautifulSoup(driver.page_source,'html5lib')

    driver.close()

    divs = soup.find_all('div',class_='job_seen_beacon')
    for item in divs:
        title = item.find('h2').text.strip()
        company = item.find('span', class_ = 'companyName').text.strip()  
        try:
            location = item.find('div', class_ = 'companyLocation').text.strip()
        except:
            location=''
        date = item.find('span', class_ = 'date').text.strip()
        try:
              salary = item.find('span',class_= 'salary-snippet').text.strip() 
        except:
              salary =''
        try:
            rating=item.find('span', class_ = 'ratingNumber').text.strip()
        except:
            rating=''
        try:
            JobDescription = item.find('div',{'class':'job-snippet'}).text.strip().replace('\n','')
        except:
            JobDescription=''

        df=df.append({'Title':title,'Company':company,'Salary':salary,'Location':location,'Job Description':JobDescription,'Date of Posting':date,'Rating':rating},ignore_index=True)
df.to_csv('Data_Science_Jobs_Indeed.csv')
