from selenium.webdriver.common.by import By
from pageObject.CheckOutPage import CheckOutPage


class HomePage:
    shop = (By.LINK_TEXT, "Shop")
    name = (By.CSS_SELECTOR, "[name='name']")
    email = (By.NAME, "email")
    checkbox1 = (By.ID, "exampleCheck1")
    gender = (By.ID, "exampleFormControlSelect1")
    submit = (By.XPATH, "//input[@value='Submit']")
    message = (By.CSS_SELECTOR, "[class*='alert-success']")

    # self.launch.find_element_by_css_selector("[name='name']").send_keys("Murali")
    # self.launch.find_element_by_name("email").send_keys("sai.murali16")
    # self.launch.find_element_by_id("exampleCheck1").click()
    # sel = Select(self.launch.find_element_by_id("exampleFormControlSelect1"))
    # sel.select_by_visible_text("Male")
    # self.launch.find_element_by_xpath("//input[@value='Submit']").click()
    # self.launch.find_element_by_css_selector("[class*='alert-success']").text
    def __init__(self, launch):
        self.launch = launch

    def name_text(self):
        return self.launch.find_element(*HomePage.name)

    def email_text(self):
        return self.launch.find_element(*HomePage.email)

    def select_checkbox1(self):
        return self.launch.find_element(*HomePage.checkbox1)

    def get_gender(self):
        return self.launch.find_element(*HomePage.gender)

    def submit_button(self):
        return self.launch.find_element(*HomePage.submit)

    def get_success_message(self):
        return self.launch.find_element(*HomePage.message)

    def shopIteam(self):
        self.launch.find_element(*HomePage.shop).click()
        return CheckOutPage(self.launch)

        # launch.find_element_by_link_text("Shop").click()