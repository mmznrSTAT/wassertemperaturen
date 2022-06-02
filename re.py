import requests
from bs4 import BeautifulSoup
import lxml
import pandas as pd
from datetime import datetime
import ch1903_wgs84 as geo

df = pd.read_csv('data/wassertemperaturen_all.csv')


converter = geo.GPSConverter()


df["wgs84_x"] = converter.LV03toWGS84(df["E"], df["N"], df["MITTLERE_HOEHE"])[1]

df["wgs84_y"] = converter.LV03toWGS84(df["E"], df["N"], df["MITTLERE_HOEHE"])[0]

df.head()

df.to_csv('data/wassertemperaturen_all.csv', mode='a', header=False)