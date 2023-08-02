import time
from selenium import webdriver
from Pages.amazone_page import AmazonPage
from Pages.croma_page import CromaPage
from Pages.display_page import Display
from Pages.flipkart_page import FlipkartPage
from Utilites.comparision import compare_products
from Utilites.modify_data import ModifyData
import unittest
from Utilites.PassArgument import browser,excu

class EcommerceTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.excu = excu
        cls.browser = browser
        cls.flipkart_link = "https://www.flipkart.com/oneplus-11-5g-eternal-green-256-gb/p/itm668119d115289?pid=MOBGMUHCGYAU8WX6&lid=LSTMOBGMUHCGYAU8WX6YJSBOE&marketplace=FLIPKART&sattr[]=color&sattr[]=storage&sattr[]=ram&st=color"
        cls.amazon_link = "https://www.amazon.com/OnePlus-Dual-SIM-Smartphone-Hasselblad-Processor/dp/B0BNWQYGZZ/ref=sr_1_1?crid=JRZGOYE9YJQ1&keywords=oneplus%2B11r%2B5g&qid=1690353972&sprefix=onepluse%2B11r%2B5g%2B%2Caps%2C365&sr=8-1&th=1"
        cls.croma_link = "https://www.croma.com/oneplus-11-5g-16gb-ram-256gb-eternal-green-/p/268762"
        # create a webdriver object for chrome-option and configure
        option = webdriver.ChromeOptions()
        option.add_experimental_option('useAutomationExtension', False)
        option.add_argument('--ignore-certificate-errors')
        option.add_argument('--start-maximized')
        option.add_experimental_option("useAutomationExtension", False)
        option.add_experimental_option("excludeSwitches", ["enable-automation"])
        option.add_argument("--disable-blink-features=AutomationControlled")
        cls.flag = False
        if excu == 'Local':
            if browser == 'chrome':
                cls.driver = webdriver.Chrome(options=option)
                cls.driver.implicitly_wait(30)
            elif browser == 'firefox':
                cls.driver = webdriver.Firefox(options=option)
                cls.driver.implicitly_wait(30)
            elif browser == 'MicrosoftEdge':
                cls.driver = webdriver.Edge(options=option)
                cls.driver.implicitly_wait(30)

            else:
                print("Please choose correct browser")
        if excu == 'Grid':
            if browser == "chrome":
                print(f"Running the test script on {browser} browser")
                cls.driver = webdriver.Remote(command_executor="http://localhost:4444/wd/hub",
                                          options=option)

            elif browser == "firefox":
                print(f"Running the test script on {browser} browser")
                cls.driver= webdriver.Remote(command_executor="http://localhost:4444/wd/hub",
                                          options=option)
            elif browser=='MicrosoftEdge':
                print(f"Running the test script on {browser} browser")
                cls.driver = webdriver.Remote(command_executor="http://localhost:4444/wd/hub",
                                              options=option)
            else:
                print('Choose correct Browser..')

        """
        if excu == 'saucelab':
            if browser == 'chrome':
                options = webdriver.ChromeOptions()
                options.browser_version = 'latest'
                options.platform_name = 'Windows 10'

                sauce_url = "https://oauth-shivamsharmamdh-6984d:5750d6be-5e92-431c-9f65-01c0683b16e0@ondemand.eu-central-1.saucelabs.com:443/wd/hub"
                cls.driver = webdriver.Remote(command_executor=sauce_url, options=options)

                cls.driver.get("https://app.keka.com/Account/KekaLogin?returnUrl=%2F")
                cls.action = ActionChains(cls.driver)
                cls.wait = WebDriverWait(cls.driver, 60)
            elif browser == 'firefox':
                options = webdriver.FirefoxOptions()
                options.browser_version = 'latest'
                options.platform_name = 'Windows 10'

                sauce_url = "https://oauth-shivamsharmamdh-6984d:5750d6be-5e92-431c-9f65-01c0683b16e0@ondemand.eu-central-1.saucelabs.com:443/wd/hub"
                cls.driver = webdriver.Remote(command_executor=sauce_url, options=options)
                cls.wait = WebDriverWait(cls.driver, 60)

            else:
                print("Please choose correct driver")
                """
        print("*************************************************************************** \n")
        print("                     Starting Program, Please wait ..... \n")
        print("*************************************************************************** \n")
    @classmethod
    def test_flipkart_page(cls):
        print("Connecting to Flipkart")
        flipkart_obj = FlipkartPage(cls.driver)
        cls.product, cls.flipkart_price, cls.flipkart_rating, cls.flipkart_people_rate, cls.flipkart_review = flipkart_obj.flipkart_compare(cls.flipkart_link)
        print(" ---> Successfully retrieved the data from Flipkart \n")
        time.sleep(2)
        print("*************************************************************************** \n")
    @classmethod
    def test_amazon_page(cls):
        print("Connecting to Amazon")
        print("*************************************************************************** \n")
        amazon_obj = AmazonPage(cls.driver)
        cls.amazon_price, cls.amazon_rating, cls.amazon_pepol_rate, cls.amazon_review = amazon_obj.amazon_compare(cls.amazon_link)
        print(" ---> Successfully retrieved the data from Amazon \n")
        time.sleep(2)
        print("*************************************************************************** \n")
    @classmethod
    def test_croma_page(cls):
        print("Connecting to Croma")
        print("*************************************************************************** \n")
        croma_obj = CromaPage(cls.driver)
        cls.corma_price, cls.corma_rating, cls.corma_pepole_rating, cls.corma_pepole_review = croma_obj.croma_compare(cls.croma_link)
        print(" ---> Successfully retrieved the data from Croma\n")
        time.sleep(2)
        print("*************************************************************************** \n")
    @classmethod
    def test_display_info(cls):
        # Final display
        cls.display_obj = Display()
        print("#------------------------------------------------------------------------#")
        cls.display_obj.display_flipkart_data(cls.product, cls.flipkart_price, cls.flipkart_rating,cls.flipkart_people_rate, cls.flipkart_review)
        print("#------------------------------------------------------------------------#")
        cls.display_obj.display_amazon_data(cls.amazon_price, cls.amazon_rating, cls.amazon_pepol_rate,cls.amazon_review)
        print("#------------------------------------------------------------------------#")
        cls.display_obj.display_croma_data(cls.corma_price, cls.corma_rating, cls.corma_pepole_rating,cls.corma_pepole_review)
        print("*************************************************************************** \n")
    @classmethod
    def test_modify_data_values(cls):
        # Modify Data Values
        # Create object for ModifyData class
        cls.modify_obj=ModifyData()
        # Call the method modify_price_data() from ModifyData class for modifying price data
        cls.prices=cls.modify_obj.modify_price_data(cls.flipkart_price, cls.amazon_price, cls.corma_price)

        # Call the method modify_people_rate_data() from ModifyData class for modifying people rate data
        cls.total_peoples_rating = cls.modify_obj.modify_people_rate_data(cls.flipkart_people_rate, cls.amazon_pepol_rate, cls.corma_pepole_rating)

        # # Call the method modify_reviews() from ModifyData class for modifying people reviews data
        cls.reviews=cls.modify_obj.modify_reviews(cls.flipkart_review, cls.amazon_review, cls.corma_pepole_review)

        # Call the method modify_people_rate_data() from ModifyData class for modifying people rate data
        cls.ratings=cls.modify_obj.modify_rating_in_stars(cls.flipkart_rating, cls.amazon_rating, cls.corma_rating)
        print('Data Modified successfully...')
        print("*************************************************************************** \n")
    @classmethod
    def test_compare_product_and_display(cls):
        company = ['FlipKart', 'Amazon', 'Corma']
        lowest_price_product, highest_rating_product, highest_num_ratings_product,highest_reviews = compare_products(cls.prices, cls.ratings, cls.total_peoples_rating,cls.reviews)
        products_info = list(zip(company, cls.prices, cls.ratings, cls.total_peoples_rating, cls.reviews))
        dct = {}
        for tup in products_info:
            dct[tup[0]] = tup[1:]
        # Output the result
        print(f"{cls.product} with Lowest Price:")
        for k, v in dct.items():
            if lowest_price_product[0] in v:
                print(
                    f"Company:{k},Price: {lowest_price_product[0]}, Rating: {lowest_price_product[1]}, Number of Ratings: {lowest_price_product[2]}, Number of reviews: {lowest_price_product[3]}")

        print(f"\n{cls.product} with Highest Rating:")
        for k, v in dct.items():
            if highest_rating_product[0] in v:
                print(
                    f"company:{k},Price: {highest_rating_product[0]}, Rating: {highest_rating_product[1]}, Number of Ratings: {highest_rating_product[2]}, Number of reviews: {highest_rating_product[3]}")

        print(f"\n{cls.product} with Highest Number of Ratings:")
        for k, v in dct.items():
            if highest_num_ratings_product[0] in v:
                print(
                    f"Company:{k},Price: {highest_num_ratings_product[0]}, Rating: {highest_num_ratings_product[1]}, Number of Ratings: {highest_num_ratings_product[2]},Number of reviews: {highest_num_ratings_product[3]}")

        print(f"\n{cls.product} with Highest Number of Reviews:")
        for k, v in dct.items():
            if highest_reviews[0] in v:
                print(
                    f"Company:{k},Price: {highest_reviews[0]}, Rating: {highest_reviews[1]}, Number of Ratings: {highest_reviews[2]},Number of reviews: {highest_reviews[3]}")
    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

# def suite():
#
#     suite = unittest.TestSuite()
#     suite.addTest(EcommerceTest('test_flipkart_page'))
#     suite.addTest(EcommerceTest('test_amazon_page'))
#     suite.addTest(EcommerceTest('test_croma_page'))
#     suite.addTest(EcommerceTest('test_display_info'))
#     suite.addTest(EcommerceTest('test_modify_data_values'))
#     suite.addTest(EcommerceTest('test_compare_product_and_display'))
#     return suite
#
# if __name__ == '__main__':
#     runner = unittest.TextTestRunner(verbosity=2)
#     runner.run(suite())
