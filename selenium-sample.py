import os
import sys
import pytest
from selenium import webdriver

# File Name
FILENAME = os.path.join(os.path.dirname(os.path.abspath(__file__)), "screenshots/test.png")


def test_function():
    driver = webdriver.Chrome('/path/to/chromedriver')
    driver.get("https://proguru.jp")
    title = driver.title
    assert title == "プログル｜学校の授業で使えるプログラミング教材"

    driver.save_screenshot(FILENAME)

    driver.quit()
