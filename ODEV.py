from typing import KeysView
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
import pytest
from pathlib import Path
from datetime import date
from selenium.webdriver.support import expected_conditions

class Sauce_Test:


    def setup_method(self):
        self.driver=webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()
        self.folderPath=str(date.today())
        Path(self.folderPath).mkdir(exist_ok=True)

    def teardown_method(self):
        self.driver.quit()

    @pytest.mark.parametrize("username,password",[("","")])
    def test_mission_1(self, username, password):
        self.waitForElementVisible((By.ID,"user-name"))
        self.waitForElementVisible((By.ID,"password"))
        giris=self.driver.find_element(By.ID, "login-button")
        giris.click()
        hatalimesaj=self.driver.find_elements(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        self.driver.save_screenshot((f"{self.folderPath}/test_mission_1-{username}-{password}.png"))
        assert hatalimesaj.text=="Epic sadface: Password is required"
    
    @pytest.mark.parametrize("username, password", [("standard_user","")])
    def test_mission_2(self, username, password):
        self.waitForElementVisible((By.ID, "user-name"))
        kullaniciAd=self.driver.find_element(By.ID, "user-name")
        self.waitForElementVisible((By.ID, "password"))
        sifre=self.driver.find_element(By.ID, "password")
        kullaniciAd.send_keys(username)
        sifre.send_keys(password)
        giris=self.driver.find_element(By.ID, "login-button")
        giris.click() 
        self.driver.save_screenshot(f"{self.folderPath}/test_mission_2-{username}-{password}.png")
        hataligiris=self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3").text
        assert hataligiris.text == "Epic sadface: Password is required"

    @pytest.mark.parametrize("username, password", [("locked_out_user","secret_sauce")])
    def test_mission_3(self,username,password):
        self.waitForElementVisible((By.ID, "user-name"))
        kullaniciAd=self.driver.find_element(By.ID, "user-name")
        sifre=self.driver.find_element(By.ID, "password")
        giris=self.driver.find_element(By.ID, "login-button")
        
        actions = ActionChains(self.driver)
        actions.send_keys_to_element(kullaniciAd)
        actions.send_keys_to_element(sifre)
        actions.send_keys_to_element(giris, Keys.ENTER)
        actions.perform()
        sleep(4)
        hataligiris=self.driver.find_elements(By.CLASS_NAME,"error-button") 
        self.driver.save_screenshot(f"{self.folderPath}/test_mission_3-{username}-{password}.png")
        assert hataligiris.text == "Epic sadface: Sorry, this user has been locked out."
    
    @pytest.mark.parametrize("username,password",[("","")])   
    def test_mission_4(self,username,password):
        kullaniciAd=self.driver.find_element(By.ID, "user-name")
        kullaniciAd.send_keys(username)
        sifre=self.driver.find_element(By.ID, "password")
        sifre.send_keys(password)
        giris=self.driver.find_element(By.ID, "login-button").click()
        hata1=self.driver.find_elements(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]") 
        self.driver.find_element(By.ID, "login-button").click()
        hata2=self.driver.find_elements(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]")
        self.driver.save_screenshot(f"{self.folderPath}/test_mission_4.png")
        assert hata1==hata2
    
    @pytest.mark.parametrize("username,password", [("standard_user", "secret_sauce" )])
    def test_mission_5(self,username,password):
        self.waitForElementVisible((By.ID, 'user-name'))
        kullaniciAd=self.driver.find_element(By.ID, 'user-name')
        self.waitForElementVisible((By.ID, "password"))
        sifre=self.driver.find_element(By.ID, 'password')
        kullaniciAd.send_keys(username)
        sifre.send_keys(password)
        girisBtn=self.driver.find_element(By.ID, 'login-button')
        girisBtn.click()
        self.driver.save_screenshot(f"{self.folderPath}/test_mission_5.png")
        assert self.driver.current_url== "https://www.saucedemo.com/inventory.html"
    
    @pytest.mark.parametrize("username,password", [("standard_user", "secret_sauce")])
    def test_mission_6(self):
        self.waitForElementVisible((By.ID, "user-name"))
        kullaniciAd=self.driver.find_element(By.ID, "user-name")
        sifre=self.driver.find_element(By.ID, "password")
        girisBtn=self.driver.find_element(By.ID, "login-button")

        actions = ActionChains(self.driver)
        actions.send_keys_to_element(kullaniciAd, "standard_user")
        actions.send_keys_to_element(sifre, "secret_sauce")
        actions.send_keys_to_element(girisBtn, Keys.ENTER)
        actions.perform()
        sleep(3)
        urunler = self.driver.find_elements(By.CLASS_NAME, "inventory_item")
        self.driver.save_screenshot(f"{self.folderPath}/test_mission_6.png")
        assert len(urunler) == 6
    
    @pytest.mark.parametrize("username,password",[("standard_user","secret_sauce")])
    def test_Mission_Add(self,username, password):
        kullaniciAd=self.driver.find_element(By.ID, "user-name")
        kullaniciAd.send_keys("standart_user")
        sifre=self.driver.find_element(By.ID, "password")
        sifre.send_keys("secret_sauce")
        girisBtn=self.driver.find_element(By.ID, "login-button").click()
        self.waitForElementVisible((By.XPATH,"//*[@id='header_container']/div[2]/span"))
        bpackAdd = self.driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack")
        bpackAdd.click()
        self.driver.save_screenshot(f"{self.folderPath}/test_Mission_Add.png")

    
    @pytest.mark.parametrize("username, password", [("aaa", "000") , ("bbb", "111"), ("ccc", "222")])
    def test_Mission_InvalidLogin(self,username, password):
        self.waitForElementVisible((By.ID, "user-name"))
        KullaniciGiris = self.driver.find_element(By.ID, "user-name")
        KullaniciGiris.send_keys(username)
        sifreGiris = self.driver.find_element(By.ID, "password")
        sifreGiris.send_keys(password)
        Mesaj = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3/button/svg")
        self.driver.save_screenshot(f"{self.folderPath}/test_Mission_InvalidLogin-{username}-{password}.png")
        assert Mesaj.text == "Epic sadface: Username and password do not match any user in this service"
    
    def test_Mission_Preis_To_Sort(self):
        self.waitForElementVisible((By.ID, "user-name"))
        kullaniciAd=self.driver.find_element(By.ID, "user-name")
        sifre=self.driver.find_element(By.ID, "password")
        girisBtn=self.driver.find_element(By.ID, "login-button")

        actions = ActionChains(self.driver)
        actions.send_keys_to_element(kullaniciAd, "standard_user")
        actions.send_keys_to_element(sifre, "secret_sauce")
        actions.send_keys_to_element(girisBtn, Keys.ENTER)
        actions.perform()

        self.waitForElementVisible((By.CLASS_NAME, "product_sort_container"))
        To_Sort_Btn = self.driver.find_element(By.CLASS_NAME, "product_sort_container")
        To_Sort_Btn.click() 
        price_low_high=self.driver.find_element(By.XPATH,"/html/body/div/div/div/div[1]/div[2]/div/span/select/option[3]")
        price_low_high.click()
        items= self.driver.find_elements(By.CLASS_NAME, "inventory_item_price")
        result_1=sorted([float(item.text[1:]) for item in items])
        result_2 = [float(item.text[1:]) for item in items]
        self.driver.save_screenshot(f"{self.folderPath}/test_Mission_Preis_To_Sort.png")
        assert result_1 == result_2

      
    def waitForElementVisible(self,locator,timeout=10):
        WebDriverWait(self.driver,timeout).until(expected_conditions.visibility_of_element_located(locator))