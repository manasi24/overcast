#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from selenium.webdriver.common import by
from selenium.webdriver.common import keys
import sys
import pageobject
import time

class LoginPage(pageobject.PageObject):
    _login_username_field_locator = (by.By.ID, 'login_field')
    _login_password_field_locator = (by.By.ID, 'password')
    _login_submit_button_locator = (by.By.CSS_SELECTOR,
                                    '.btn.btn-primary.btn-lg')
    _sign_in_button_locator = (by.By.NAME,'commit')
    _logout_locator = (by.By.LINK_TEXT, 'Log out')

    def __init__(self, driver, conf):
        super(LoginPage, self).__init__(driver, conf)
        self.login_url = self.conf.dashboard.login_url
        self._page_title = "Login"

    def is_login_page(self):
        return (self.is_the_current_page() and
                self._is_element_visible(*self._login_submit_button_locator))

    @property
    def username(self):
        return self.driver.find_element(*self._login_username_field_locator)

    @property
    def password(self):
        return self.driver.find_element(*self._login_password_field_locator)

    @property
    def login_button(self):
        return self.driver.find_element(*self._login_submit_button_locator)

    @property 
    def sign_in_button(self):
        return self.driver.find_element(*self._sign_in_button_locator)

    @property
    def logout_button(self):
        return self.driver.find_element(*self._logout_locator)        

    def _click_on_login_button(self):
        self.login_button.click()

    def _click_on_sign_in_button(self):
        self.sign_in_button.click()

    def _press_enter_on_login_button(self):
        self.login_button.send_keys(keys.Keys.RETURN)

    def login(self, user=None, password=None):
        return self.login_with_mouse_click(user, password)

    def login_with_mouse_click(self, user, password):
        return self._do_login(user, password, self._click_on_sign_in_button)

    def login_with_enter_key(self, user, password):
        return self._do_login(user, password,
                              self._press_enter_on_login_button)

    def _do_login(self, user, password, login_method):
            if password is None:
                password = self.conf.identity.password
            if user is None:
                user = self.conf.identity.username
            return self.login_as_user(user, password, login_method)

    def login_as_user(self, user, password, login_method):
        self.username.send_keys(user)
        self.password.send_keys(password)
        login_method()

    def login_submit(self):
       self._click_on_login_button()

    def sign_in(self):
       self._click_on_sign_in_button()
    
    def go_to_login_page(self):
       self.driver.get(self.login_url)
       self.login_submit()
    

    def _click_on_logout_button(self):
        self.logout_button.click()

    def log_out(self):
        self._click_on_logout_button()
        #return self.go_to_main_page()
       #self.is_the_current_page()
