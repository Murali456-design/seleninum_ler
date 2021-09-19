# from selenium import webdriver
from time import sleep

from pageObject.CheckOutPage import CheckOutPage
from pageObject.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestDemoOne(BaseClass):
    log = BaseClass.get_Logger(__name__)

    def test_End2End(self):
        homepage = HomePage(self.launch)
        # log = self.get_Logger()
        checkoutpage = homepage.shopIteam()
        self.log.info("getting all the cart titles")
        sleep(1)
        all_elements = checkoutpage.get_cart_titles()
        i = -1
        for product in all_elements:
            i = i + 1
            if product.text == 'Nokia Edge':
                self.log.info(product.text + " is selected")
                checkoutpage.get_cart_footer()[i].click()
                break

        sleep(3)
        checkoutpage.get_checkout_primary().click()
        sleep(1)
        confrompage = checkoutpage.get_checkout_submit()
        self.log.info("click submit")
        sleep(1)
        self.log.info("entering country")
        confrompage.get_country().send_keys("ind")
        self.verify_link_present("India")
        confrompage.select_country().click()
        confrompage.select_checkout2().click()
        sleep(1)
        confrompage.select_submit().click()
        sleep(1)
        message = confrompage.read_message().text
        self.log.info(message)
        assert "Success" in message






