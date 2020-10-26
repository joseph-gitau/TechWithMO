from selenium import webdriver
from selenium.webdriver.common.keys import Keys
PATH = "C:\Program Files (x86)\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://rwlyaxcdsobuk3nudnlmtg-on.drv.tw/Mini_project4/www.voicebasedemail.com/")
print(driver.title)

driver.implicitly_wait(10)
search = driver.find_element_by_id("start-record-btn")
search.send_keys(Keys.ARROW_DOWN)
driver.sleep(5)
print("x")
search = driver.find_element_by_id("pause-record-btn")
search.send_keys(Keys.ARROW_DOWN)
print("x")
search = driver.find_element_by_id("email-id-btn")
search.send_keys(Keys.ARROW_DOWN)

