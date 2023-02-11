import time
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from selenium.webdriver.support.wait import WebDriverWait
from logg import vk_pass
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

options = chrome_options()
driver = webdriver.Chrome(executable_path='C:\Program Files\Google\chromedriver.exe', options=options)
url = 'https://vk.com/'
driver.get(url)
elem = driver.find_element(By.CLASS_NAME, "VkIdForm__input")
elem.send_keys('89513651398')
elem.send_keys(Keys.ENTER)
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.NAME, "password"))).click()
login = driver.find_element(By.NAME, "password")
print(login)
login.send_keys(vk_pass)
login.send_keys(Keys.ENTER)
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "l_aud"))).click()
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, "_audio_section_tab__all"))).click()
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, "audio_page_player_icon"))).click()

time.sleep(300)
