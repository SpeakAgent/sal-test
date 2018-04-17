from datetime import datetime
from random import choice

from selenium import webdriver
from selenium.common.exceptions import (NoSuchElementException, ElementNotInteractableException,
    ElementNotVisibleException)
from selenium.webdriver.common.keys import Keys

from utilities import pause

from picturepairs import play_game


# Replace these with the lesson PK and the LI pk
pks = [[2038, 8314],
 [2037, 8311],
 [2036, 8306],
 [2035, 8303],
 [2034, 8298],
 [2033, 8295],
 [2032, 8292],
 [2031, 8289],
 [2030, 8286],
 [2027, 8262],
 [1588, 5848],
 [1586, 5842],
 [1583, 5833],
 [1580, 5824],
 [1577, 5815],
 [1574, 5806],
 [1571, 5797],
 [1568, 5788],
 [1565, 5779],
 [1562, 5770],
 [1559, 5761],
 [1556, 5752],
 [1553, 5743],
 [1550, 5734],
 [1547, 5725],
 [1544, 5716],
 [1538, 5698],
 [1536, 5692],
 [1523, 5660],
 [1520, 5651],
 [1517, 5642],
 [1514, 5633],
 [1511, 5624],
 [1508, 5615],
 [1505, 5606],
 [1502, 5597],
 [1498, 5585],
 [1495, 5576],
 [1482, 5515],
 [1479, 5506]]

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
