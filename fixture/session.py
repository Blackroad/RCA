import time

class SessionHelper:
    def __init__(self, app):
        self.app = app

    def login(self):
        #login to main dashboard
        credentials=self.app.config['web']
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_xpath("//div[@class='content-body aui-panel']//div[@class='field-group']/input[@id='login-form-username']").clear()
        wd.find_element_by_xpath("//div[@class='content-body aui-panel']//div[@class='field-group']/input[@id='login-form-username']").send_keys(credentials['login'])
        wd.find_element_by_xpath("//div[@class='content-body aui-panel']//div[@class='field-group']/input[@id='login-form-password']").clear()
        wd.find_element_by_xpath("//div[@class='content-body aui-panel']//div[@class='field-group']/input[@id='login-form-password']").send_keys(credentials['password'])
        wd.find_element_by_xpath("//div[@class='buttons-container form-footer']//input[@value='Log In']").click()
       # wd.find_element_by_name("WebLogin$Login").click()
        time.sleep(0.5)


    def login_to_MES(self):
        wd=self.app.wd
        credentials = self.app.config['mes']
        wd.find_element_by_xpath("//div[@class='field-group']/input[@id='mes-login']").clear()
        wd.find_element_by_xpath("//div[@class='field-group']/input[@id='mes-login']").send_keys(credentials['dom'] + "\\" + credentials['login'])
        wd.find_element_by_xpath("//div[@class='field-group']/input[@id='mes-password']").clear()
        wd.find_element_by_xpath("//div[@class='field-group']/input[@id='mes-password']").send_keys(credentials['password'])
        wd.find_element_by_xpath("//div[@class='dialog-button-panel']/button[1]").click()
        time.sleep(2)



    def logout(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Logout").click()

    def is_logged_in_as(self, username):
        wd = self.app.wd
        return self.get_logged_user() == username


    def ensure_logout(self):
        if self.is_logged_in():
            self.logout()

    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements_by_link_text("Logout")) > 0

    def get_logged_user(self):
        wd = self.app.wd
        return wd.find_element_by_xpath("//*[@class='pull-left name']/label").text

    def ensure_login(self, username, password):
        wd = self.app.wd
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)




