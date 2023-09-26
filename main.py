from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
SIMILAR_ACCOUNT = "berkaykarabas"
EMAIL = "USERNAME OR EMAIL"
PASSWORD = "PASSWORD"
chrome_options= webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

class InstaFollower:

    def __init__(self,options):
        self.driver = webdriver.Chrome(options=options)

    def login(self):

        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)

        username = self.driver.find_element(By.NAME,"username")

        password = self.driver.find_element(By.NAME,"password")

        username.send_keys(EMAIL)
        password.send_keys(PASSWORD)

        time.sleep(2)
        password.send_keys(Keys.ENTER)

    def find_followers(self):
        time.sleep(5)
        self.driver.get(url=f"https://www.instagram.com/{SIMILAR_ACCOUNT}/")
        time.sleep(5)
        followers = self.driver.find_element(By.CSS_SELECTOR,value='div ul li a')
        followers.click()

        time.sleep(2)
        modal = self.driver.find_element(By.XPATH,'/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]')
        for i in range(50):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)
    def follow(self):

        follower_buttons=self.driver.find_elements(By.CSS_SELECTOR,"div button")
        for button in follower_buttons:
            if button.text == "Takiptesin" or button.text == "" or button.text == "İstek Gönderildi":
                pass
            else:
                try:
                    button.click()
                    time.sleep(1)
                except ElementClickInterceptedException:
                    cancel_button = self.driver.find_element(By.XPATH,'/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div/div/button[2]')
                    cancel_button.click()

bot = InstaFollower(chrome_options)
bot.login()

bot.find_followers()
bot.follow()

