from selenium.webdriver.common.by import By

from Locators.flipkart_locators import FlipkartLocators as fl


class FlipkartPage:
    '''flipkart locators and driver are initialized'''

    def __init__(self, driver):
        self.driver = driver
        self.fk_price = fl.fk_price
        self.product_name = fl.product_name
        self.fk_rate = fl.fk_rate
        self.fk_tot_rating = fl.fk_tot_rating
        self.fk_review = fl.fk_review

    def flipkart_compare(self, source1):
        driver = self.driver
        driver.get(source1)
        driver.implicitly_wait(10)
        f_price = driver.find_element(By.XPATH, self.fk_price)
        pr_name = driver.find_element(By.XPATH, self.product_name)
        product = pr_name.text
        flipkart_price = f_price.text
        flipkart_rating = driver.find_element(By.CSS_SELECTOR, self.fk_rate).text
        flipkart_people_rate = driver.find_element(By.XPATH, self.fk_tot_rating).text
        flipkart_review = driver.find_element(By.XPATH, self.fk_review).text
        return product, flipkart_price, flipkart_rating, flipkart_people_rate, flipkart_review
