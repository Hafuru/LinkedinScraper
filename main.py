from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup


def login(browser):
    url = "https://www.linkedin.com/checkpoint/lg/sign-in-another-account"

    browser.get(url)

    email_field = browser.find_element(By.ID, "username")
    email_field.send_keys("civepe5699@idurse.com")
    time.sleep(3)
    password_field = browser.find_element(By.ID, "password")
    password_field.send_keys("hfqbq$Ei5aVXnZM7@h2$")
    time.sleep(4)
    login_button = browser.find_element(By.XPATH, "/html/body/div/main/div[3]/div[1]/form/div[3]/button")
    login_button.click()
    time.sleep(3)


def search_people(browser):
    search_field = browser.find_element(By.XPATH, "/html/body/div[7]/header/div/div/div/div[1]/input")
    search_value = "SAP people"
    search_field.send_keys(search_value)
    search_field.send_keys(Keys.RETURN)
    time.sleep(5)

    all_people_button = browser.find_element(By.XPATH,
                                             "/html/body/div[7]/div[3]/div[2]/div/div[1]/main/div/div/div[2]/div[2]/a")
    all_people_button.click()


def user_url(browser):
    page_source = BeautifulSoup(browser.page_source)
    profiles = page_source.findAll('a', class_="app-aware-link")


browser = webdriver.Firefox()
login(browser)
search_people(browser)
