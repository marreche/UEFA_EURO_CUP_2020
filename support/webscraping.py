import requests
import pandas as pd
from bs4 import BeautifulSoup as bs
import json


def sep_string(string):
    length = int(len(string) / 2)
    first = string[:length]
    second = string[length:]
    return [first, second]


def get_table(url):
    res = requests.get(url)
    html = bs(res.text,features="lxml")
    table = html.select("tr")
    headers_d = table[0].get_text()
    clean_headers = headers_d.split()
    clean_headers[5] = clean_headers[5].replace("Positions", "Preferred Positions")
    del clean_headers[4]
    clean_headers.insert(0, "Number")
    clean_headers[2] = clean_headers[2] + clean_headers[3]
    del clean_headers[3]
    fifa = pd.DataFrame()
    for i in range(len(table)):
        info = [e.get_text(strip=True) for e in table[i]]
        del info[2], info[2]
        info[2] = sep_string(info[2])
        pl = (dict(zip(clean_headers,info)))
        fifa = fifa.append(pl, ignore_index=True)
        i += 1
    fifa = fifa.drop([0])
    return fifa

Portugal = get_table("https://www.fifaindex.com/team/1354/portugal/fifa21_464/")
Portugal['Nationality'] = 'Portugal'
France = get_table("https://www.fifaindex.com/team/1335/france/fifa21_464/")
France['Nationality'] = 'France'
Finland = get_table("https://www.fifaindex.com/team/1334/finland/fifa21_464/")
Finland['Nationality'] = 'Finland'
England = get_table("https://www.fifaindex.com/team/1318/england/fifa21_464/")
England['Nationality'] = 'England'
Italy = get_table("https://www.fifaindex.com/team/1343/italy/fifa21_464/")
Italy['Nationality'] = 'Italy'
Denmark = get_table("https://www.fifaindex.com/team/1331/denmark/fifa21_464/")
Denmark['Nationality'] = 'Denmark'
Spain = get_table("https://www.fifaindex.com/team/1362/spain/fifa21_464/")
Spain['Nationality'] = 'Spain'
Belgium = get_table("https://www.fifaindex.com/team/1325/belgium/fifa21_464/")
Belgium['Nationality'] = 'Belgium'
Czech_Republic = get_table("https://www.fifaindex.com/team/1330/czech-republic/fifa21_464/")
Czech_Republic['Nationality'] = 'Czech Republic'
Switzerland = get_table("https://www.fifaindex.com/team/1364/switzerland/fifa21_464/")
Switzerland['Nationality'] = 'Switzerland'
Ukraine = get_table("https://www.fifaindex.com/team/1366/ukraine/fifa22_487/")
Ukraine['Nationality'] = 'Ukraine'
Austria = get_table("https://www.fifaindex.com/team/1322/austria/fifa21_464/")
Austria['Nationality'] = 'Austria'
Croatia = get_table("https://www.fifaindex.com/team/1328/croatia/fifa18wc_271/")
Croatia['Nationality'] = 'Croatia'
Germany = get_table("https://www.fifaindex.com/team/1337/germany/fifa21_464/")
Germany['Nationality'] = 'Germany'
Netherlands = get_table("https://www.fifaindex.com/team/105035/netherlands/fifa21_464/")
Netherlands['Nationality'] = 'Netherlands'
Sweden = get_table("https://www.fifaindex.com/team/1363/sweden/fifa21_464/")
Sweden['Nationality'] = 'Sweden'
Wales = get_table("https://www.fifaindex.com/team/1367/wales/fifa21_464/")
Wales['Nationality'] = 'Wales'
Hungary = get_table("https://www.fifaindex.com/team/1886/hungary/fifa21_464/")
Hungary['Nationality'] = 'Hungary'
Poland = get_table("https://www.fifaindex.com/team/1353/poland/fifa21_464/")
Poland['Nationality'] = 'Poland'
Russia = get_table("https://www.fifaindex.com/team/1357/russia/fifa21_464/")
Russia['Nationality'] = 'Russia'
Scotland = get_table("https://www.fifaindex.com/team/1367/wales/fifa21_464/")
Scotland['Nationality'] = 'Scotland'
Turkey = get_table("https://www.fifaindex.com/team/1365/turkey/fifa21_464/")
Turkey['Nationality'] = 'Turkey'


combine = France.append(Portugal)
combine = combine.append(Finland)
combine = combine.append(England)
combine = combine.append(Italy)
combine = combine.append(Denmark)
combine = combine.append(Spain)
combine = combine.append(Belgium)
combine = combine.append(Czech_Republic)
combine = combine.append(Switzerland)
combine = combine.append(Ukraine)
combine = combine.append(Austria)
combine = combine.append(Croatia)
combine = combine.append(Germany)
combine = combine.append(Netherlands)
combine = combine.append(Sweden)
combine = combine.append(Wales)
combine = combine.append(Hungary)
combine = combine.append(Poland)
combine = combine.append(Russia)
combine = combine.append(Scotland)
combine = combine.append(Turkey)
combine = combine.reset_index()
del combine["index"]
players = combine
players


data = players.to_json(orient='records')
parsed = json.loads(data)
with open("../data/team_players.json","w") as fp:
    res = json.dump(parsed,fp,indent=4,ensure_ascii=False)