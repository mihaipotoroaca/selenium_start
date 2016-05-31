import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:

    _IMPLICIT_WAIT = 20

    def __init__(self, selenium, variables, open_url=False):
        self.selenium = selenium
        self.variables = variables
        if open_url:
            self.selenium.get(self.variables['url'])
        self.confirm_page_load()
        time.sleep(3)  # just for demo purposes

    def confirm_page_load(self):
        pass

    def is_visible(self, selector):
        element = WebDriverWait(self.selenium, self._IMPLICIT_WAIT).until(
            EC.visibility_of_element_located(
                selector
            )
        )
        return element

    def get_element(self, selector):
        element = WebDriverWait(self.selenium, self._IMPLICIT_WAIT).until(
            EC.presence_of_element_located(
                selector
            )
        )
        return element

    def get_elements(self, selector):
        elements = WebDriverWait(self.selenium, self._IMPLICIT_WAIT).until(
            EC.presence_of_all_elements_located(
                selector
            )
        )
        return elements

    def enter_text(self, selector, text):
        element = self.is_visible(selector)
        element.click()
        element.clear()
        element.send_keys(text)

    def click(self, selector):
        element = WebDriverWait(self.selenium, self._IMPLICIT_WAIT).until(
            EC.element_to_be_clickable(
                selector
            )
        )
        element.click()

    def check_clickable(self, selector):
        WebDriverWait(self.selenium, self._IMPLICIT_WAIT).until(
            EC.element_to_be_clickable(
                selector
            )
        )

    def select_text_from_dropdown(self, selector, value):
        dropdown = WebDriverWait(
                self.selenium, self._IMPLICIT_WAIT
        ).until(EC.visibility_of_element_located(selector))
        Select(dropdown).select_by_value(value)