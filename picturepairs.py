from datetime import datetime
from random import choice

from selenium import webdriver
from selenium.common.exceptions import (NoSuchElementException, ElementNotInteractableException,
    ElementNotVisibleException)
from selenium.webdriver.common.keys import Keys

from utilities import pause

def play_game(driver):
    # We're going to keep clicking random items until we run out of screens
    rounds = 0
    cards = driver.find_elements_by_class_name('lexeme')
    imgs = []
    i = 0
    while True:      
        words = []
        img = driver.find_element_by_class_name('large-card')
        if img.get_attribute('src') not in imgs:
            imgs.append(img.get_attribute('src'))
        for card in cards:
            words.append(card.text)
        try:
            try:
                cards[i].click()
                i += 1
            except IndexError:
                pause(10, "Ugh, need to load more...")
                cards = driver.find_elements_by_class_name('lexeme')
                cards[i].click()
                i += 1
            pause(3, "Letting the new screen load if needed")
            cards = driver.find_elements_by_class_name('lexeme')
            curr_words = []
            for card in cards:
                curr_words.append(card.text)
            print "Checking", words, curr_words
            if not words == curr_words:
                rounds += 1
                i = 0
        except ElementNotInteractableException:
            print "Game done"
            return rounds, "Done", imgs
        except ElementNotVisibleException:
            print "Game done 2"
            return rounds, "Done 2", imgs

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

    # driver = webdriver.Firefox()
    driver = webdriver.Chrome()
    driver.get(url)
    pause(5, "Loading up page")

    btn = driver.find_element_by_class_name("btn-with-symbol")
    btn.click()

    pause(2)
    play_game(driver)

    return driver, data


if __name__ == "__main__":
    driver, data = main()