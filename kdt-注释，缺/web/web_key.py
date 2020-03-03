from web.web_driver import Get_driver
from web.web_driver import Get_element
class key:

    def __init__(self):

        self.driver = Get_driver().webdriver()   #
        self.e = Get_element()

    def open(self,url):
        self.driver.get(url)

    def click(self,how,what):
        self.e.ele(how,what).click()

    def input(self,how,what,valu):
        self.e.ele(how,what).send_keys(valu)

    def check(self):
        pass

if __name__ == '__main__':
    k = key()