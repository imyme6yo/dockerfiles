import sys
import requests
from bs4 import BeautifulSoup

host = 'http://www.egosan.com'
target = host + '/src/data_z2.php'

forms = {
    'BYear': '1900',
    'BMonth': '0',
    'BDay': '0',
    'BTime': '0',
    'BYun': '0',
}


resp = requests.post(target, forms)

soup = BeautifulSoup(resp.content, 'html.parser')

print(soup.get_text())
#contents = soup.find_all('td', {'class':'text2'})[1].contents


contents = soup.find_all('td', {'class':'text2'})[1].contents

# BYear 1900-2032
# BMonth 0-11
# BDay 0-31
# BTime 0 - 11 
# BYun 0-1


# 0 (64, 7)
# 0 (52, 17)