# -*- coding: utf-8 -*-
from selenium import webdriver
from time import sleep

from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Firefox()
driver.set_window_size(1080, 780)

driver.get("https://www.linkedin.com/")
print(driver.title)

# driver.maximize_window()

sleep(1)
driver.find_element_by_partial_link_text("Sign in").click()

sleep(1)
driver.find_element_by_id("username").clear()
driver.find_element_by_id("username").send_keys("vicky.feng.yu.2019@gmail.com")

driver.find_element_by_id("password").clear()
driver.find_element_by_id("password").send_keys("Well@1314")
sleep(2)

driver.find_element_by_class_name("btn__primary--large.from__button--floating").click()
sleep(1.5)

driver.find_element_by_id("jobs-tab-icon").click()
sleep(1.5)
print(driver.title)

driver.find_element_by_xpath("//*[contains(@id, 'jobs-search-box-keyword-id')]").clear()
driver.find_element_by_xpath("//*[contains(@id, 'jobs-search-box-keyword-id')]").send_keys("Software Engineer")

driver.find_element_by_xpath("//*[contains(@id, 'jobs-search-box-location-id')]").clear()
driver.find_element_by_xpath("//*[contains(@id, 'jobs-search-box-location-id')]").send_keys("Singapore")

driver.find_element_by_class_name("jobs-search-box__submit-button.artdeco-button.artdeco-button--3.ml2").click()
sleep(3)
print(driver.title)

count = 0

driver.execute_script("window.scrollTo(0, document.body.scrollHeight + 3000);")

while True:
    try:
        sleep(3)
        print("count: {}", count)
        jobList_init = driver.find_elements_by_class_name("job-card-search__easy-apply")
        # print("len(jobList_init): {}", len(jobList_init))

        if count >= len(jobList_init):
            count = len(jobList_init) - 1

        leftEasyApplyItem = jobList_init[count]
        leftEasyApplyItem.click()
        count += 1
        try:
            sleep(2)
            rightEasyApplyItem = driver.find_element_by_xpath(
                "//span[contains(@class, 'artdeco-button__text') and text()='Easy Apply']")
            rightEasyApplyItem.click()
            sleep(2)
        except BaseException:
            print("rightEasyApplyItem ignore")
            sleep(0.5)
            continue

    except NoSuchElementException:
        print("leftEasyApplyItem ignore")
        count += 1
        sleep(0.3)

    try:
        while True:
            nextItem = driver.find_element_by_xpath(
                "//span[contains(@class, 'artdeco-button__text') and text()='Next']")
            if nextItem.size == 0:
                break
            nextItem.click()
        sleep(1)
    except BaseException:
        print("nextItem ignore")
        sleep(0.3)

    try:
        reviewItem = driver.find_element_by_xpath(
            "//span[contains(@class, 'artdeco-button__text') and text()='Review']")
        reviewItem.click()
        sleep(1)
    except BaseException:
        print("reviewItem ignore")
        sleep(0.5)

    try:
        if driver.find_element_by_id("follow-company-checkbox").get_attribute('checked'):
            driver.find_elements_by_class_name("jobs-easy-apply-footer__follow-company.mt5")[0].click()

        submitItem = driver.find_element_by_xpath(
            "//span[contains(@class, 'artdeco-button__text') and text()='Submit application']")
        submitItem.click()
        sleep(3)
        continue
    except BaseException:
        print("submitItem ignore")
        sleep(0.5)
        continue
