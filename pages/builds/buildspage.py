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

import sys
import time
from selenium.webdriver.common import by
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
#import selenium.common.exceptions as Exceptions
from selenium.common.exceptions import NoSuchElementException 
from selenium.webdriver.common import keys
from selenium.webdriver.support import expected_conditions as EC

from pages import pageobject

class BuildPage(pageobject.PageObject):
#    _giturl_locator = (by.By.ID, 'id_git_url')
#    _branch_locator = (by.By.ID, 'id_branch')
    _submit_button_locator = (by.By.CSS_SELECTOR, '.btn.btn-primary')
    _builds_button_locator = (by.By.LINK_TEXT, 'Builds')
    #_new_button_locator = (by.By.LINK_TEXT, 'New')
    _new_button_locator = (by.By.CSS_SELECTOR, '.btn.btn-primary')
#    _login_submit_button_locator = (by.By.NAME, 'commit')
    #_dropdown_menu_locator = (by.By.XPATH, './/select[@id='"id_series"']/option[@value='"38"']')
    #_dropdown_menu_locator = (by.By.CSS_SELECTOR, "select#id_series > option[value='38']")
    #_dropdown_menu_locator = (by.By.XPATH, '//select[@id='"id_series"']/option[text()='"manasishah24/aasemble"']')
    _dropdown_menu_locator = (by.By.ID, 'id_series')

    def __init__(self, driver, conf):
        """Constructor"""
        super(BuildPage, self).__init__(driver, conf)
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
    def builds_button(self):
        return self.driver.find_element(*self._builds_button_locator)

    @property
    def new_button(self):
        return self.driver.find_element(*self._new_button_locator)

    @property
    def dropdown_menu(self):
        return self.driver.find_element(*self._dropdown_menu_locator)

    def click_on_builds_button(self):
        try :
            if self.builds_button.is_displayed():
                self.builds_button.click()
                #print "builds button found"
        except NoSuchElementException:
            print "builds button not found" 

    def click_on_new_button(self):
        self.new_button.click()

    def click_on_dropdown_menu(self):
        mySelect = Select(self.driver.find_element_by_id("id_series"))
        #mySelect.select_by_value("38")
        mySelect.select_by_visible_text("manasishah24/aasemble")
    
    def delete_package_source(self):
        follow_buttons = self.driver.find_elements_by_xpath('//small/a/span[@class="glyphicon glyphicon-pencil"]')
        follow_buttons[1].click()
        self.driver.find_element_by_css_selector(".btn.btn-danger").click()
        #print "deleted"
        
    def view_build_log(self):
        self.driver.refresh()
	print "refreshed once"
	wait = WebDriverWait(self.driver, 20)
	try:
            #self.driver.implicitly_wait(250)
	    print "now going to sleep for 300 seconds"
            time.sleep(300)
            print "now awake"
            print "now will refresh"
            self.driver.refresh()
	    print "refreshed twice"
	    element = wait.until(
	    EC.presence_of_element_located((by.By.XPATH, "//table/tbody/tr/td[5]/a"))
            )
	    element.click()
            print "element found"
	finally:
	    print "ok!"
        #self.driver.find_element(by.By.XPATH,"//table/tbody/tr/td[5]/a").click()
        element = self.driver.find_element(by.By.TAG_NAME, "pre")
        assert "successful" in element.text
        print "present"
        self.driver.back()
	#element = wait.until(EC.element_to_be_clickable((By.ID,'someid')))
	#self.driver.implicitly_wait(3000)
	#try:
	#    element = WebDriverWait(driver, 120).until(
        #    EC.presence_of_element_located((By.XPATH, "//table/tbody/tr/td[5]/a"))
    	#    )
    	#    element[1].click()
	#finally:
	#    print "ok"
        #build_logs = self.driver.find_elements_by_xpath('//table/tbody/tr/td[5]/a')
        #build_logs[1].click()

    def create_new_package_source(self):
        self.click_on_new_button()
        git_url = self.conf.sources.git_url
        branch = self.conf.sources.branch
        self.git_url.send_keys(git_url)
        self.branch.send_keys(branch)
        self.click_on_dropdown_menu()
        self.click_on_submit()
        #print "created"
        
    def click_on_submit(self):
        self.submit_button.click()
