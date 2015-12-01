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
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException 
from selenium.webdriver.support import expected_conditions as EC

from pages import pageobject

class BuildPage(pageobject.PageObject):
    _submit_button_locator = (by.By.CSS_SELECTOR, '.btn.btn-primary')
    _builds_button_locator = (by.By.LINK_TEXT, 'Builds')
    _new_button_locator = (by.By.LINK_TEXT, 'New')

    def __init__(self, driver, conf):
        """Constructor"""
        super(BuildPage, self).__init__(driver, conf)
        self._page_title = "Overcast Cloud"

    @property
    def submit_button(self):
        return self.driver.find_element(*self._submit_button_locator)
    
    @property
    def builds_button(self):
        return self.driver.find_element(*self._builds_button_locator)

    @property
    def new_button(self):
        return self.driver.find_element(*self._new_button_locator)

    def click_on_builds_button(self):
        try :
            if self.builds_button.is_displayed():
                self.builds_button.click()
                #print "builds button found"
        except NoSuchElementException:
            print "builds button not found" 

    def view_build_log(self):
        self.driver.refresh()
	print "refreshed once"
	wait = WebDriverWait(self.driver, 20)
	try:
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
            print "build element found"
	finally:
	    print "ok!"
        element = self.driver.find_element(by.By.TAG_NAME, "pre")
        assert "successful" in element.text
        print "present"
        self.driver.back()
