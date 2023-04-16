from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
from selenium.webdriver.chromium import webdriver

options = webdriver.ChromeOptions()
options.binary_location = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
options.headless = True
driver_path = 'C:\\webdriver\\chromedriver.exe'
driver = Chrome(executable_path=driver_path, options=options)
driver.get('https://rrr.lt/paieska?man_id=97&cmc=747&cm=3009&mfi=97,747,3009;&prs=1&_=1681637648193&page=3')
soup = BeautifulSoup(driver.page_source, 'html.parser')
car_parts = soup.find_all('div', class_='products__items')
car_parts_list = []
for car_part in car_parts:
    # Car part price
    car_part_price_get = car_part.find('div', class_='products__price').find('strong')
    price = str(car_part_price_get).replace('<strong>', '').replace('strong', '').replace('€', '').replace('</>', '')

    # Taking everything from image part.
    car_part_image_get = (car_part.find('img', class_='lazy_hh lazy'))
    item_name = car_part_image_get.get('alt')
    src = car_part_image_get.get('src')

    # Car part location
    car_part_location = car_part.find('p', class_='products__scrapyard products__text_scrap_location').find(
        'span').text.strip()

    # Car model
    from_what_model_car_part = car_part.find('div', class_='products__text__description__main').find(
        'span').text.strip()

    car_parts_list.append({'item_name': item_name,
                           'item_price': float(price),
                           'image_location': src,
                           'location': car_part_location,
                           'car_model': from_what_model_car_part
                           })

print(car_parts_list)
