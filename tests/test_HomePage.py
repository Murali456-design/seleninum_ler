from time import sleep
from selenium.webdriver.support.select import Select
import pytest

from TestData.HomePageData import HomePageData
from pageObject.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):
    log = BaseClass.get_Logger(__name__)

    def test_form_submit(self, get_data):
        homepage = HomePage(self.launch)
        # log = get_full_data[1]
        # get_data = get_full_data[0]
        # log = self.get_Logger()
        self.log.info("Name => " + get_data['name'])
        homepage.name_text().send_keys(get_data['name'])
        self.log.info("Email => " + get_data['email'])
        homepage.email_text().send_keys(get_data['email'])
        homepage.select_checkbox1().click()
        self.log.info("Gender => " + get_data['gender'])
        self.select_by_visual_text(homepage.get_gender(), get_data['gender'])
        homepage.submit_button().click()
        alert_text = homepage.get_success_message().text
        # self.launch.find_element_by_css_selector("[name='name']").send_keys("Murali")
        # self.launch.find_element_by_name("email").send_keys("sai.murali16")
        # self.launch.find_element_by_id("exampleCheck1").click()
        # sel = Select(self.launch.find_element_by_id("exampleFormControlSelect1"))
        # sel.select_by_visible_text("Male")
        # self.launch.find_element_by_xpath("//input[@value='Submit']").click()
        #
        # alert_text = self.launch.find_element_by_css_selector("[class*='alert-success']").text
        # print(alert_text)
        sleep(2)
        self.log.info("Message => " + alert_text)
        assert "Success" in alert_text
        sleep(5)
        self.launch.refresh()

    @pytest.fixture(params=HomePageData.test_homepage_data)
    def get_data(self, request):
        # self.get_Logger()
        return request.param