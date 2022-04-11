import time
from selenium import webdriver
from selenium.webdriver.chrome import service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import datetime

t=datetime.datetime.now()
timex=t.strftime('%Y-%m-%d')
laptop_list = []

# initialize webdriver

website = 'https://www.emag.ro/'
class Emag_bot(webdriver.Chrome):

    def __init__(self, drive_path=service.Service("C:\SeleniumDrivers\chromedriver.exe"), teardown=False):
        self.driver_path = drive_path
        self.teardown = teardown
        options = Options()
        s = service.Service('C:\SeleniumDrivers\chromedriver.exe')
        super(Emag_bot, self).__init__(service=s, options=options)
        self.implicitly_wait(1)
        self.maximize_window()
        self.get('https://www.emag.ro/')
        self.implicitly_wait(2)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def sel_laptop(self):
        time.sleep(3)
        try:
            gdpr = self.find_element(By.XPATH, '//button[text()="Accept"]')
            gdpr.click()
            time.sleep(2)
            xclose = self.find_element(By.CSS_SELECTOR,
                                       'body > div.gdpr-cookie-banner.js-gdpr-cookie-banner.pad-sep-xs.pad-hrz-none.login-view.login-view-ro.show > div > button > i')
            xclose.click()
        except:
            pass
        x2close = self.find_element(By.CSS_SELECTOR, 'body > div.ns-wrap-bottom-right > div > div > button > i')
        x2close.click()
        time.sleep(2)
        laptop = self.find_element(By.PARTIAL_LINK_TEXT, ("Laptop, Tablete & Telefoane"))
        laptop.click()
        time.sleep(2)
        laptops = self.find_element(By.PARTIAL_LINK_TEXT, ("Laptopuri si accesorii"))
        laptops.click()
        time.sleep(2)
        laptops2 = self.find_element(By.XPATH,'//a[@href="'+"/laptopuri/c?tree_ref=2172&ref=cat_tree_91"+'"]')
        laptops2.click()

    def filtre(self):
        price_order = self.find_element(By.XPATH, "//div[contains(@class, 'sort-control-btn-dropdown hidden-xs')]")
        price_order.click()
        time.sleep(2)
        price_inc = self.find_element(By.XPATH, '//a[@data-sort-dir="asc"]')
        price_inc.click()
        time.sleep(2)
        stoc = self.find_element(By.XPATH, "//a[@data-name ='In Stoc']")
        stoc.click()
        time.sleep(2)
        # pret = self.find_element(By.XPATH,"//a[@data-option-id ='4000-5000']")
        # pret.click()
        time.sleep(2)
        price_min = self.find_element(By.XPATH,'// *[ @ id = "js-filter-6411-collapse"] / div[2] / div[2] / div[2] / input[1]')
        price_min.clear()
        price_min.send_keys(3900)
        price_max = self.find_element(By.XPATH,'// *[ @ id = "js-filter-6411-collapse"] / div[2] / div[2] / div[2] / input[2]')
        price_max.clear()
        price_max.send_keys(6000)
        button_price = self.find_element(By.XPATH,'//*[@id="js-filter-6411-collapse"]/div[2]/div[2]/div[2]/span/button/i')
        button_price.click()
        time.sleep(2)
        brand = self.find_element(By.XPATH, "//a[@data-name ='ASUS']")
        brand.click()
        time.sleep(2)
        gaming = self.find_element(By.XPATH, "//a[@data-name ='Gaming']")
        gaming.click()
        time.sleep(2)
        procesor = self.find_element(By.XPATH, "//a[@data-name = 'Intel® Core™ i7']")
        procesor.click()
        time.sleep(2)
        placa_video = self.find_element(By.XPATH, "//a[@data-name = 'Dedicata']")
        placa_video.click()
        time.sleep(2)
        diagonala = self.find_element(By.XPATH, "//a[@data-name = 'Peste 15.6']")
        diagonala.click()
        time.sleep(2)
        try:
            up = self.find_element(By.CSS_SELECTOR,'#main-container > section.page-section.page-listing-v2 > div > div.sticky-button-container > div > p')
            up.click()
            self.execute_script('window.scrollBy(0,0)')
        except:
            self.execute_script('window.scrollBy(0,0)')
        time.sleep(5)
        self.execute_script('window.scrollBy(0,400)')
        time.sleep(2)
        self.get_screenshot_as_file('laptop'+timex+'.png')

    def report_laptop(self):
        global pd
        time.sleep(2)
        laptop_boxes = self.find_elements(By.CSS_SELECTOR, '#card_grid > div')

        for laptop in laptop_boxes[0:4]:
            time.sleep(2)
            model_laptop = laptop.find_element(By.CLASS_NAME, "pad-hrz-xs")
            time.sleep(2)
            price_laptop = laptop.find_element(By.CLASS_NAME, 'product-new-price')
            lap_dict = {
                'title': model_laptop.text,
                'price': price_laptop.text
            }
            laptop_list.append(lap_dict)


















