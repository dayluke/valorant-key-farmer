import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.twitch.tv/directory/all/tags/c2542d6d-cd10-4532-919b-3d19f30a768b');
time.sleep(5)
first_twitch_stream = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/main/div[1]/div[3]/div/div/div/div[4]/div/div[1]/div[2]/div/div/div/div/article/div[1]/div/div/div[1]/div/a").click()
