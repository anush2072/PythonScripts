# Use Sellenium web-diver and Chrome to download quaterly statements report from MorningStar
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://financials.morningstar.com/income-statement/is.html?t=prpl")

drop_down = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[3]/div[1]/div[2]/div[1]/li')
drop_down.click()
options = drop_down.find_elements_by_tag_name('li')
options[-1].click()
driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[3]/div[1]/div[2]/div[21]/span/a').click()