# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 18:36:51 2021

@author: Pradeep Sheokand
"""
import time
import logging
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
import math
import re
import os

BASEURL = 'https://borg:qa@sosour.pythonanywhere.com/'

#Function to set-up Chrome Driver
def chromebrowser():
    driver = webdriver.Chrome(executable_path='chromedriver')
    return driver

#Function to set-up Firefox Driver
def firefoxbrowser():
    driver = webdriver.Firefox(executable_path='geckodriver')
    return driver

#Function to locate web calculator search box element
def searchboxElement(driver):
    try:
        search_box = driver.find_element_by_name("number")
        driver.implicitly_wait(3)
        return search_box
        
    except TimeoutException:
        print ("Timed out waiting for element to load")

#Function to locate web calculator factorial calculation button element
def submitButtonElement(driver):
    try:
        submitbutton_element = driver.find_element_by_xpath("//p//button[@type=\"submit\"]")
        driver.implicitly_wait(3)
        return submitbutton_element
        
    except TimeoutException:
        print ("Timed out waiting for element to load")

#Function to locate web calculator result text element
def readResultText(driver):
    try:
        result_element = driver.find_element_by_id("resultDiv")
        driver.implicitly_wait(3)
        return result_element
        
    except TimeoutException:
        print ("Timed out waiting for element to load")

#Function to calculate Factorial using Factorial Web Calculator, it takes a single number as input
def calcFactorialSingleNumber(inputNumber):
    driver = chromebrowser()
    driver.get(BASEURL)
    resultList = []
    searchbox_element = searchboxElement(driver)
    searchbox_element.clear()
    searchbox_element.send_keys(inputNumber)
    submitbutton_element = submitButtonElement(driver)
    submitbutton_element.click()
    driver.implicitly_wait(5)
    resulttext_element = readResultText(driver)
    txt = resulttext_element.text
    logging.getLogger("urllib3").setLevel(logging.ERROR)
    logging.info(f"txt= ${txt}")
    final_list = re.findall("[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?", txt)
    resultList.append(final_list)    
    resultList = [[int(float(j)) for j in i] for i in resultList]
    logging.info(f"result_list= ${resultList}")
    return resultList

#Function to calculate Factorial using Factorial Web Calculator, it is used to test out negative scenarios such as text, negative numbers, big numbers etc.
def calcFactorialUnexpected(value):
    driver = chromebrowser()
    driver.get(BASEURL)
    searchbox_element = searchboxElement(driver)
    searchbox_element.clear()
    searchbox_element.send_keys(value)
    submitbutton_element = submitButtonElement(driver)
    submitbutton_element.click()
    driver.implicitly_wait(5)
    resulttext_element = readResultText(driver)
    txt = resulttext_element.text
    logging.getLogger("urllib3").setLevel(logging.ERROR)
    logging.info(f"txt= ${txt}")
    return txt

#Function to calculate Factorial using Factorial Web Calculator on CHROME, it takes a range of numbers as input
def calcFactorialRangeOnChrome(lower_range,upper_range):
    list_webtest = []
    driver = chromebrowser()
    driver.get(BASEURL)
    driver.implicitly_wait(5)
    search_box = searchboxElement(driver)
    for i in range(lower_range,upper_range):
        search_box.clear()
        search_box.send_keys(i)
        driver.implicitly_wait(5)
        submitbutton_element = submitButtonElement(driver)
        submitbutton_element.click()
        driver.implicitly_wait(5)
        resulttext_element = readResultText(driver)
        txt = resulttext_element.text
        driver.implicitly_wait(5)
        logging.getLogger("urllib3").setLevel(logging.ERROR)
        logging.info(f"txt= ${txt}")
        final_list = re.findall("[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?", txt)
        list_webtest.append(final_list)
            
    list_webtest = [[int(float(j)) for j in i] for i in list_webtest]
    driver.quit()
    return list_webtest

#Function to calculate Factorial using Factorial Web Calculator on FIREFOX, it takes a range of numbers as input
def calcFactorialRangeOnFirefox(lower_range,upper_range):
    list_webtest = []
    driver = firefoxbrowser()
    driver.get(BASEURL)
    driver.implicitly_wait(5)
    search_box = searchboxElement(driver)
    for i in range(lower_range,upper_range):
        search_box.clear()
        search_box.send_keys(i)
        submitbutton_element = submitButtonElement(driver)
        submitbutton_element.click()
        driver.implicitly_wait(5)
        resulttext_element = readResultText(driver)
        txt = resulttext_element.text
        logging.getLogger("urllib3").setLevel(logging.ERROR)
        logging.info(f"txt= ${txt}")
        final_list = re.findall("[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?", txt)
        list_webtest.append(final_list)
            
    list_webtest = [[int(float(j)) for j in i] for i in list_webtest]
    driver.quit()
    return list_webtest

#Function to calculate Factorial using Python Math Factorial Function, it takes a range of numbers as input
def calcExpectedFactorialRange(lower_range,upper_range):
    list_math = []
    for i in range(lower_range,upper_range):
        list_math.append([i, float(math.factorial(i))])
        
    expectedFactorial = [[int(float(j)) for j in i] for i in list_math]
    return expectedFactorial

#Function to calculate Factorial using Python Math Factorial Function, it takes one number as input
def calcExpectedFactorialSingleNumber(basenumber):
    list_math = []
    list_math.append([basenumber, float(math.factorial(basenumber))])
    
    expectedFactorial = [[int(float(j)) for j in i] for i in list_math]
    return expectedFactorial
