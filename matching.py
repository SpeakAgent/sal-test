# Goal: Test a game of Matching (Memory). Right now, this uses the
# Teacher preview view.

from datetime import datetime
import os
from time import sleep

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

def pause(n, msg):
    print "Pausing for", n, " - ", msg
    sleep(n)

def play_game(driver):
    cards = driver.find_elements_by_class_name('back')
    num = len(cards)
    while len(cards) != 0:
        for i in range(1, len(cards)):
            print i
            cards[0].click()
            pause(2, 'flip')
            cards[i].click()
            pause(2, 'flip')
            cards = driver.find_elements_by_class_name('back')
            if len(cards) != num:
                num = len(cards)
                break

def main():
    base_url = "http://127.0.0.1:5000/lingshare-dev/#"
    lpk = '1401'
    lipk = '5130'
    path = "/lessons/preview/{lpk}/matching/{lipk}/".format(
        lpk=lpk,
        lipk=lipk)
    url = base_url + path

    data = []

    driver = webdriver.Firefox()
    driver.get(url)
    pause(5, "Loading up page")

    driver.find_element_by_xpath("//button").click()

    play_game(driver)

    return driver, data

driver, data = main()
