# Goal: Create a wordlist, add some new words to it, make some updates.
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

def create_wl(driver):
    return_data = []

    wlnav = driver.find_element_by_id("n-wordlist")
    wlnav.click()

    pause(3)

    addwl = driver.find_element_by_id("add-wordlist")
    addwl.click()
    title = driver.find_element_by_id("wl-new-title")
    t = "Selenium test " + datetime.now().strftime("%Y-%m-%d %H:%M")
    return_data.append(("title", t))
    title.send_keys(t)
    lang = driver.find_element_by_xpath(
        "//select[@id='languagesDropdown']/option[text()='English (U.S.)']")
    lang.click()
    tags = driver.find_element_by_name("tags")
    tags.send_keys("selenium1, selenium2")

    grades = driver.find_element_by_name("gradesSelection")
    grades.click()
    pause(1)
    gr = grades.find_element_by_xpath("//ul/li/div[6]/span")
    return_data.append(("Grade", gr.text)) #Save the grade for later.
    gr.click()
    # Click to close the drop down
    driver.find_element_by_xpath("/html/body").click()

    subs = driver.find_element_by_name("subjectsSelection")
    subs.click()
    sub = driver.find_element_by_xpath(
        "//form/fieldset/div[3]/div[2]/div[1]/ul/li/div[3]/span")
    return_data.append(("Subject", sub.text))
    sub.click()
    # Close dropdown
    driver.find_element_by_xpath("/html/body").click() 

    driver.find_element_by_id("wl-save").click()

    pause(3, "Loading before returning")
    return return_data

def add_words(driver):
    data = []
    driver.find_element_by_partial_link_text("ADD WORDS").click()
    words = ['apple','blue', 'button', 'auto']
    for word in words:
        driver.find_element_by_name("new_target_word-0").send_keys(word)
        pause(2, "waiting for words")
        wd = driver.find_element_by_xpath("//form[2]/div/div[2]/a[1]/div")
        data.append(("Word", wd.text))
        wd.click()
        driver.find_element_by_name("new_target_word-0").clear()
    driver.find_element_by_xpath("//form[2]/div/div[3]/div[1]/input").click()
    return data

def check_data(driver, data):
    errors = 0
    for k, v in data:
        if k == "Word":
            try:
                driver.find_element_by_link_text(v.split(" - ")[0])
            except NoSuchElementException:
                print "Word not found:", v
                errors += 1

        if k == "Subject":
            # TODO: This needs to be more exact. Needs class or something.
            r = driver.find_elements_by_xpath(
                "//span[contains(text(), '{}')]".format(v))
            if not r:
                print "Subject not found:", v
                errors +=1

        if k == "Grade":
            # TODO: This needs to be more exact. Needs class or something.
            r = driver.find_elements_by_xpath(
                "//span[contains(text(), '{}')]".format(v))
            if not r:
                print "Grade not found:", v
                errors += 1

    print "Errors found:", errors

def main():
    base_url = "http://127.0.0.1:5000/lingshare-dev/#"
    driver = webdriver.Firefox()
    driver.get(base_url)
    pause(5, "Loading up page")

    login(driver)
    pause(5)
    data = create_wl(driver)
    pause(5)
    data.extend(add_words(driver))
    pause(5)
    check_data(driver, data)

    return driver, data

driver, data = main()