from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import requests
import random
import json

driver = webdriver.Chrome(r'C:\Users\swech\Downloads\chromedriver_win32\chromedriver')

# Get links of inspirational speeches
driver.get("https://www.youtube.com/results?search_query=inspirational+speeches")
links_inspirational = driver.find_elements_by_xpath('//*[@id="video-title"]')
links = set()
for i in links_inspirational:
    links.add(i.get_attribute('href'))

# Get links of motivational speeches
driver.get("https://www.youtube.com/results?search_query=motivational+speeches")
links_motivational = driver.find_elements_by_xpath('//*[@id="video-title"]')
for i in links_motivational:
    links.add(i.get_attribute('href'))
links = list(links)

# Get motivational quotes
quotes = requests.get("https://type.fit/api/quotes")
quotes = quotes.text
quotes = json.loads(quotes)

driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600)
target = '"Swetha"'

random_quotes_int = random.randint(0,len(quotes)-1)
string = links[random.randint(0,len(links)-1)] + "\n" + quotes[random_quotes_int]['text'] + " - " + quotes[random_quotes_int]['author']

x_arg = '//span[contains(@title,' + target + ')]'
user_name = wait.until(EC.presence_of_element_located((
    By.XPATH, x_arg)))
user_name.click()

inp_xpath = ' //span[contains(@title, ' + target +')]'
input_box = wait.until(EC.presence_of_element_located((
    By.XPATH, inp_xpath)))
input_box.click()

# Inspect and find the class name of text box
text_box = driver.find_element_by_class_name('DuUXI')
text_box.send_keys(string + Keys.ENTER)