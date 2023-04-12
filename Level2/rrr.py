from bs4 import BeautifulSoup
import requests


url = f'https://rrr.lt/naudotos-autodalys/audi/a3-s3-a3-sportback-8p-2005-2013/apsvietimo-sistema/galiniai-zibintai/galinio-zibinto-dangtelis-lizdas?man_id=3&cmc=4&cm=306'
source = requests.get(url)
soup = BeautifulSoup(source.content, 'html.parser')

print(soup)