''' Put all general use functions here. 
'''

import os
from time import sleep

def pause(n, msg="(Loading)"):
    print "Sleeping for", n, "-", msg
    sleep(n)

def getopts(argv):
    opts = {}  # Empty dictionary to store key-value pairs.
    while argv:  # While there are arguments left to parse...
        if argv[0][0] == '-':  # Found a "-name value" pair.
            opts[argv[0]] = argv[1]  # Add key and value to the dictionary.
        argv = argv[1:]  # Reduce the argument list by copying it starting from index 1.
    return opts

def teacher_login(driver):
    ''' This is the login for the teacher only.
        Assumes that the username and password are in the env vars.
    '''
    print "Logging in"
    tlogin = driver.find_element_by_id("teacher-sign-in")
    tlogin.click()
    ufield = driver.find_element_by_id("login-email")
    pfield = driver.find_element_by_id("login-password")
    subbtn = driver.find_element_by_id("login-button")
    ufield.send_keys(os.environ.get('TUSER'))
    pfield.send_keys(os.environ.get('TPASS'))
    subbtn.click()