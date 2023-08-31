import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time


@pytest.mark.amazon
class TestAmazon:
    """
    Amazon test cases are added successfully
    """

    def test_01_sign_in(self):
        driver = webdriver.Chrome()
        driver.get('https://www.amazon.in/')
        driver.maximize_window()
        driver.find_element(By.ID, "nav-link-accountList-nav-line-1").click()
        driver.find_element(By.ID, "ap_email").send_keys('9346439423')
        driver.find_element(By.ID, "continue").click()
        driver.find_element(By.ID, "ap_password").send_keys('Teja@123')
        driver.find_element(By.ID, "signInSubmit").click()
        element = driver.find_element(By.ID, "nav-link-accountList")
        action = webdriver.ActionChains(driver)
        action.move_to_element(element).perform()
        driver.find_element(By.ID, "nav-item-signout").click()
        time.sleep(5)
        driver.close()

















