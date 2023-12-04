import time
from unittest import TestCase
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
from selenium.webdriver.support.select import Select

class boeing_home_page(TestCase):
    def test_home_page(self): # Before starting any test, Checking connection
        Boeing_web = driver.get("https://www.boeing.com/")
        print(Boeing_web)
        print("Clear for tasting")
        driver.close()
        driver.quit()


    def test_link_Commercial(self):  # For understand customer view for a future orders
        driver.get("https://www.boeing.com/")
        commercial = driver.find_element(By.LINK_TEXT, "Commercial")
        commercial.click()
        time.sleep(3)
        driver.close()
        driver.quit()
        print('Link Commercial is connected as required')

class commercial_page(TestCase):
    driver.get("https://www.boeing.com/commercial/")
    def test_Commercial_images(self): # This website zone may be "heavy"

        driver.maximize_window()
        Next_Generation_737_Image = driver.find_element(By.CSS_SELECTOR,"img[alt='Picture of a Next-Generation 7 3 7 in flight with Boeing livery.']")
        Boeing_737_Max = driver.find_element(By.XPATH,"//img[@alt='Picture of a 7 3 7 MAX 10 in flight with Boeing livery.']")
        Boeing_747_800 = driver.find_element(By.XPATH,"//img[@alt='Picture of a 7 4 7 dash 8 in flight with Boeing livery.']")
        Boeing_767 = driver.find_element(By.XPATH, "//img[@alt='Picture of a 7 6 7 in flight with Boeing livery.']")
        Boeing_777 = driver.find_element(By.XPATH, "//img[@alt='Picture of a 7 7 7 in flight with Boeing livery.']")
        time.sleep(3) # For upload half images
        Boeing_777X = driver.find_element(By.XPATH, "//img[@alt='Picture of a 7 7 7 dash 9 in flight with Boeing livery.']")
        Boeing_787 = driver.find_element(By.XPATH, "//img[@alt='Picture of a 7 8 7 dash 10 in flight with Boeing livery.']")
        Freighter = driver.find_element(By.CSS_SELECTOR, "img[alt='Right side view of a 7 4 7 dash 8F in flight with Boeing livery.']")
        Boeing_support_and_service = driver.find_element(By.CSS_SELECTOR,"img[alt='Picture of an Boeing factory employee.']")
        Boeing_Business_Jets = driver.find_element(By.CSS_SELECTOR,"img[alt='Picture of a Boeing Business Jet in flight.']")
        time.sleep(5)
        driver.close()
        driver.quit()
        print('Images tests of the Commercial category is completed')

class sing_up(TestCase):
    def test_sign_up_link(self): # For getting more information Updates to future orders
        driver.get("https://www.boeing.com/")
        sing_up_link = driver.find_element(By.LINK_TEXT, "Sign Up")
        sing_up_link.click()
        driver.close()
        driver.quit()

    def test_sing_up_menu(self): # Just to get access
        driver.get("https://www.boeing.com/manage/preference-center.page")
        email = driver.find_elements(By.CSS_SELECTOR, '#EmailAddress')
        first_name = driver.find_elements(By.CSS_SELECTOR, '#FirstName')
        last_name = driver.find_elements(By.CSS_SELECTOR, '#LastName')
        city = driver.find_elements(By.CSS_SELECTOR, '#City')
        country = driver.find_elements(By.NAME, "Country")
        dropDown = Select(country)
        dropDown.select_by_value("Israel")
        Newsletters = driver.find_elements(By.XPATH,"//label[@for='CommercialAirplanes']//div[@class='newsletter-header']")  # To get newsletter of commercial airplanes
        Newsletters.click()
        sing_up_button = driver.find_elements(By.XPATH, "sing_up_button")
        sing_up_button.click()

    # In the future I will do it with different randomly details : Email, last name, first name, city
    # With more experience
        email.send_keys("kondi@kondi.com") # "kondi" is funny Indian word
        first_name.send_keys("Kondi")
        last_name.send_keys("Manam")
        city.send_keys("Hifa")
        id_like_box = driver.find_elements(By.XPATH, "id_like_box")
        id_like_box.click()
        time.sleep(3)
        sing_up_button = driver.find_elements(By.XPATH, "sing_up_button")
        sing_up_button.click()

class boeing_737_max(TestCase):
    def test_table_737_Max(self):
    # This generation of aircraft is the most popular product in the world
    # Testing receiving 737-Max generation table info

        driver.get("https://www.boeing.com/commercial/737max/")
        table_Boeing_737_Max = driver.find_elements(By.XPATH,"/html/body/div[1]"
        + "/div/div/div[3]"
        +"/div/div[2]"
        +"/div/section/div/div[2]"
        +"/div/div/div/table")

        print(table_Boeing_737_Max)
        driver.maximize_window()
        time.sleep(5)
