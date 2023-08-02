import argparse
import unittest

parser = argparse.ArgumentParser(description='Calculate values of two numbers')
parser.add_argument('-browser',default='chrome', type=str, help='string1')
parser.add_argument('-excu',default='Local', type=str, help='string2')
args = parser.parse_args()

browser=args.browser
excu=args.excu
if __name__ == '__main__':
    from Tests.main_test import EcommerceTest
    suite = unittest.TestSuite()
    suite.addTest(EcommerceTest('test_flipkart_page'))
    suite.addTest(EcommerceTest('test_amazon_page'))
    suite.addTest(EcommerceTest('test_croma_page'))
    suite.addTest(EcommerceTest('test_display_info'))
    suite.addTest(EcommerceTest('test_modify_data_values'))
    suite.addTest(EcommerceTest('test_compare_product_and_display'))
    runner = unittest.TextTestRunner()
    runner.run(suite)
