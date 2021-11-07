# standard
import os
import sys
import time
import platform
# selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Robot(object):
    def __init__(self, browser, drivers_path, delay):
        # get driver
        self._driver = self.driver(browser, drivers_path)
        # select option delay
        self._delay = delay

    @staticmethod
    def driver(browser, drivers_path):
        ops = 'windows' if sys.platform == 'win32' else 'linux'
        ext = '.exe' if sys.platform == 'win32' else ''
        arch = '64' if platform.machine().endswith('64') else '32'
        if browser == 'firefox':
            executable = os.path.join(drivers_path, 'firefox_{}_{}{}'.format(ops, arch, ext))
            driver = webdriver.Firefox(executable_path=executable)
        else:
            executable = os.path.join(drivers_path, 'chrome_{}{}'.format(ops, ext))
            options = Options()
            options.add_argument("--log-level=3")
            driver = webdriver.Chrome(executable_path=executable, options=options)
        return driver

    def _fill_input(self, name, value):
        elem = self._driver.find_element_by_name(name)
        elem.send_keys(value)

    def _set_option(self, name, value):
        elem = self._driver.find_element_by_name(name)
        for option in elem.find_elements_by_tag_name('option'):
            if option.text == value:
                option.click()
                break
        time.sleep(self._delay)

    def get(self, url):
        self._driver.get(url)

    def setupForm(self, data):
        inputs = {
            'first_name': data['nam'],
            'last_name': data['nam_khanevadegi'],
            'fathers_name': data['nam_pedar'],
            'national_code': data['cod_meli'],
            'identity_code': data['shomareh_shenasnameh'],
            'identity_serial': data['serial_shenasnameh'],
            'birth_date_dd': data['tavalod_rooz'],
            'birth_date_mm': data['tavalod_mah'],
            'birth_date_yy': data['tavalod_sal'],
            'issuance_date_dd': data['sodoor_rooz'],
            'issuance_date_mm': data['sodoor_mah'],
            'issuance_date_yy': data['sodoor_sal'],
            'street': data['address_khiaban_asli'],
            'bystreet': data['address_khiaban_farei'],
            'alley': data['address_kooche'],
            'no': data['address_pelak'],
            'postal_code': data['address_cod_posti'],
            'bank_name': data['nam_bank'],
            'sheba': data['shomareh_shaba'],
            'mobile_number': data['hamrah'],
            'phone_number': data['sabet'],
            'email': data['email'],
            'certificate_number': data['govahiname']
        }
        selects = {
            'issuance_place_province': data['mahal_sodoor_ostan'],
            'issuance_place_city': data['mahal_sodoor_shahr'],
            'birth_place_province': data['mahal_tavalod_ostan'],
            'birth_place_city': data['mahal_tavalod_shahr'],
            'sex': data['jensiat'],
            'occupation': data['shoghl'],
            'ashnaei': data['ashnayi'],
            'carPlaque': data['noe_pelak'],
            'address_province': data['address_ostan'],
            'address_city': data['address_shahr']
        }
        for name, value in inputs.items():
            self._fill_input(name, value)

        for name, value in selects.items():
            self._set_option(name, value)
