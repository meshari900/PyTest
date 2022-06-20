import requests
import pandas as pd
from bs4 import BeautifulSoup
import time
import datetime
url = "https://www.saudiexchange.sa/wps/portal/tadawul/markets/equities/market-watch?locale=ar"
data = requests.get(url).text
soup = BeautifulSoup(data, 'html.parser')
table = soup.find('table', class_='display')
name = []
Price = []
for row in table.tbody.find_all('tr'):    
    columns = row.find_all('td')
    name.append(columns[1].text.strip())
    Price.append(columns[2].text.strip())
list_of_tuple= list(zip(name, Price))
df = pd.DataFrame(list_of_tuple,columns=['أسم الشركة', 'السعر'])
pd.set_option("display.max_rows", None)
while True:
    now = datetime.datetime.now()
    filename = now.strftime("%H_%M_%S")
    df.to_excel("saudiexchange_{}.xlsx".format(filename),index=False)
    print(filename)
    time.sleep(900)
