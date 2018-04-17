from datetime import datetime
import itertools
from random import choice

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.keys import Keys

from utilities import pause, teacher_login

def get_ingredients(driver):
    ingredients = []
    elems = driver.find_elements_by_class_name('bold')
    for e in elems:
        if e.text: ingredients.append(e)

    return ingredients

def get_word(driver):
    used = []

    pause(5, "Letting Annie talk 2")
    btn = driver.find_element_by_xpath("//*[contains(text(), 'Next')]")    
    btn.click()
    pause(5, "Letting Annie talk 3")

    ings = get_ingredients(driver)
    blanks = driver.find_elements_by_class_name('border-bottom-lines')    

    combos = itertools.combinations(range(len(ings)), len(blanks))

    # NEXT: Click ingredients until mix can be interacted with. Add them to used.
    for i, j in combos:
        print "Trying", i,j
        try:
            ings[i].click()
            ings[j].click()
        except ElementNotInteractableException:
            print "Returning..."
            continue

        driver.find_element_by_link_text('Mix!').click()
        pause(3, "Waiting for mixing animation")


def play_game(driver):
    found_words = []

    btn = driver.find_element_by_xpath("//*[contains(text(), 'Play Now!')]")
    btn.click()
    pause(5, "Allowing game to load")
    # There's an offscreen non-clickable play now
    btn = driver.find_elements_by_xpath("//*[contains(text(), 'Play Now!')]")[1]
    btn.click()
    pause(5, "Let Annie talk...")
    words = driver.find_elements_by_class_name("bold")
    n = 0
    for word in words:
        if word.text: n +=1

    for i in range(n):
        words = driver.find_elements_by_class_name("bold")

        found_words.append(words[i].text)
        words[i].click()

        get_word(driver)
        



def main():
    # http://127.0.0.1:5000/lingshare-dev/#/lessons/preview/2103/review/8637
    base_url = "http://127.0.0.1:5000/lingshare-dev/#"
    lpk = '2103'
    lipk = '8788'
    path = "/lessons/preview/{lpk}/vocablab/{lipk}/".format(
        lpk=lpk,
        lipk=lipk)
    url = base_url + path

    data = []

    driver = webdriver.Firefox()
    driver.get(base_url)
    pause(5, "Loading up page")
    teacher_login(driver)
    pause(5)
    driver.get(url)
    pause(5)
    play_game(driver)

    return driver, data


if __name__ == "__main__":
    driver, data = main()