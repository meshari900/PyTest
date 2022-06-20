import requests
import pandas as pd
from bs4 import BeautifulSoup
import time
import datetime

while True:
    url = "https://www.saudiexchange.sa/wps/portal/tadawul/markets/equities/market-watch?locale=ar"
    data = requests.get(url).text
    soup = BeautifulSoup(data, 'html.parser')
    table = soup.find('table', class_='display')
    name = []
    Price = []
    vol = []
    chv = []
    chp = []
    nootc = []
    vtc = []
    bp = []
    bv = []
    bop = []
    bov = []
    for row in table.tbody.find_all('tr'):
        columns = row.find_all('td')
        name.append(columns[1].text.strip())
        Price.append(columns[2].text.strip())
        vol.append(columns[3].text.strip())
        chv.append(columns[4].text.strip())
        chp.append(columns[5].text.strip())
        nootc.append(columns[6].text.strip())
        vtc.append(columns[7].text.strip())
        bp.append(columns[8].text.strip())
        bv.append(columns[9].text.strip())
        bop.append(columns[10].text.strip())
        bov.append(columns[11].text.strip())
    list_of_tuple = list(zip(name, Price, vol, chv, chp, nootc, vtc, bp, bv, bop, bov))
    df = pd.DataFrame(list_of_tuple,
                      columns=['أسم الشركة', 'السعر', 'آخر كمية', 'تغيير القيمة', 'التغير', 'تراكمي عدد الصفقات',
                               'تراكمي الكمية', 'أفضل طلب سعر', 'أفضل طلب كمية', 'أفضل عرض سعر', 'أفضل عرض كمية'])
    pd.set_option("display.max_rows", None)
    now = datetime.datetime.now()
    filename = now.strftime("%H_%M_%S")
    df.to_excel("saudiexchange_{}.xlsx".format(filename),index=False)
    print(filename)
    time.sleep(900)



