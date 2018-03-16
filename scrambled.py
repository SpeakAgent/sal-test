# Play a game of scrambled sentences.

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

from utilities import pause, getopts, teacher_login

def start_game(driver):
    load_btn = driver.find_element_by_class_name('btn-container-new-game')
    load_btn.click()
    pause(5, "Wait for gremlins")
    start_btn = driver.find_element_by_xpath('//*[contains(text(),"Start Game")]')
    start_btn.click()
    pause(1, "Wait for screen to load")
    driver.execute_script("window.scrollTo(0, 1080)")
    pick_level = driver.find_element_by_xpath('//*[contains(text(),"Pick Level")]')
    pick_level.click()
    pause(3, "Picking a level")
    grs = driver.find_elements_by_class_name("gremling-box")
    grs[-1].click()
    # Only the second one works, since that's our active one.
    next_btn = driver.find_elements_by_xpath('//*[contains(text(),"Next")]')[1]
    next_btn.click()

def check_done(driver):
    pass

def get_empty_slots(driver):
    slots = driver.find_elements_by_class_name('empty-slot') #Yes, bad class name
    empties = []
    for slot in slots:
        if not slot.text:
            empties.append(slot)
    return empties

def get_bads(driver):
    bad = []
    source_area, target_area = driver.find_elements_by_class_name('advancedDemo')
    for div in target_area.find_elements_by_class_name('sentence-container-color'):
        if div.value_of_css_property('background-color'):
            bad.append(div)
            continue
    return bad

def check_for_bad(driver):
    # If we find a red word, put it in the next empty div
    # But first, check!

    bad = get_bads(driver)

    print "Bad:", bad

    source_area, target_area = driver.find_elements_by_class_name('advancedDemo')
    targets = target_area.find_elements_by_class_name('itemlist')

    print "Targets:", targets

    if not bad:
        return bad, targets

    num = len(targets)
    print "Num", num

    dropped = ""

    # TODO: We need to keep track of where we dropped it
    for i in range(num):
        print "Round", i
        bad = get_bads(driver)
        print "Bads:", bad
        if not bad:
            return bad, targets
        targets = target_area.find_elements_by_class_name('itemlist')
        print "Targets:"
        for target in targets:
            print "\t", target


        if targets[i]._id == dropped:
            print "Same slot as last round. Skip"
            continue
        if targets[i].text:
            print "There's text. Something is already here. Assuming it's correct for now."
            continue
        bad[0].click()
        targets[i].click()
        dropped = targets[i]._id

        pause(1, "Pausing for next bit")
        

    return bad, targets


def play_game(driver):
    ''' Round one: Just one word missing. TODO: more words!
    '''
    # Get the two zones
    source_area, target_area = driver.find_elements_by_class_name('advancedDemo')

    while True:

        source_words = []
        target_blocks = []

        for div in source_area.find_elements_by_class_name('itemlist'):
            if div.text:
                source_words.append(div)

        for div in target_area.find_elements_by_class_name('itemlist'):
            if not div.text:
                target_blocks.append(div)

        print "SW# / TB#:", len(source_words), len(target_blocks)

        if not source_words:
            return source_words, target_blocks

        source_words[0].click()
        target_blocks[0].click()

        check_for_bad(driver)

    return source_words, target_blocks



def main(lpk=2114, lipk=8716):
    try:
        data = {}
        base_url = "http://127.0.0.1:5000/lingshare-dev/#"
        wl_path = "lessons/preview/{lpk}/scramble/{lipk}/".format(
            lpk=lpk,
            lipk=lipk)
        driver = webdriver.Firefox()
        driver.get(base_url)
        pause(5)
        teacher_login(driver)
        pause(5)
        driver.get(base_url + wl_path)
        pause(5, "loading page")
        start_game(driver)
        pause(5)
        while True:
            play_game(driver)
            pause(2, "Win screen")
            try:
                driver.execute_script("window.scrollTo(0, 1080)")
                nxt_btn = driver.find_element_by_xpath('//*[contains(text(),"Next sentence")]')
                nxt_btn.click()
                pause(1, "Next sentence!")
            except NoSuchElementException:
                print "Game done!"
                break
        

    except:
        pass # make sure the driver is at least returned

    return driver, data

if __name__=="__main__":
    driver, data = main()