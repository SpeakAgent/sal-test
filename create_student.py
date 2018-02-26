# Goal: Create a student, make some updates.
from datetime import datetime
import os
from time import sleep

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

from utilities import pause, getopts, teacher_login


def create_student(driver):
    return_data = []

    driver.find_element_by_id("n-classes").click()
    pause(10)

    driver.find_element_by_id('your-students-tab').click()
    driver.find_element_by_id("add-student").click()
    pause(1)

    time = datetime.now().strftime("%Y-%m-%d %H:%M")
    student_name = ('Selenium Test %s') % (time)
    driver.find_element_by_id('add-student-names').send_keys(student_name)
    return_data.append(("student", student_name))

    driver.find_element_by_id('add-student-btn').click()

    pause(5, "Loading before returning")

    driver.find_element_by_link_text(student_name).click()

    return return_data


def update_student(driver):
    return_data = []
    driver.find_element_by_id(
        'edit-student-button').click()
    
    time = datetime.now().strftime("%Y-%m-%d %H:%M")
    new_student_name = ('Selenium Edit Student %s') % (time)
    srudent_name = driver.find_element_by_id(
        'input-student-edit-name')
    srudent_name.clear()
    srudent_name.send_keys(new_student_name)
    return_data.append(("new student name", new_student_name))
    
    driver.find_element_by_id(
        'update-student-btn-1').click()
    pause(6)
    driver.find_element_by_id(
        'cancel-student-btn-1').click()

    return return_data

    

def main():
    base_url = "http://127.0.0.1:5000/lingshare-dev/#"
    driver = webdriver.Firefox()
    driver.get(base_url)
    pause(5, "Loading up page")
    teacher_login(driver)
    pause(5)
    data = create_student(driver)
    pause(5)
    data.extend(update_student(driver))

    return driver, data


driver, data = main()
