import time

import pytest
from selenium import webdriver

from config.loadyaml import loadyaml


class TestCase:
    def setup(self):
        self.driver=webdriver.Chrome()
        self.driver.get('http://39.98.138.157/shopxo/index.php?s=/index/user/Logininfo.html')

    def teardown(self):
        time.sleep(2)
        self.driver.quit()

    # def test_01LoginSucess(self):
    #     self.driver.find_element_by_name('accounts').send_keys('qiushui')
    #     self.driver.find_element_by_name('pwd').send_keys('123456')
        # self.driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[2]/form/div[3]/button').submit()
    @pytest.mark.parametrize('udata',loadyaml('./data/login.yaml'))
    def test_02(self,udata):
        self.driver.find_element_by_name('accounts').send_keys(udata['uname'])
        self.driver.find_element_by_name('pwd').send_keys(udata['upas'])
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[2]/form/div[3]/button').submit()

if __name__ == '__main__':
    pytest.main(['-vs','py_test.py'])