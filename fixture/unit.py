from PIL import Image, ImageGrab
import string
import time
import random


class UnitHelper:
    def __init__(self,app):
        self.app = app



    def find_units(self,action):
        wd = self.app.wd
        unit_serials = self.app.config['jira']
        wd.find_element_by_xpath("//div[@class='tabs-pane active-pane']/div[@id='unitserials']/textarea").send_keys(unit_serials['unitserials'])
        wd.find_element_by_xpath("//div[@class='tabs-pane active-pane']/div[@id='unitserials']/div[@class='buttons']/input[@id='unit-serial-search'] ").click()
        time.sleep(2)
        self.app.session.login_to_MES()
        if self.element_presented("//button[@id='ok_button_only']"):
            wd.find_element_by_xpath("//button[@id='ok_button_only']").click()
        else:
            pass
        time.sleep(4)
        self.get_MES_serial_list()
        wd.find_element_by_xpath("//div[@id='rca-left']/ul[@class='tabs-menu']/li[@class='menu-item']/a[@href='#tab-unit-details']").click()
        self.app.wait("//div[@class='tabs-pane with-rca-inputs active-pane']")
        self.open_random_MES(action)
        time.sleep(2)


    #gather all units from MES list
    def get_MES_serial_list(self):
        wd = self.app.wd
        MES_list=[]
        list = wd.find_elements_by_xpath("//table[@id='failureEventsTable']//tr/td[3]")
        for element in list:
            unit_name = element.text
            MES_list.append(unit_name)
        return MES_list

    def open_random_MES(self,action):
        wd = self.app.wd
        list = self.get_MES_serial_list()
        while self.open_disposition_window(action,list)!= True:
            if len(list)!= 0:
                continue
            else:
                print ('No elements in list of units with action = %s' % action)
        else:
            wd.find_element_by_xpath("//select[@id='select-dc']").click()
            wd.find_element_by_xpath("//select[@id='select-dc']/option[@data-action='%s']" % value).click()



    def open_disposition_window(self,action,list):
        random_serial = random.choice(list)
        self.select_disposition(list, random_serial)
        self.app.wait("//select[@id='select-dc']/option[text()]")
        if self.find_action_value(action):
            return True
        list.remove(random_serial)

    def select_disposition(self, list, random_serial):
        wd=self.app.wd
        wd.find_element_by_xpath("//table[@id='failureEventsTable']/tbody/tr/td[text()='%s']" % random_serial).click()
        while self.element_presented("//div[@id='tab-unit-details']//input[@id='select-disposition-button' and @style = 'display: inline-block;']") == False:
            random_serial = random.choice(list)
            wd.find_element_by_xpath("//table[@id='failureEventsTable']/tbody/tr/td[text()='%s']" % random_serial).click()
        else:
            wd.find_element_by_xpath("//div[@id='tab-unit-details']//input[@id='select-disposition-button' and @value = 'Select Disposition']").click()


    def find_action_value(self,action):
        global value
        wd = self.app.wd
        get_action_list = wd.find_elements_by_xpath("//table[@id='disp-options']/tbody/tr[1]/td[1]/select/option")
        for element in (get_action_list):
            value = element.get_attribute("data-action")
            if value == action:
                return True
            else:
                continue
        wd.find_element_by_xpath("//div[@class='buttonPanel']/button[@class='cancel_button aui-button rca-popup-button']").click()
        self.app.wait("//table[@id='failureEventsTable']")
        return False

    def get_unit_list(self):
        units = self.app.config['jira']['unitserials']
        units = units.split()
        return units

    def random_string(self, prefix, maxlen, digits=None):

        if digits != None:
            digits = string.digits
            return prefix + "".join([random.choice(digits) for i in range(random.randrange(maxlen))])
        else:
            all = string.ascii_letters + string.digits + string.punctuation
            return prefix + "".join([random.choice(all) for i in range(random.randrange(maxlen))])

    def take_screenshot(self,screen_name):
        screen = ImageGrab.grab()
        name = self.random_string(screen_name,3,1) + '.png'
        screen.save(name,'PNG')


    def submit_unit(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@class='buttonPanel']/button[@id='ok_button']").click()
        time.sleep(2)



    def element_presented(self,elem_xpath):
        wd=self.app.wd
        if len (wd.find_elements_by_xpath("%s" % elem_xpath)) > 0:
            return True
        return False

    def open_event_details(self):
        wd=self.app.wd
        wd.find_element_by_xpath("//div[@id='select-dispositionMsgContainer']/a[@id='popup-summary']").click()
        time.sleep(2)
        wd.switch_to_window(wd.window_handles[-1])
        self.app.wait("//li[@class='item item-right']")


    def unit_status(self,status):
        wd = self.app.wd
        current_status = wd.find_element_by_xpath("//span[@id='status-val']/img").get_attribute('title')
        if current_status == status:
            return True
        else:
            return False


    def assignee_field(self):
        wd = self.app.wd
        user_info = wd.find_elements_by_xpath("//span[@id='assignee-val']/span[1]")
        for element in user_info:
            username=element.text
            return username



    def user_id(self):
        wd = self.app.wd
        user_id = ((wd.find_element_by_xpath("//div[@id='e-sign']").text).strip()).split()
        user_id = user_id[2] + ' ' + user_id[3]
        return user_id


    def text_presented(self, text):
        wd = self.app.wd
        element = wd.find_element_by_xpath("//div[@id='e-sign']").text
        if text == element:
            return True
        return False


    def Rwk_submit_with_workpath(self, work_path):
        wd=self.app.wd
        wd.find_element_by_xpath("//select[@id='select-disp-act']").click()
        wd.find_element_by_xpath("//select[@id='select-disp-act']/option[@value = '%s']" % work_path).click()
        self.submit_unit()
        time.sleep(2)
        assert self.submit_without_fail()==True
        self.take_screenshot('Rework_submit')
        if work_path  == 'RwkNCP':
            wd.find_element_by_xpath("//div[@class='buttonPanel']/button[@data-event='rca-popup-cancel'and text()='Close']").click()
        else:
            pass


    def submit_without_fail(self):
        wd = self.app.wd
        result=[]
        fails = wd.find_elements_by_xpath("//table[@id='disp-result']/tbody//td[2]")
        for element in fails:
            result.append(element.text)
        if 'fail' in result:
            return False
        else:
            return True

    def release_from_NCP(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//div/input[@id='release-from-ncp-button' and @value='Release from NCP']").click()
        self.app.wait("//input[@id='select-disposition-button' and @style='display: inline-block;']")




    def unit_serial_step_name(self,step_name):
        wd = self.app.wd
        actual_step_name = wd.find_element_by_xpath("//table[@id='configurable-unit-detail-items']//tr[3]/td").text
        if step_name == actual_step_name:
            return True
        else:
            return False


    def contol_is_enable(self,control_id):
        wd = self.app.wd
        if wd.find_element_by_xpath("//input[@id='%s']" %control_id).get_attribute('disable')==True:
            return False
        else:
            return True















