import unittest
from selenium import webdriver

class ProductShopping(unittest.TestCase):
    @classmethod
    def setUpClass(inst):
        # create a new Firefox session
        inst.driver = webdriver.Chrome()
        inst.driver.implicitly_wait(7)
        inst.driver.maximize_window()
        # navigate to the application home page
        inst.driver.get("https://rahulshettyacademy.com/angularpractice/")
        inst.driver.title

    def test_shopping(self):
        driver_chrome = self.driver
        print(self.driver.title)
        driver_chrome.find_element_by_css_selector("a[href*='shop']").click()
        products = driver_chrome.find_elements_by_xpath("//div[@class='card h-100']")
        for product in products:
            productName = product.find_element_by_xpath("div/h4/a").text
            if productName == "Blackberry":
                print(productName)
                product.find_element_by_xpath("div/button").click()
                driver_chrome.find_element_by_xpath("//a[@class='nav-link btn btn-primary']").click()
                driver_chrome.find_element_by_xpath("//button[@class='btn btn-success']").click()
                driver_chrome.find_element_by_xpath("//input[@id='country']").send_keys("India")
                driver_chrome.find_element_by_xpath("//div[@class='suggestions']/ul/li/a").click()
                driver_chrome.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
                driver_chrome.find_element_by_xpath("//div/form/input[@class='btn btn-success btn-lg']").click()
                success = (
                    driver_chrome.find_element_by_xpath("//div[@class='alert alert-success alert-dismissible']").text)
                print(success)



    @classmethod
    def tearDownClass(inst):
        # close the browser window
        inst.driver.quit()

if __name__ == '__main__':
    unittest.main()