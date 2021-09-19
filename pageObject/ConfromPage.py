from selenium.webdriver.common.by import By


class ConfromPage:
    id_country = (By.ID, "country")
    link_country = (By.LINK_TEXT, "India")
    checkout2 = (By.CSS_SELECTOR, "label[for='checkbox2']")
    submit = (By.CSS_SELECTOR, "[type='submit']")
    message = (By.CSS_SELECTOR, "[class*='alert-succes']")

    def __init__(self,launch):
        self.launch = launch

    def get_country(self):
        return self.launch.find_element(*ConfromPage.id_country)

    def select_country(self):
        return self.launch.find_element(*ConfromPage.link_country)

    def select_checkout2(self):
        return self.launch.find_element(*ConfromPage.checkout2)

    def select_submit(self):
        return self.launch.find_element(*ConfromPage.submit)

    def read_message(self):
        return self.launch.find_element(*ConfromPage.message)