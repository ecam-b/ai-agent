from selenium.webdriver.common.by import By
from pages.base_page import BasePage

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from pages.base_page import BasePage

class SignupPage(BasePage):
    def login(self, email, password):
        self._type(self.__email_field, email)
        self._type(self.__password_field, password)
        self._click(self.__submit_button)

    def is_login_to_account_visible(self):
        return self._is_displayed((By.XPATH, "//h2[text()='Login to your account']"))
    __url = "https://automationexercise.com/login"
    __name_field = (By.CSS_SELECTOR, 'input[data-qa="signup-name"]')
    __email_field = (By.CSS_SELECTOR, 'input[data-qa="signup-email"]')
    __submit_button = (By.CSS_SELECTOR, 'button[data-qa="signup-button"]')
    __signup_login_btn = (By.LINK_TEXT, 'Signup / Login')
    __new_user_signup = (By.XPATH, "//h2[text()='New User Signup!']")
    __enter_account_info = (By.XPATH, "//b[text()='Enter Account Information']")
    __gender_radio = (By.ID, 'id_gender1')
    __password_field = (By.ID, 'password')
    __days_field = (By.ID, 'days')
    __months_field = (By.ID, 'months')
    __years_field = (By.ID, 'years')
    __newsletter_checkbox = (By.ID, 'newsletter')
    __offers_checkbox = (By.ID, 'optin')
    __first_name = (By.ID, 'first_name')
    __last_name = (By.ID, 'last_name')
    __company = (By.ID, 'company')
    __address1 = (By.ID, 'address1')
    __address2 = (By.ID, 'address2')
    __country = (By.ID, 'country')
    __state = (By.ID, 'state')
    __city = (By.ID, 'city')
    __zipcode = (By.ID, 'zipcode')
    __mobile_number = (By.ID, 'mobile_number')
    __create_account_btn = (By.XPATH, "//button[text()='Create Account']")
    __account_created = (By.XPATH, "//b[text()='Account Created!']")
    __continue_btn = (By.XPATH, "//a[text()='Continue']")
    __delete_account_btn = (By.PARTIAL_LINK_TEXT, "Delete Account")
    __account_deleted = (By.XPATH, "//b[text()='Account Deleted!']")
    __logged_in_as_partial = (By.PARTIAL_LINK_TEXT, 'Logged in as')

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def go_to_signup(self):
        self._click(self.__signup_login_btn)

    def is_new_user_signup_visible(self):
        return self._is_displayed(self.__new_user_signup)

    def enter_name_email(self, name, email):
        self._type(self.__name_field, name)
        self._type(self.__email_field, email)

    def click_signup(self):
        self._click(self.__submit_button)

    def is_enter_account_info_visible(self):
        return self._is_displayed(self.__enter_account_info)

    def fill_account_info(self, password, day, month, year):
        self._click(self.__gender_radio)
        self._type(self.__password_field, password)
        self._type(self.__days_field, day)
        self._type(self.__months_field, month)
        self._type(self.__years_field, year)

    def select_newsletter(self):
        self._click(self.__newsletter_checkbox)

    def select_offers(self):
        self._click(self.__offers_checkbox)

    def fill_address(self, first, last, company, address1, address2, country, state, city, zipcode, mobile):
        self._type(self.__first_name, first)
        self._type(self.__last_name, last)
        self._type(self.__company, company)
        self._type(self.__address1, address1)
        self._type(self.__address2, address2)
        self._type(self.__country, country)
        self._type(self.__state, state)
        self._type(self.__city, city)
        self._type(self.__zipcode, zipcode)
        self._type(self.__mobile_number, mobile)

    def click_create_account(self):
        self._click(self.__create_account_btn)

    def is_account_created_visible(self):
        return self._is_displayed(self.__account_created)

    def click_continue(self):
        self._click(self.__continue_btn)

    def is_logged_in_as_visible(self, username=None):
        return self._is_displayed(self.__logged_in_as_partial)

    def click_delete_account(self):
        self._click(self.__delete_account_btn)

    def is_account_deleted_visible(self):
        return self._is_displayed(self.__account_deleted)
