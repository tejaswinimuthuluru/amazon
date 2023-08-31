import pytest
import requests
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from lib.ui.amazon_browser import *
from selenium.webdriver.common.action_chains import ActionChains
import time


@pytest.mark.amazon
@pytest.mark.run(order=1)
class TestDashboard:
    """
    Amazon test cases are added successfully
    """

    def test_01_sign_in(self):
        driver = webdriver.Chrome()
        driver.get('https://www.amazon.in/')
        driver.maximize_window()

        # element = driver.find_element(By.ID, "nav-link-accountList")
        # action = webdriver.ActionChains(driver)
        # action.move_to_element(element).perform()
        # driver.find_element(By.ID, "nav-item-signout").click()
        driver.close()

    def test_02_post_call(self):
        url = 'https://jsonplaceholder.typicode.com/posts'
        headers = {
            'userId': 5,
            'title': 'Stuff and Things',
            "body": 'An amazing blog post about both stuff and things.'
        }
        r = requests.post(url, data=json.dumps(headers))
        print(r)
        print(r.content)



