import time

from selenium.webdriver.common.by import By

from Locators.croma_locators import CromaLocators as cl
from Utilites.BasePage import BaseClass


class CromaPage:
    '''flipkart locators and driver are initialized'''

    def __init__(self, driver):
        self.driver = driver
        self.croma_custom_icon = cl.croma_custom_icon
        self.croma_price = cl.croma_price
        self.croma_rate = cl.croma_rate
        self.croma_rating_review = cl.croma_rating_review

    def croma_compare(self, source_link):
        driver = self.driver
        driver.switch_to.new_window('WINDOW')
        driver.get(source_link)
        # time.sleep(2)
        # driver.refresh()
        driver.implicitly_wait(10)
        wait = BaseClass(driver)
        try:
            if wait.verifywait(By.ID, self.croma_custom_icon).is_displayed():
                driver.find_element(By.ID, self.croma_custom_icon).click()
        except:
            pass
        time.sleep(2)
        try:
            if not (driver.find_element(By.ID, self.croma_price).is_displayed()):
                driver.refresh()
        except:
            pass
        c_price = driver.find_element(By.ID, self.croma_price)
        corma_price = c_price.text
        corma_rating = driver.find_element(By.XPATH, self.croma_rate).text
        corma_rating_reviws = driver.find_element(By.XPATH, self.croma_rating_review).text
        corma_r_v = corma_rating_reviws.split('&')
        corma_pepole_rating = corma_r_v[0]
        corma_pepole_review = corma_r_v[1]
        return corma_price, corma_rating, corma_pepole_rating, corma_pepole_review
