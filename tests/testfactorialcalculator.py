# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 20:13:22 2021

@author: Pradeep Sheokand
"""
from src.factorialsourcecode import calcFactorialRangeOnChrome, calcFactorialRangeOnFirefox, calcFactorialSingleNumber, calcFactorialUnexpected, calcExpectedFactorialSingleNumber, calcExpectedFactorialRange
import pytest
import random
import os

'''TEST_CASE_1: Factorial of 0, expected result is 1, result is in format (BaseNumber, BaseNumberFactorial) hence {0,1} '''
@pytest.mark.parametrize(
    "items,expected",
    [
        (0, [[0,1]]),  #BaseNumber is 0, second value is the base number and its expected output
    ],
)
def test_factorial_basic(items, expected):
    actualResult = calcFactorialSingleNumber(items)
    assert actualResult  == expected #input 0 is passed to calcFactorialSingleNumber function that launches the factorial calculator website, enters the basenumber and reads its factrial value; output is compared with expected output given above
    

'''TEST_CASE_2: Factorial of -ive numbers, expected result is: Calculator should print a message: Please enter a positive integer '''
@pytest.mark.parametrize(
    "items,expected",
    [
        (-2, 'Please enter a positive integer'),  #BaseNumber is 0, second value is the base number and its expected output
    ],
)
def test_factorial_negative(items, expected):
    actualResult = calcFactorialUnexpected(items)
    assert actualResult  == expected

'''TEST_CASE_3: Factorial of a String, expected result is: Calculator should print a message: Please enter an integer '''
@pytest.mark.parametrize(
    "items,expected",
    [
        ('abc', 'Please enter an integer'),  #BaseNumber is 0, second value is the base number and its expected output
    ],
)
def test_factorial_string(items, expected):
    actualResult = calcFactorialUnexpected(items)
    assert actualResult  == expected
    
    
'''TEST_CASE_4: Factorial of a positive integer with a + sign in front example: +3, expected result is: Calculator should treat it as a positive integer and calculate factorial, in this instance [+3,6]'''
@pytest.mark.parametrize(
    "items,expected",
    [
        (+3, [[3,6]]),  #BaseNumber is 0, second value is the base number and its expected output
    ],
)
def test_factorial_plus_sign(items, expected):
    actualResult = calcFactorialSingleNumber(items)
    assert actualResult  == expected
    
    
'''TEST_CASE_5: Factorial of a big number, example: 500, expected result is: [500,'Infinity']'''
@pytest.mark.bignumbers
@pytest.mark.parametrize(
    "items,expected",
    [
        (500, 'The factorial of 500 is: Infinity'),  #BaseNumber is 0, second value is the base number and its expected output
    ],
)
def test_factorial_500(items, expected):
    actualResult = calcFactorialUnexpected(items)
    assert actualResult  == expected
    

'''TEST_CASE_6: Factorial of even bigger number, example: 1000, expected result is: [1000,'Infinity']'''
@pytest.mark.bignumbers
@pytest.mark.parametrize(
    "items,expected",
    [
        (1000, 'The factorial of 1000 is: Infinity'),  #BaseNumber is 0, second value is the base number and its expected output
    ],
)
def test_factorial_1000(items, expected):
    actualResult = calcFactorialUnexpected(items)
    assert actualResult  == expected
    
'''TEST_CASE_7: Factorial of a random number between 0 and 20, it is compared with factorial calculated by factorial function in Python Math module'''    
@pytest.mark.random
def test_factorial_random():
    items = random.randint(0,21)
    actualResult = calcFactorialSingleNumber(items)
    expectedResult = calcExpectedFactorialSingleNumber(items)
    assert actualResult  == expectedResult
    
'''TEST_CASE_8: Factorial of Numbers between [10,100],it is compared with factorial calculated by factorial function in Python Math module. 
This test-case is run on the Chrome Browser'''
@pytest.mark.cross_browser    
def test_factorial_positiveinteger_chrome():
    expectedResult = calcExpectedFactorialRange(95,101)
    actualResult = calcFactorialRangeOnChrome(95,101)
    assert expectedResult == actualResult
    
    
'''TEST_CASE_9: Factorial of Numbers between [10,100],it is compared with factorial calculated by factorial function in Python Math module. 
This test-case is run on the Firefox Browser'''
@pytest.mark.cross_browser    
def test_factorial_positiveinteger_firefox():
    expectedResult = calcExpectedFactorialRange(95,101)
    actualResult = calcFactorialRangeOnFirefox(95,101)
    assert expectedResult == actualResult
