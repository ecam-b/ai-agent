import pytest
from pages.signup_page import SignupPage

class TestSignup:
    @pytest.mark.signup
    @pytest.mark.login
    def test_login_user_with_correct_email_and_password(self, driver):
        signup = SignupPage(driver)

        # Paso 1-2: Abrir página principal
        signup.open_url('http://automationexercise.com')

        # Paso 3: Verificar home page
        assert 'Automation Exercise' in driver.title

        # Paso 4: Click en 'Signup / Login'
        signup.go_to_signup()

        # Paso 5: Verificar 'Login to your account' visible
        assert signup.is_login_to_account_visible()

        # Paso 6-7: Ingresar email y password correctos y hacer login
        signup.login('ecam-b101@gmail.com', 'testing123')

        # Paso 8: Verificar 'Logged in as username' visible
        assert signup.is_logged_in_as_visible()

        # Paso 9: Click en 'Delete Account' button
        signup.click_delete_account()

        # Paso 10: Verificar 'ACCOUNT DELETED!' visible
        assert signup.is_account_deleted_visible()


    @pytest.mark.signup
    def test_positive_signup(self, driver):
        signup = SignupPage(driver)

        # Paso 1-2: Abrir página principal
        signup.open_url('http://automationexercise.com')

        # Paso 3: Verificar home page
        assert 'Automation Exercise' in driver.title

        # Paso 4: Click en 'Signup / Login'
        signup.go_to_signup()

        # Paso 5: Verificar 'New User Signup!'
        assert signup.is_new_user_signup_visible()

        # Paso 6: Ingresar nombre y email
        name = 'TestUser'
        email = 'testuser{}@mail.com'.format(driver.session_id[-6:])
        signup.enter_name_email(name, email)

        # Paso 7: Click en 'Signup'
        signup.click_signup()

        # Paso 8: Verificar 'ENTER ACCOUNT INFORMATION'
        assert signup.is_enter_account_info_visible()

        # Paso 9: Llenar datos
        signup.fill_account_info('TestPass123', '1', 'January', '2000')

        # Paso 10 y 11: Seleccionar checkboxes
        signup.select_newsletter()
        signup.select_offers()

        # Paso 12: Llenar dirección
        signup.fill_address('Test', 'User', 'TestCompany', 'Test Address 1', 'Test Address 2', 'Canada', 'TestState', 'TestCity', '12345', '1234567890')

        # Paso 13: Click en 'Create Account'
        signup.click_create_account()

        # Paso 14: Verificar 'ACCOUNT CREATED!'
        assert signup.is_account_created_visible()

        # Paso 15: Click en 'Continue'
        signup.click_continue()

        # Paso 16: Verificar 'Logged in as username'
        assert signup.is_logged_in_as_visible(name)

        # Paso 17: Click en 'Delete Account'
        signup.click_delete_account()

        # Paso 18: Verificar 'ACCOUNT DELETED!' y click en 'Continue'
        assert signup.is_account_deleted_visible()
        signup.click_continue()
