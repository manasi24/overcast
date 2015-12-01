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
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from pages import pageobject

class SourcePage(pageobject.PageObject):
    _giturl_locator = (by.By.ID, 'id_git_url')
    _branch_locator = (by.By.ID, 'id_branch')
    _submit_button_locator = (by.By.CSS_SELECTOR, '.btn.btn-primary')
    _sources_button_locator = (by.By.LINK_TEXT, 'Sources')
    _new_button_locator = (by.By.LINK_TEXT, 'New')
    _dropdown_menu_locator = (by.By.ID, 'id_series')
    _delete_button_locator = (by.By.CSS_SELECTOR, '.btn.btn-danger')

    def __init__(self, driver, conf):
        """Constructor"""
        super(SourcePage, self).__init__(driver, conf)
        self._page_title = "Overcast Cloud"

    @property
    def git_url(self):
        return self.driver.find_element(*self._giturl_locator)

    @property
    def branch(self):
        return self.driver.find_element(*self._branch_locator)

    @property
    def submit_button(self):
        return self.driver.find_element(*self._submit_button_locator)

    @property
    def sources_button(self):
        return self.driver.find_element(*self._sources_button_locator)

    @property
    def new_button(self):
        return self.driver.find_element(*self._new_button_locator)

    @property
    def delete_button(self):
        return self.driver.find_element(*self._delete_button_locator)

    @property
    def dropdown_menu(self):
        return self.driver.find_element(*self._dropdown_menu_locator)

    def click_on_sources_button(self):
        try:
            if self.sources_button.is_displayed():
                self.sources_button.click()
        except NoSuchElementException:
            print "source button not found"

    def click_on_dropdown_menu(self):
        dropdown = Select(self.driver.find_element_by_id("id_series"))
        dropdown.select_by_visible_text("manasishah24/aasemble")

    def delete_package_source(self):
        follow_buttons = self.driver.find_elements_by_xpath(
                         '//small/a/span[@class="glyphicon glyphicon-pencil"]')
        follow_buttons[0].click()
        self.delete_button.click()
        print "source deleted"

    def create_new_package_source(self):
        self.new_button.click()
        git_url = self.conf.sources.git_url
        branch = self.conf.sources.branch
        self.git_url.send_keys(git_url)
        self.branch.send_keys(branch)
        self.click_on_dropdown_menu()
        self.submit_button.click()
        print "new package source created"
