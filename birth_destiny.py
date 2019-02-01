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

with open('birth_destiny.csv', 'w') as csv_file:
    csv_writer = csv.writer(csv_file)
    for birth_yun in range(2):
        for birth_time in range(12):
            for birth_day in range(31):
                for birth_month in range(12):
                    for birth_year in range(1900, 2033):
                        forms = {
                            'BYear': birth_year,
                            'BMonth': birth_month,
                            'BDay': birth_day,
                            'BTime': birth_time,
                            'BYun': birth_yun,
                            #'x': '20',
                            #'y': '13'
                        }

                        resp = requests.post(target, forms)
                    
                        soup = BeautifulSoup(resp.content, 'html.parser')
                   
                        # Remove br tags from content
                        for e in soup.find_all('br'):
                            e.extract()

                        contents = soup.find_all('td', {'class':'text2'})[1].contents
                        birth_destiny = ''.join(contents).strip()

                        row = [birth_year, birth_month, birth_day, birth_time, birth_yun, birth_destiny] 

                        time.sleep(3)          

                        csv_writer.writerow(row)

csv_file.close()
