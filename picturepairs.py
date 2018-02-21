from datetime import datetime
from random import choice

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.keys import Keys

from utilities import pause

def play_game(driver):
    # We're going to keep clicking random items until we run out of screens
    while True:
        cards = driver.find_elements_by_class_name('lexeme')
        try:
            choice(cards).click()
        except ElementNotInteractableException:
            print "Game done"
            return
        pause(3)


def main():
    base_url = "http://127.0.0.1:5000/lingshare-dev/#"
    lpk = '2103'
    lipk = '8638'
    path = "/lessons/preview/{lpk}/picturepairs/{lipk}/".format(
        lpk=lpk,
        lipk=lipk)
    url = base_url + path

    data = []

    driver = webdriver.Firefox()
    driver.get(url)
    pause(5, "Loading up page")

    driver.find_element_by_xpath("/html/body/section/div/ui-view/div[3]/div[1]/div[1]/div[2]/button").click()

    pause(2)
    play_game(driver)

    return driver, data


if __name__ == "__main__":
    driver, data = main()