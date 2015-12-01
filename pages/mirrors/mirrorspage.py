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
from selenium.common.exceptions import NoSuchElementException
from pages import pageobject

class MirrorPage(pageobject.PageObject):
    _url_locator = (by.By.ID, 'id_url')
    _series_locator = (by.By.ID, 'id_series')
    _components_locator = (by.By.ID, 'id_components')
    _public_checkbox_locator = (by.By.ID, 'id_public')
    _submit_button_locator = (by.By.CSS_SELECTOR, '.btn.btn-primary')
    _mirrors_button_locator = (by.By.LINK_TEXT, 'Mirrors')
    _new_button_locator = (by.By.LINK_TEXT, 'New')
    _delete_button_locator = (by.By.CSS_SELECTOR, '.btn.btn-danger')

    def __init__(self, driver, conf):
        """Constructor"""
        super(MirrorPage, self).__init__(driver, conf)
        self._page_title = "Overcast Cloud"

    @property
    def url(self):
        return self.driver.find_element(*self._url_locator)

    @property
    def series(self):
        return self.driver.find_element(*self._series_locator)

    @property
    def components(self):
        return self.driver.find_element(*self._components_locator)

    @property
    def submit_button(self):
        return self.driver.find_element(*self._submit_button_locator)

    @property
    def mirrors_button(self):
        return self.driver.find_element(*self._mirrors_button_locator)

    @property
    def new_button(self):
        return self.driver.find_element(*self._new_button_locator)

    @property
    def delete_button(self):
        return self.driver.find_element(*self._delete_button_locator)

    @property
    def public_checkbox(self):
        return self.driver.find_element(*self._public_checkbox_locator)

    def click_on_mirrors_button(self):
        try:
            if self.mirrors_button.is_displayed():
                self.mirrors_button.click()
                print "mirror button found"
        except NoSuchElementException:
            print "mirror button not found"

    def delete_mirror(self):
        follow_buttons = self.driver.find_elements_by_xpath(
                  '//table[@class="table table-striped"]/tbody/tr[1]/td[1]/a')
        follow_buttons[0].click()
        self.delete_button.click()
        print "deleted mirror"

    def create_new_mirror(self):
        self.new_button.click()
        url = self.conf.mirrors.url
        series = self.conf.mirrors.series
        components = self.conf.mirrors.components
        self.url.send_keys(url)
        self.series.send_keys(series)
        self.components.send_keys(components)
        self.public_checkbox.click()
        self.submit_button.click()
        print "created a new mirror"
