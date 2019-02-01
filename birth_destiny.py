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

with open('birth_destiny.csv', 'w') as birth_destiny:
    destiny_writer = csv.writer(birth_destiny)
    
    for birth_year in range(1900, 2033):
        for birth_month in range(12):
            for birth_day in range(31):
                for birth_time in range(12):
                    for birth_yun in range(2):
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

                        destiny_id = 0
                        findFlag = False
                        try:
                            with open('birth_destiny_detail.csv', 'r') as birth_destiny_detail:
                                birth_destiny_detail_reader = csv.reader(birth_destiny_detail)
                                for row in birth_destiny_detail_reader:
                                    if row[1] == birth_destiny:
                                        destiny_id = int(row[0])
                                        findFlag = True
                                        break
                                    else:
                                        destiny_id = destiny_id + 1
                        except:
                            print("No File")
                            pass

                        if findFlag == False:
                            with open('birth_destiny_detail.csv', 'a') as birth_destiny_detail:
                                birth_destiny_detail_writer = csv.writer(birth_destiny_detail)

                                destiny_detail_row = [destiny_id, birth_destiny]

                                birth_destiny_detail_writer.writerow(destiny_detail_row)

                        destiny_row = [birth_year, birth_month, birth_day, birth_time, birth_yun, destiny_id] 
                        
                        print("destiny_row")
                        print(destiny_row)

                        destiny_writer.writerow(destiny_row)

                        time.sleep(3)          

