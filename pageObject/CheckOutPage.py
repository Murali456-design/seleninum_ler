from selenium.webdriver.common.by import By
from pageObject.ConfromPage import ConfromPage


class CheckOutPage:
    def __init__(self, launch):
        self.launch = launch

    # self.launch.find_elements_by_xpath("//div[@class='card h-100']")
    cart_title = (By.XPATH, "//div[@class='card h-100']/div/h4/a")
    # product.find_element_by_xpath("div/button").click()
    card_footer = (By.CSS_SELECTOR, ".card-footer button")
    # self.launch.find_element_by_css_selector("a[class*='btn-primary']").click()
    checkout_primary = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    checkout_submit = (By.CSS_SELECTOR, "button[class*='btn-success']")

    def get_cart_titles(self):
        return self.launch.find_elements(*CheckOutPage.cart_title)

    def get_cart_footer(self):
        return self.launch.find_elements(*CheckOutPage.card_footer)

    def get_checkout_primary(self):
        return self.launch.find_element(*CheckOutPage.checkout_primary)

    def get_checkout_submit(self):
        self.launch.find_element(*CheckOutPage.checkout_submit).click()
        return ConfromPage(self.launch)