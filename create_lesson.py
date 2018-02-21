# Create a lesson from a wordlist. 
from datetime import datetime
import os, sys
from time import sleep

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

from utilities import pause, getopts, teacher_login

def create_lesson_from_wl(driver):
    ''' Creates a lesson from the 'create lesson' button on a wordlist.
        Assumes that the wordlist the 'create lesson' button is active.
    '''
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
    teacher_login(driver)
    pause(5)
    driver.get(base_url+wl_path)
    pause(5)
    create_lesson_from_wl(driver)

    return driver

if __name__ == "__main__":
    args = getopts(sys.argv)
    if '--pk' in args:
        main(args['--pk'])
    else:
        main()





