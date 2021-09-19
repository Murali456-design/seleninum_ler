import inspect
import pytest
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class BaseClass:
    def verify_link_present(self, text):
        WebDriverWait(self.launch, 10).until(EC.presence_of_element_located((By.LINK_TEXT, text)))

    @staticmethod
    def get_Logger(filename):
        filename = filename + ".txt" if ".txt" not in filename else filename
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler(filename)
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s",
                                      datefmt="%a %b %d %H:%M:%S %Y")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)  # filehandler object
        logger.setLevel(logging.DEBUG)
        # return logger
        return logger
    #
    # def print_debug(self, message):
    #     self.log.debug(message)
    #
    # def print_info(self, message):
    #     self.log.info(message)
    #
    # def print_warning(self, message):
    #     self.log.warning(message)
    #
    # def print_error(self, message):
    #     self.log.error(message)
    #
    # def print_critical(self, message):
    #     self.log.critical(message)



    def select_by_visual_text(self, locator, text):
        Select(locator).select_by_visible_text(text)

