from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import re
import getpass
import csv

FILENAME = input("Enter file to save data to: ")
POST_LINK = input("Enter post link: ")
USERNAME = input("Enter Username: ")

CHROME_DRIVER_PATH = '<ENTER PATH TO CHROMEDRIVER HERE>'

PASSWORD = getpass.getpass()

exp = r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+"

driver = webdriver.Chrome(CHROME_DRIVER_PATH)
driver.get('https://www.linkedin.com')
username = driver.find_element_by_id("session_key")
username.send_keys(USERNAME)
password = driver.find_element_by_id("session_password")
password.send_keys(PASSWORD)
signin_button = driver.find_element_by_class_name("sign-in-form__submit-button")
signin_button.click()
time.sleep(10)
driver.get(POST_LINK)

time.sleep(10)

comments_order_selector = driver.find_element_by_class_name("comments-sort-order-toggle__trigger")
comments_order_selector.click()
time.sleep(1)
comments_order = driver.find_elements_by_class_name("comments-sort-order-toggle-option")
comments_order[1].click()
time.sleep(1)

with open(FILENAME, 'w', newline='') as file:
    writer = csv.writer(file)
    START = 0
    while True:
        comments_array = driver.find_elements_by_class_name("comments-comment-item__main-content")
        comments_name = driver.find_elements_by_class_name("comments-post-meta__name")
        comments_profile_link = driver.find_elements_by_class_name("comments-post-meta__profile-link")
        END = len(comments_array)
        for i in range(START, END):
            email = re.findall(exp, comments_array[i].text)
            name = comments_name[i].find_element_by_class_name("hoverable-link-text").text
            link = comments_profile_link[i].get_attribute("href")
            writer.writerow([name, str(email).replace('[', '').replace(']', '').replace("'", ""), link])
        START = END
        try:
            load_more = driver.find_element_by_class_name("comments-comments-list__load-more-comments-button")
            load_more.click()
            time.sleep(1)
        except NoSuchElementException:
            break
        print(str(START) + " comments parsed!")
    file.close()