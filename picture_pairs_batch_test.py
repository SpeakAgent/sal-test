from datetime import datetime
from random import choice

from selenium import webdriver
from selenium.common.exceptions import (NoSuchElementException, ElementNotInteractableException,
    ElementNotVisibleException)
from selenium.webdriver.common.keys import Keys

from utilities import pause

from picturepairs import play_game


# Replace these with the lesson PK and the LI pk
pks = [
 # (1866, 7322),
 (1749, 6648),
 (1688, 6311),
 (1678, 6254),
 (1677, 6250),
 (1674, 6237),
 (1673, 6231),
 (1672, 6228),
 (1663, 6179),
 (1651, 6120),
 (1650, 6117),
 (1632, 6031),
 (1617, 5957),
 (1616, 5954),
 (1615, 5951),
 (1614, 5948),
 (1613, 5945),
 (1612, 5942),
 (1611, 5939),
 (1610, 5936),
 (1609, 5933)
 ]

def print_results(results):
    for result in results:
        print "\t".join(str(x) for x in result[:-1]),
        print "\t" + result[-1][-1]

def main():
    try:
        base_url = "http://teach.speakagent.com/#"
        driver = webdriver.Chrome()
        # driver = webdriver.Firefox()
        data = []

        for lpk, lipk in pks:
            path = "/lessons/preview/{lpk}/picturepairs/{lipk}/".format(
                lpk=lpk,
                lipk=lipk)
            url = base_url + path


            driver.get(url)
            pause(7, "Loading up page")

            btn = driver.find_element_by_class_name("btn-with-symbol")
            btn.click()

            rounds, result, last_card = play_game(driver)

            data.append((lpk, lipk, rounds, result, last_card))

            print_results(data)
            pause(2)
    except Exception as inst:
        print "Error", inst, inst.args
        pass # At least let me get my data

    return driver, data

if __name__ == "__main__":
    driver, data = main()
