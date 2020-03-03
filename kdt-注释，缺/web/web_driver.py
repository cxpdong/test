from selenium import webdriver

class Get_driver:
    # driver =None

    def __init__(self):
        pass
    @classmethod
    def webdriver(cls):
        cls.driver=webdriver.Firefox()
        return cls.driver

class Get_element:
    def __init__(self):
        self.driver = Get_driver().driver

    def ele(self,how,what):
        self.element=self.driver.find_element(how,what)
        return self.element


if __name__ == '__main__':
    driver = Get_driver().webdriver()






