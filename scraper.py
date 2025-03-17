from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import random
import time
import os
from datetime import datetime

import dropbox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.keys import Keys



options = Options()
options.add_experimental_option("detach", True)


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=options)

driver.get("crossfit_login_url_here")

driver.maximize_window()

login_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "email")))
login_field.clear()
login_field.send_keys("your_email_here")

password_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "password")))
password_field.clear()
password_field.send_keys("your_password_here")

password_field.send_keys(Keys.RETURN)

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

workouts_link = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="93968"]/span')))
workouts_link.click()

current_year = int(time.strftime("%Y"))
current_month = int(time.strftime("%m"))

month_dropdown = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="monthFilter"]')))
select_month = Select(month_dropdown)
months = [option for option in select_month.options if option.get_attribute("value") and int(option.get_attribute("value")) <= current_month]
random_month = random.choice(months)
select_month.select_by_visible_text(random_month.text)

year_dropdown = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="yearFilter"]')))
select_year = Select(year_dropdown)
years = [option for option in select_year.options if option.get_attribute("value") and int(option.get_attribute("value")) <= current_year]
random_year = random.choice(years)
select_year.select_by_visible_text(random_year.text)

search_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="archiveFormSearch"]/div/div[4]/div/a')))
search_button.click()

time.sleep(5)

date_rows = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="archives"]//h3')))

random_date_row = random.choice(date_rows)

driver.execute_script("arguments[0].scrollIntoView();", random_date_row)

accept_cookies_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="pp-cookie-accept"]')))
accept_cookies_button.click()

# here we wait for a moment to let the accept cookies message disappear
time.sleep(2)

def take_screenshot(driver, filename):
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')  
    filename_with_timestamp = f'{filename}_{timestamp}.png'  
    driver.save_screenshot(filename_with_timestamp)
    return filename_with_timestamp

latest_screenshot_path = take_screenshot(driver, 'your_screenshot_path_here')


def upload_to_dropbox(file_path, target_path, access_token):
    dbx = dropbox.Dropbox(access_token)

    with open(file_path, "rb") as f:
        dbx.files_upload(f.read(), target_path)


upload_to_dropbox(
    file_path=latest_screenshot_path,
    target_path=f'/Workouts/{os.path.basename(latest_screenshot_path)}',
    access_token='YOUR_ACCESS_TOKEN'
)
