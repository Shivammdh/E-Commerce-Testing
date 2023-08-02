import time

from selenium.webdriver.common.by import By

from Locators.amazon_locators import AmazonLocators as al
from Utilites.BasePage import BaseClass


class AmazonPage:
    '''Amazon locators and driver are initialized'''

    def __init__(self, driver):
        self.driver = driver
        self.amz_lang_btn = al.amz_lang_btn
        self.amz_lang_dropdwn = al.amz_lang_dropdwn
        self.amz_lang_save_btn = al.amz_lang_save_btn
        self.amz_price = al.amz_price
        self.amz_rate = al.amz_rate
        self.amz_people_rate = al.amz_people_rate
        self.amz_rview = al.amz_rview

    def amazon_compare(self, source_link):
        driver = self.driver
        driver.get(source_link)
        try:
            if driver.find_element(By.ID, "captchacharacters").is_displayed():
                captcha = input('Enter Captcha:')
                driver.find_element(By.ID, "captchacharacters").send_keys(captcha)
                time.sleep(2)
                driver.find_element(By.XPATH, "//button").click()
        except Exception:
            pass
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH, self.amz_lang_btn).click()
        time.sleep(2)
        dropdwn = driver.find_element(By.ID, self.amz_lang_dropdwn)
        select = BaseClass(driver)
        select.selectOptionByValue(dropdwn, 'INR')
        time.sleep(2)
        driver.find_element(By.XPATH, self.amz_lang_save_btn).click()
        # a_price = driver.find_element_by_id("priceblock_ourprice")
        time.sleep(3)
        a_price = driver.find_element(By.XPATH, self.amz_price)
        amazon_price = a_price.text
        amazon_rating = driver.find_element(By.XPATH, self.amz_rate).text
        amazon_pepol_rate = driver.find_element(By.ID, self.amz_people_rate).text
        amazon_review = driver.find_element(By.XPATH, self.amz_rview).text
        return amazon_price, amazon_rating, amazon_pepol_rate, amazon_review
