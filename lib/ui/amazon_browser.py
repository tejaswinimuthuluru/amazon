import re
from threading import current_thread
import logging
from lib.common.common_locators import *

WAIT_FOR = 3


class AmazonBrowser():
    """
    Function to create web driver object and some common function in it
    """
    def __init__(self,
                 username,
                 password,
                 browser_type,
                 geckodriver_log_path='C:/Users/Dell/Downloads/chromedriver.exe',
                 browser_wait=10,
                 uri='https://www.amazon.in/'):
        """ Constructor for Amazon Browser class to initialize the attributes of a class

        :param username(string): Amazon login username.
        :param password(string): Amazon login password.
        :param browser_type(string): Type of web browser ['Firefox, chrome].
        :param browser_wait(string): Implicitly wait to execute selenium commands.
        """
        self.logger = logging.getLogger(current_thread().name)
        super().__init__(browser_type=browser_type, browser_wait=browser_wait,
                         geckodriver_log_path=geckodriver_log_path)
        self.username = username
        self.password = password
        self.uri = uri


    def login_amazon(self, **kwargs):
        """Login to AMAZON.

        :param kwargs: Keyword arguments ex: wait=5, tries=5

        :returns: type boolean. True for Success and False for failed cases.
        """
        try:
            self.logger.info("Logging in to Amazon Browser")
            self.driver.get(self.url)
            self.wait_untill_presence_of_element(
                'id',
                amazon_logo,
                msg="'Amazon page' is not present in 'Chrome web driver' Page")
            self.driver.maximize_window()
            self.check_element_exists_by_id(profile_box, element_name="Profile box").click()
            self.find_element_by_id(email_textbox).send_keys('9346439423')
            self.find_element_by_id(click_continue).click()
            self.find_element_by_id(password_textbox).send_keys('Teja@123')
            self.find_element_by_id(click_submit).click()

            # self.type_text("username", self.username)
            # self.type_text_by_name("password", self.password)
            # self.sleep(WAIT_FOR, 'before clicking submit button')
            # self.click_button("submit_btn", "id", element_name='submit button')
            # self.driver.find_element(By.ID, "nav-link-accountList-nav-line-1").click()
            # driver.find_element(By.ID, "ap_email").send_keys('9346439423')
            # driver.find_element(By.ID, "continue").click()
            # driver.find_element(By.ID, "ap_password").send_keys('Teja@123')
            # driver.find_element(By.ID, "signInSubmit").click()
            return True
        except Exception as e:
            self.logger.exception("login failed, Exception:{}".format(str(e)))





