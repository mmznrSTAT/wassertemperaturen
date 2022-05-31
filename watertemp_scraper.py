import requests
from bs4 import BeautifulSoup
import lxml
import pandas as pd
from datetime import datetime

url = "https://hw.zh.ch/hochwasser/mac/AktWassertemp.HTML"

# Mit request Webseite aufrufen
r = requests.get(url)

# wir machen eine Suppe aus der Antwort
soup = BeautifulSoup(r.content, 'lxml')

dct_lst = []

for el in soup.find_all('tr')[1:-1]:

    mydict = {}

    this_row = el.find_all('td')
    
    now = datetime.now()
    filename = now.strftime("%Y%m%d-%Hh%M")

    mydict['DatumScraping'] = now.strftime("%Y%m%d-%Hh%M")
    mydict['gewaesser'] =  this_row[0].text.replace("''","").strip()
    mydict['Messeinheit'] = this_row[1].text.replace("''","").strip()
    mydict['Datum']=        this_row[2].text.replace("''","").strip()
    mydict['Aktueller_Wert'] = this_row[3].text.replace("''","").strip()
    mydict['24h_vorher'] =  this_row[4].text.replace("''","").strip()
    mydict['Differenz'] =  this_row[5].text.replace("''","").strip()
    mydict['Mittel_24h'] =  this_row[6].text.replace("''","").strip()
    mydict['Maximum_24h'] = this_row[7].text.replace("''","").strip()
    mydict['Minimum_24h'] = this_row[8].text.replace("''","").strip()
    dct_lst.append(mydict)


df = pd.DataFrame(dct_lst)   
stations = pd.read_csv('data/matching_tab.csv')

df = pd.merge(df,stations, on='gewaesser', how='left')

df.to_csv('data/wassertemperaturen_all.csv', mode='a', header=False)

