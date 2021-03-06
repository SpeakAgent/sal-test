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

def add_scramble(driver, text="This is sentence one. This is sentence 2."):
    scram_btn = driver.find_element_by_id("scrambledLabel")
    scram_btn.click()
    next_btn = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/span")
    next_btn.click()
    ttl = driver.find_element_by_name("li_title")
    ttl.send_keys("Selenium Scramble test")
    txt = driver.find_element_by_id("text")
    txt.send_keys(text)
    save_btn = driver.find_element_by_id("scramSave")
    save_btn.click()

def add_vocab_lab(driver):
    vlbtn = driver.find_element_by_id("vocabLabLabel")
    vlbtn.click()
    next_btn = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/span")
    next_btn.click()
    pause(3)
    vls = driver.find_elements_by_name("vocab")
    vls[0].click()
    save_btn = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/form/div[41]/button")
    save_btn.click()

def add_tall_tales(driver):
    ttbtn = driver.find_element_by_id("tallTalesLabel")
    ttbtn.click()
    next_btn = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/span")
    next_btn.click()
    pause(2)
    tales = driver.find_elements_by_name("tales")
    tales[0].click()
    # save_btn = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/form/div[73]/button")
    # save_btn.click()

def add_text_activity(driver):
    txtbtn = driver.find_element_by_id("textLabel")
    txtbtn.click()
    next_btn = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/span")
    next_btn.click()
    pause(2)
    ttl = driver.find_element_by_id("li_title")
    ttl.send_keys("Selenium text activity")
    bdy = driver.find_element_by_name("text")
    bdy.send_keys("This is some sample text. Generated by Selenium automated test suite.")
    sbmt = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/form/div[3]/button")
    sbmt.click()

def add_video(driver, url="https://www.youtube.com/watch?v=z_yeSidJNcE"):
    videobtn = driver.find_element_by_id("videoLabel")
    videobtn.click()
    pause(2)
    next_btn = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/span")
    next_btn.click()
    vurl = driver.find_element_by_id("video_url")
    vurl.send_keys(url)
    ttl = driver.find_element_by_id("video_title")
    ttl.send_keys("Selium video")
    sbmt = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/form/div[3]/button")
    sbmt.click()

def add_activities(driver):
    btn = driver.find_element_by_link_text("ADD ACTIVITIES")
    btn.click()
    add_scramble(driver)
    pause(3)
    # add_tall_tales()
    # pause(3)

    btn = driver.find_element_by_link_text("ADD ACTIVITIES")
    btn.click()
    add_vocab_lab(driver)
    pause(3)

    btn = driver.find_element_by_link_text("ADD ACTIVITIES")
    btn.click()
    add_video(driver)
    pause(3)

    btn = driver.find_element_by_link_text("ADD ACTIVITIES")
    btn.click()
    add_text_activity(driver)
    pause(3)

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
    pause(5)
    add_activities(driver)

    return driver

if __name__ == "__main__":
    args = getopts(sys.argv)
    if '--pk' in args:
        driver = main(args['--pk'])
    else:
        driver = main()





