from selenium import webdriver
from time import sleep
import math
import config


class InstaBot:
    def __init__(self, username, pw):
        self.driver = webdriver.Chrome()
        self.username = username
        self.driver.get("https://www.instagram.com")
        sleep(3)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
            .send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
            .send_keys(pw)
        self.driver.find_element_by_xpath('//button[@type="submit"]')\
            .click()
        sleep(4)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Ikke nu')]")\
            .click()
        sleep(4)

    def get_unfollowers(self):
        self.driver.find_element_by_xpath("//a[contains(@href,'/{}')]".format(self.username))\
            .click()  # Går til profil
        sleep(2)
        self.driver.find_element_by_xpath("//a[contains(@href,'/following')]")\
            .click()  # Åbner liste over dem du følger
        following = self._get_followings()  # Gemmer dem du følger i liste
        self.driver.find_element_by_xpath("//a[contains(@href,'/followers')]")\
            .click()
        followers = self._get_followers()
        not_following_back = [user for user in following if user not in followers]
        print(not_following_back)
        print(len(not_following_back))

    def _get_followings(self):
        sleep(2)
        total_following = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a/span').text
        num_scrolls = math.ceil(int(total_following) / 12)
        print(num_scrolls)
        # Scroller gennem liste af dem man følger
        for i in range(0, num_scrolls):
            scr1 = self.driver.find_element_by_xpath('/html/body/div[4]/div/div[2]')
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scr1)
            sleep(1)
        scroll_box = self.driver.find_element_by_xpath('/html/body/div[4]/div/div[2]')
        
        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text != '']
        # close button
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/div[2]/button")\
            .click()
        #self.driver.find_element_by_xpath('//button[@type="button"]')\
         #   .click()

        return names

    def _get_followers(self):
        sleep(2)
        total_followers = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/span').text
        num_scrolls = math.ceil(int(total_followers) / 12)
        print(num_scrolls)
        # Scroller gennem liste af dem man følger
        for i in range(0, num_scrolls):
            scr1 = self.driver.find_element_by_xpath('/html/body/div[4]/div/div[2]')
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scr1)
            sleep(1)
        scroll_box = self.driver.find_element_by_xpath('/html/body/div[4]/div/div[2]')
        
        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text != '']
        # close button
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/div[2]/button")\
            .click()
        #self.driver.find_element_by_xpath('//button[@type="button"]')\
         #   .click()

        return names


my_bot = InstaBot('rasmus.strange', config.pw)
my_bot.get_unfollowers()


## 204 - 18 pr scroll
## 239 - 16 pr scroll
## 290 - 12 pr scroll