from datetime import datetime
from random import choice

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.keys import Keys

from utilities import pause

def play_game(driver):
    cards = driver.find_elements_by_class_name("word-card")
    cards[0].click()
    pause(3)
    for i in range(len(cards)-1):
        nextbtn=driver.find_element_by_class_name('next-word')
        nextbtn.click()
        pause(3)

    allbtn = driver.find_element_by_xpath("/html/body/section/div/ui-view/aside/a[1]")
    allbtn.click()


def main():
    # http://127.0.0.1:5000/lingshare-dev/#/lessons/preview/2103/review/8637
    base_url = "http://127.0.0.1:5000/lingshare-dev/#"
    lpk = '2103'
    lipk = '8637'
    path = "/lessons/preview/{lpk}/review/{lipk}/".format(
        lpk=lpk,
        lipk=lipk)
    url = base_url + path

    data = []

    driver = webdriver.Firefox()
    driver.get(url)
    pause(5, "Loading up page")

    driver.find_element_by_xpath("/html/body/section/div/ui-view/ui-view/div[2]/div[1]/div[1]/div[2]/a").click()

    pause(2)
    play_game(driver)

    return driver, data


if __name__ == "__main__":
    driver, data = main()