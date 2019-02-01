import sys
import csv
import time
import requests
from bs4 import BeautifulSoup
from bs4 import Comment

host = 'http://www.egosan.com'
target = host + '/src/data_z2.php'

# Iteration for all Destiny
# BYear 1900-2032
# BMonth 0-11
# BDay 0-31
# BTime 0-11
# BYun 0-1

with open('zodiac_destiny.csv', 'w') as csv_file:
    csv_writer = csv.writer(csv_file)
    for birth_year in range(1, 13):
        for birth_day in range(1, 31):
            forms = {
                'BirthYear': birth_year,
                'BirthDay': birth_day,
                #'x': '20',
                #'y': '13'
            }

            resp = requests.post(target, forms)
                    
            soup = BeautifulSoup(resp.content, 'html.parser')
                   
            # Remove br tags from content
            for e in soup.find_all('br'):
                e.extract()
            contents = soup.find_all('td', {'class':'text2'})[1].contents
            zodiac_destiny = ''.join(contents).strip()

            row = [birth_year, birth_day, zodiac_destiny] 

            time.sleep(3)          

            csv_writer.writerow(row)

csv_file.close()
