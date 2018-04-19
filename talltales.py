# Under construction

from datetime import datetime
from random import choice

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.keys import Keys

from utilities import pause

def get_right_word(driver, slot):
    ''' Assumes that the modal is already open
    '''
    # Get all of the possible words
    options = driver.find_elements_by_class_name('col-xs-3')
    words = []
    for option in options:
        words.append(option.text)
    print "Words", words
    
    # Clicking each one to see 
    # The choices are in a random order, so we just have to keep going
    # until one is right
    while True:
        options = driver.find_elements_by_class_name('col-xs-3')
        f = True
        i = 0
        while f:
            print "Trying", options[i].text
            if options[i].text in words:
                print "Haven't tried that!"
                words.remove(options[i].text)
                options[i].click()
                pause(2, "Letting choices go away")
                f = False
            i += 1

        if not driver.find_elements_by_class_name('square-choice-incorrect'):
            # There are no bad slots on the page, so we can move on
            return

        # Have to get the slot in a slightly different way
        slot = driver.find_element_by_class_name('tale-answer-incorrect')
        slot.click()
        pause(2, "Letting choices show up")
        


def play_game(driver):
    slots = driver.find_elements_by_class_name('typeOfSlot')
    for slot in slots:
        slot.click()
        pause(2, "Letting choices show up")
    
        get_right_word(driver, slot)

    

def main():
    # http://127.0.0.1:5000/lingshare-dev/#/lessons/preview/2103/tall/8870/
    base_url = "http://127.0.0.1:5000/lingshare-dev/#"
    lpk = '2103'
    lipk = '8870'
    path = "/lessons/preview/{lpk}/tall/{lipk}/".format(
        lpk=lpk,
        lipk=lipk)
    url = base_url + path

    data = []

    driver = webdriver.Firefox()
    driver.get(url)
    pause(5, "Loading up page")

    driver.find_element_by_class_name('btn-with-symbol').click()
    pause(5, "Letting Annie speak")
    driver.find_element_by_xpath("//*[contains(text(), 'Start Game')]").click()
    pause(5, "Loading next page")

    play_game(driver)

    return driver, data  

if __name__ == "__main__":
    driver, data = main()