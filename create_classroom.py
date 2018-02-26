# Goal: Create a classroom, add some students to it, make some updates.
from datetime import datetime
import os
from time import sleep

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

from utilities import pause, getopts, teacher_login


def create_classroom(driver):
    '''
    This is all the logic related to the cretion of a classroom.
    '''
    return_data = []

    driver.find_element_by_id("n-classes").click()
    pause(5)

    driver.find_element_by_id("add-classroom").click()
    pause(1)

    title = driver.find_element_by_id("classroom-new-title")
    classroom_title = "Selenium test " + datetime.now().strftime("%Y-%m-%d %H:%M")
    return_data.append(("title", classroom_title))
    title.send_keys(classroom_title)

    driver.find_element_by_id("classroom-new-description").send_keys("Description Test")

    section_name = "Section Name Test"
    driver.find_element_by_id("classroom-new-section-name").send_keys(section_name)

    driver.find_element_by_id("classroom-new-add-class-btn").click()

    pause(5, "Loading before returning")

    driver.find_element_by_link_text(classroom_title + " | " + section_name).click()

    return return_data


def create_student(driver):
    '''
    This is all the logic related to the creation of multiple students
    in the previously created classroom.
    '''
    return_data = []
    driver.find_element_by_id('add-classroom-student').click()
    pause(3)
    time = datetime.now().strftime("%Y-%m-%d %H:%M")
    students_names = ('Selenium Test 1 %s, Selenium Test 2 %s') % (time, time)
    driver.find_element_by_id('add-student-names').send_keys(students_names)
    return_data.append(("students", students_names))

    driver.find_element_by_id('add-student-btn').click()

    return return_data


def update_classroom(driver):
    return_data = []
    driver.find_element_by_id(
        'edit-classroom-button').click()

    time = datetime.now().strftime("%Y-%m-%d %H:%M")
    new_classroom_name = ('Selenium Edit Classroom %s') % (time)
    edit_name = driver.find_element_by_id(
        'input-classroom-edit-name')
    edit_name.clear()
    edit_name.send_keys(new_classroom_name)

    section_name = driver.find_element_by_id(
        'input-classroom-edit-section-name')
    section_name.clear()
    section_name.send_keys("Edit Section Name Test")

    description = driver.find_element_by_id(
        'input-classroom-edit-description')
    description.clear()
    description.send_keys("Description Edit Test")

    return_data.append(("new classroom name", new_classroom_name))

    driver.find_element_by_id(
        'update-classroom-btn-2').click()

    return return_data


def main():
    base_url = "http://127.0.0.1:5000/lingshare-dev/#"
    driver = webdriver.Firefox()
    driver.get(base_url)
    pause(5, "Loading up page")

    teacher_login(driver)
    pause(5)
    data = create_classroom(driver)
    pause(5)
    data.extend(create_student(driver))
    pause(5)
    data.extend(update_classroom(driver))

    return driver, data


driver, data = main()
