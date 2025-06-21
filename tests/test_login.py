import pytest
from pages.login_page import LoginPage

@pytest.mark.debug
class TestLoginScenario:
    @pytest.mark.debug
    def test_login_logout(self, driver):
        login = LoginPage(driver)
        login.open()
        login.set_email('ecam-b101@gmail.com')
        login.set_password('testing123')
        login.submit()
        assert login.is_logged_in(), "No se encontró el link 'Logged in as' tras login."
        login.logout()
        assert login.current_url == 'https://automationexercise.com/login', f"No regresó al login, url actual: {login.current_url}"
