# Use Selenium web-diver and Chrome to count how many times "price target raised to $" occurred on https://thefly.com/
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from datetime import datetime, timedelta
import time
import re
from collections import Counter
from tabulate import tabulate

def scroll(timeout):
    print("Keep scrolling for the next " ,timeout , " seconds OR end_of_stories reached")
    stop = datetime.now() + timedelta(seconds=timeout)
    html = driver.find_element_by_tag_name('html')
    while( datetime.now() < stop and end_of_stories()==False):
        print("Clicking 'PAGE_END' and sleeping for three seconds ")
        html.send_keys(Keys.END)
        time.sleep(3)

def end_of_stories():
    try:
        driver.find_element_by_partial_link_text("No more news for the last year")
    except NoSuchElementException:
        return False
    print("No more news for the last year. STOPPING NOW!")
    return True

def counter(elements, min_limit):
    for index, item in enumerate(elements):
        elements[index] = item.text
    counter_list = []
    pattern = r' price target raised to .*'
    for x in elements:
        y = re.sub(pattern, '', x, 1)
        counter_list.append(y)
    counter_list = Counter(counter_list)
    for key, count in list(counter_list.items()):   
        if count < min_limit:
            del counter_list[key]
    
    # print in new line (See 'tabulate_example1.py' for more options)
    for key, value in counter_list.items():
        print(key, " : ", value)


# Read user input
symbol = input("Enter your stock symbol(Press ENTER to navigate to HomePage): ")
if symbol == "":
    url = "https://thefly.com/news.php?"
else:
    url = "https://thefly.com/news.php?symbol="+symbol

time_out = int(input("Enter how long (in seconds) you would like to scroll the web page: "))
#min_limit = int(input("Enter your minimum threshold to display an item: "))
min_limit = 4

# Setting "options" to suppress the DevTools debugging messages in the command prompt
options = Options()
options.add_argument('--no-sandbox') # Bypass OS security model
options.add_argument('--disable-gpu')  # applicable to windows os only
options.add_argument('disable-infobars')
options.add_argument("--disable-extensions")
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.get(url)

#Scroll the web page and retreive the elements with desired text
scroll(time_out)
elements = driver.find_elements_by_partial_link_text("price target raised to")
us_elements = driver.find_elements_by_partial_link_text("price target raised to $")

# Display the results in the command prompt
if symbol != "":
    print(symbol + " price target raised " + str(len(elements)) + " times ")
else:
    counter(us_elements, min_limit)   

driver.close()
driver.quit()