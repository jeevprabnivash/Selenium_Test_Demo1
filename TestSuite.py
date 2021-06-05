import unittest
import HtmlTestRunner
import os
from demo1 import ProductShopping

# get all tests from SearchText  class
product_test = unittest.TestLoader().loadTestsFromTestCase(ProductShopping)

# create a test suite combining search_text and home_page_test
test_suite = unittest.TestSuite([product_test])


HtmlTestRunner.HTMLTestRunner(report_name="MyReport", add_timestamp=True).run(test_suite)