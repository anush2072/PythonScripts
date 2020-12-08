# Use Selenium web-diver and Chrome to count how many times "price target raised to $" occurred.
from selenium import webdriver

symbol = input("Enter your stock symbol: ")
url = "https://thefly.com/news.php?symbol="+symbol
# Setting "options" to suppress the DevTools debugging messages in the command prompt
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.get(url)

elements = driver.find_elements_by_partial_link_text("price target raised to")

# displaying the result in the command prompt
print(symbol + " price target raised " + str(len(elements)) + " times ")

driver.close()
driver.quit()