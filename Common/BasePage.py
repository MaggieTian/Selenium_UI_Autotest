# -*- coding: utf-8 -*-
# @Time    : 2018/6/18
# @Author  : 
# @File    : BasePage.py

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class BasePage:

    """
    BasePage contains  all common ui interactions
    All pages should be inherited from this class
    """

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10

    def _get_element(self, locator: tuple, wait: int = None):

        '''
        :param locator: using to find element, is a tuple such as (By.ID,"login"),which means find element by id with given value
        :param wait: the wait time for find element
        :return: selenium.webdriver.remote.webelement.WebElement
        '''

        # check the wait time

        if not wait:
            wait = self.timeout

        if not isinstance(wait,int):
            raise  Exception("wait time should be int numbers:{wait}".format(wait=wait))

        element = WebDriverWait(self.driver, int(wait)).until(EC.presence_of_element_located(locator))
        return element

    def _get_elements(self, locator,wait=None):
        '''

        :param locator: using to find element, is a tuple such as (By.ID,"login"),which means find element by id with given value
        :param wait: the wait time for find element
        :return: the list of webElement
        '''

        if not wait:
            wait = self.timeout
        if not isinstance(wait,int):
            raise  Exception("wait time should be int numbers:{wait}".format(wait=wait))
        elements = WebDriverWait(self.driver, int(wait)).until(EC.presence_of_element_located(locator))

        return elements

    def element_is_present(self,locator):
        '''

        :param locator: the loctor that find element,s a tuple such as (By.ID,"login")
        :return: boolen
        '''
        element = self._get_element(locator)
        return element is not None

    def click(self,locator):
        '''

        :param locator: the loctor that find element,s a tuple such as (By.ID,"login")
        :return: None
        '''
        element = self._get_element(locator)
        time.sleep(3)
        element.click()

    def type_word(self,locator,text):
        '''

        :param locator: the loctor that find element,s a tuple such as (By.ID,"login")
        :param text: the text of typing
        :return: None
        '''
        element = self._get_element(locator)
        time.sleep(3)
        element.send_keys(text)

    def get_element_text(self,locator):
        '''

        :param locator: the loctor that find element,s a tuple such as (By.ID,"login")
        :return: the text of element

        '''

        element = self._get_element(locator)
        if element:
            return element.text
        else:
            return None

    def open_url(self, url):
        '''

        :param url: the url of web site
        :return: None
        '''

        self.driver.get(url)
        time.sleep(5)








