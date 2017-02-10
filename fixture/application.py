from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from fixture.session import SessionHelper

from fixture.unit import UnitHelper



class Application:

    def __init__(self, browser, config):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument("--start-maximized")
            self.wd = webdriver.Chrome(chrome_options=options)
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)

        self.session = SessionHelper(self)
        self.unit = UnitHelper(self)
        self.config = config
        self.base_url = config['jira']['baseURL']

    def wait(self,element):
        wd = self.wd
        wait = WebDriverWait(wd, 20)
        wait.until(EC.element_to_be_clickable((By.XPATH,"%s" % element)))


    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url)


    def destroy(self):
        self.wd.quit()

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False



