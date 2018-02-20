# Create a lesson from a wordlist. 
from datetime import datetime
import os
from time import sleep

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

def pause(n, msg="(Loading)"):
    print "Sleeping for", n, "-", msg
    sleep(n)

def login(driver):
    print "Logging in"
    tlogin = driver.find_element_by_id("teacher-sign-in")
    tlogin.click()
    ufield = driver.find_element_by_id("login-email")
    pfield = driver.find_element_by_id("login-password")
    subbtn = driver.find_element_by_id("login-button")
    ufield.send_keys(os.environ.get('TUSER'))
    pfield.send_keys(os.environ.get('TPASS'))
    subbtn.click()

def create_lesson_from_wl(driver):
    btn = driver.find_element_by_xpath("/html/body/section/div/ui-view/div/div/div[2]/div[3]/button")
    btn.click()
    pause(5)
    title = driver.find_element_by_id("wl-new-title")
    title.clear()
    t = "Selenium test lesson from wl " + datetime.now().strftime("%Y-%m-%d %H:%M")
    title.send_keys(t)
    # Find by ID, not xpath
    btn = driver.find_element_by_id("save-lesson")
    btn.click()

def main(wlpk=2545):
    base_url = "http://127.0.0.1:5000/lingshare-dev/#"
    wl_path = "/author/wordlists/{}/edit/".format(wlpk)
    driver = webdriver.Firefox()
    driver.get(base_url)
    pause(5)
    login(driver)
    pause(5)
    driver.get(base_url+wl_path)
    pause(5)
    create_lesson_from_wl(driver)

    return driver

if __name__ == "__main__":
    main()





