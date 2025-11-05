import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd
 
url = requests.get(f'https://www.scrapethissite.com/pages/forms/').text
soup = BeautifulSoup(url, 'lxml')
#players = soup.find_all('tr')
#print(players)
players = soup.find_all('tr')[1:]
st.write(players[0])
team_name = []
years = []
wins = []
 
for i in players:
    name = i.find_all('td')[0].text.strip()
    year = i.find_all('td')[1].text.strip()
    win = i.find_all('td')[2].text.strip()
    team_name.append(name)
    years.append(year)
    wins.append(win)
 
    data = pd.DataFrame({'Team Name': team_name, 'Year': years, 'Wins': wins})
    st.dataframe(data)