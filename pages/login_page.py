from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from pages.base_page import BasePage

class LoginPage(BasePage):
    __url = 'https://automationexercise.com/login'
    __email_field = (By.NAME, 'email')
    __password_field = (By.NAME, 'password')
    __login_btn = (By.XPATH, "//button[contains(text(),'Login') or contains(text(),'login')]")
    __logout_link = (By.LINK_TEXT, 'Logout')
    __logged_in_as = (By.PARTIAL_LINK_TEXT, 'Logged in as')

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        self.open_url(self.__url)

    def set_email(self, email):
        self._type(self.__email_field, email)

    def set_password(self, password):
        self._type(self.__password_field, password)

    def submit(self):
        self._click(self.__login_btn)

    def logout(self):
        self._click(self.__logout_link)

    def is_logged_in(self):
        return self._is_displayed(self.__logged_in_as)
