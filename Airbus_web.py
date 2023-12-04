import time
from unittest import TestCase
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

class airbuss_home_page(TestCase):
    def test_home_page(self):  # Before starting any test, Checking connection
        Airbus_web = driver.get("https://www.airbus.com/en")
        print(Airbus_web)
        driver.close()
        driver.quit()
        print("Clear for tasting")


    def test_way_to_commercial(self):
         Airbus_web = driver.get("https://www.airbus.com/en")
         menu = driver.find_element(By.CSS_SELECTOR, ".awx-switch-text.awx-menu-drawer-toggler__text")
         menu.click()
         product_and_service = driver.find_element(By.CSS_SELECTOR, "div[id='menu-407417332-toggler'] label[for='menu-407417332-state']")
         product_and_service.is_selected() # Because the "Product & Service" menu must be selected to perform for next menu
         commercial_aircrafth = driver.find_element(By.CSS_SELECTOR, "li[class='awx-menu-list__item awx-menu-list__item--level2 awx-menu"
         "-list__item--last-level'] a[title='Airbus’ diverse and innovative product"
         " line of aircraft includes everything from commercial jetliners"       # This is the long way to reach to next page
         " – such as the best-selling A320 – to freighters and private jets.']")
         commercial_aircrafth.is_selected()
         driver.maximize_window()
         time.sleep(5)
         driver.close()
         driver.quit()

class commercial_page(TestCase):
    commercial_page = driver.get("https://www.airbus.com/en/products-services/commercial-aircraft")
    def test_commercial_page(self):
        video_high_lights_2022 = driver.find_element(By.XPATH, "//div[@class='vjs-poster']")
        video_source = video_high_lights_2022.get_attribute("https://mediaassets.airbus.com/medias/domain38/media102015/604510-l7s59rqbs5-480.mp4")
        video_high_lights_2022.is_displayed()
        driver.maximize_window()
        time.sleep(5)
        video_high_lights_2022.is_enabled()
        current_time = driver.execute_script("return arguments[0].currentTime",video_high_lights_2022)
        driver.close()
        driver.quit()



class airbus_A320_page(TestCase): # What  the Buyer needs to explore for his company
    driver.get("https://www.airbus.com/en/products-services/commercial-aircraft/passenger-aircraft/a320-family")
    def test_A320_neo(self):
        download_link = driver.find_element(By.PARTIAL_LINK_TEXT, "Infographic A320neo Family")
        download_link.is_selected()

    def test_A321_XLR(self):
        download_link_321 = driver.find_element(By.PARTIAL_LINK_TEXT, "Infographic A321X")
        download_link_321.is_selected()
        driver.close()
        driver.quit()

    # function ".click" isn't working, So I don't know if it will download
















