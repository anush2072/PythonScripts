# Use Selenium web-diver and Chrome to count how many times "price target raised to $" occurred
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from datetime import datetime, timedelta
import time
import re
from collections import Counter

def scroll(driver, timeout):
    scroll_pause_time = timeout

    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(scroll_pause_time)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            # If heights are the same it will exit the function
            break
        last_height = new_height

def scroll2(timeout):
    print("Keep scrolling for the next " ,timeout , " seconds OR end_of_stories reached")
    stop = datetime.now() + timedelta(seconds=timeout)
    html = driver.find_element_by_tag_name('html')

    while( datetime.now() < stop and end_of_stories()==False):
        print("Clicking 'PAGE_END' and sleeping for two seconds ")
        html.send_keys(Keys.END)
        time.sleep(2)

def end_of_stories():
    try:
        driver.find_element_by_partial_link_text("No more news for the last year")
    except NoSuchElementException:
        return False
    print("No more news for the last year. STOPPING NOW!")
    return True

def counter(elements):
    for index, item in enumerate(elements):
        elements[index] = item.text
    #print(elements)
    counter_list = []
    pattern = r' price target raised to .*'
    for x in elements:
        y = re.sub(pattern, '', x, 1)
        counter_list.append(y)
    print(Counter(counter_list))




symbol = input("Enter your stock symbol(Press ENTER to navigate to HomePage): ")
if symbol == "":
    url = "https://thefly.com/news.php?"
else:
    url = "https://thefly.com/news.php?symbol="+symbol

# Setting "options" to suppress the DevTools debugging messages in the command prompt
options = Options()
options.add_argument('--no-sandbox') # Bypass OS security model
options.add_argument('--disable-gpu')  # applicable to windows os only
options.add_argument('disable-infobars')
options.add_argument("--disable-extensions")
options.add_experimental_option('excludeSwitches', ['enable-logging'])

#driver = webdriver.Chrome(chrome_options=options, executable_path=r'F:\tmp\chromedriver.exe')
driver = webdriver.Chrome(options=options)
driver.get(url)

#scroll(driver, 5) # THIS IS where I want to SCROLL FOR MAY BE 30 seconds
scroll2(20)

elements = driver.find_elements_by_partial_link_text("price target raised to")

# displaying the result in the command prompt
if symbol != "":
    print(symbol + " price target raised " + str(len(elements)) + " times ")
else:
     counter(elements)   

driver.close()
driver.quit()