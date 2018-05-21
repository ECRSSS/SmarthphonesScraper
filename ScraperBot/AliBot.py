from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from ScraperBot.Item import Item
import re


class AliBot:

    def run(self,modelName):

        driver = self.init()
        listItems = self.findFirst(modelName)
        items=self.grabItemsFromPage(listItems, modelName)
        return items

    def doubleSort(self):
        element2 = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"div.n-sort-filter>div.n-sort-lists>div.narrow-down-bg:last-child")))
        element2.click()
        element2 = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"div.n-sort-filter>div.n-sort-lists>div.narrow-down-bg:last-child")))
        element2.click()

    # Граббинг данных из итемов
    def grabItemsFromPage(self, listItems, modelName):
        itemsDom = listItems.find_elements_by_css_selector("li.list-item")
        items = []
        for item in itemsDom:

            title = item.find_element_by_css_selector("div.info > h3 > a").get_attribute("title")
            title = title.lower()
            shopName=self.grabShopName(item)

            if modelName.lower() in title:
                # парсинг цены
                price = item.find_element_by_css_selector("div.info > span.price > span.value").text
                price = price.replace(" ", "")
                price = price.replace(",",".")
                rs = re.findall('[0-9]+[.]*[0-9]*', price)

                # парсинг url
                url = item.find_element_by_css_selector("div.pic > a.picRind.history-item").get_attribute("href")

                items.append(Item(modelName, url, rs,shopName))
        return items

    def grabShopName(self,elm):
        return elm.find_element_by_css_selector("div.info-more>div.store-name-chat>div.store-name.util-clearfix>a").get_attribute("title")








    #переход на страницу и парсинг списка итемов первой страницы
    def findFirst(self, modelName):
        resultSearch = self.driver.find_element_by_css_selector(
            'input#ipt-kwd.ui-textfield.ui-textfield-system.keyword-search-input')
        resultSearch.click()
        resultSearch.send_keys(modelName + Keys.ENTER)
        self.doubleSort()
        listItems = self.driver.find_element_by_css_selector("ul#hs-below-list-items")
        return listItems

    #инициализация
    def init(self):

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--proxy-server=159.224.65.253:3128')

        self.driver = webdriver.Chrome('E:\chromedriver_win32 (1)\chromedriver.exe',chrome_options=chrome_options)
        self.wait=WebDriverWait(self.driver,10)
        self.driver.get(
            'https://ru.aliexpress.com/af/category/202001195.html?g=y&d=n&origin=n&blanktest=0&spm=a2g0v.search0101.1.34.2c185d8bm7B9FY&jump=afs&CatId=202001195&catName=mobile-phones&isViewCP=y')
        self.driver.maximize_window()

    def close(self):
        self.driver.close()

