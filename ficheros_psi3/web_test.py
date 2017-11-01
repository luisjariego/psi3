# -*- coding: utf-8 -*-
#NOTE, if selenium is not installed execute pip install --user selenium
#NOTE, if loremipsum is not installed execute pip install --user loremipsum 
#NOTE: chromedriver is available at moodle. For labs use version 2.22
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, os
from collections import OrderedDict
from loremipsum import get_paragraphs, get_sentences

class onLineShopTester(unittest.TestCase):
    username    = "alumnodb"
    passwd      = "alumnodb"
    #base_url    = "https://rocky-inlet-76734.herokuapp.com/"
    base_url     = "http://127.0.0.1:8000/"
    admin_url    = base_url + "admin/"
    addCategoryPath = "shop/category/add/"
    addProductPath  = "shop/product/add/"
    catList     = ["Angels", "Butterflies", "Kokopelli"]
    productDict = {catList[0]: ["angel-tattoo-art",
                 "black-angel-tattoo",
                 "male-angel-tattoo",
                 "angel-tattoo-design-3",
                 "cute-angel-design",
                 "praying-angel-tattoo"],
                   catList[1]: ["butterflies-tattoos",
                 "butterfly-swirls-tattoo",
                 "purple-butterfly-tattoo",
                 "butterfly-stars-tat",
                 "butterfly-tattoo-3",
                 "yellow-butterfly-tattoo"],
                  catList[2]: ["dancing-kokopelli",
                 "kokopelli-dancing",
                 "kokopelli",
                 "kokopelli-music",
                 "kokopelli-tattoo-5",
                 "kokopelli-tattoo-design"]
                }
    chromeDriver = "/usr/local/bin/chromedriver"
    imagesPath = "/home/roberto/Docencia/PSI/psi_2017-18/Assigns/assign3/onLineShop/static/"

    def setUp(self):
#        self.driver = webdriver.Firefox()
        self.driver = webdriver.Chrome(self.chromeDriver)
##DO NOT CHANGE ANYTHING BELLOW THIS POINT
    def find_element_by_id(self,_id,value,waitFor=1):
        self.driver.find_element_by_id(_id).clear()
        self.driver.find_element_by_id(_id).send_keys(value)
        time.sleep(waitFor)

    def find_element_by_xpath(self,_xpath,waitFor=1):
        self.driver.find_element_by_xpath(_xpath).click()
        time.sleep(waitFor)

    def find_element_by_name(self,_name,waitFor=1):
        self.driver.find_element_by_name(_name).click()
        time.sleep(waitFor)

    def login(self,userName, passwd):
        self.driver.get(self.admin_url + "")
        self.find_element_by_id("id_username",userName)
        self.find_element_by_id("id_password",passwd)
        self.find_element_by_xpath('//*[@id="login-form"]/div[3]/input')

    def addCat(self,catName, waitFor=1):
        self.driver.get(self.admin_url + self.addCategoryPath)
        self.find_element_by_id("id_catName",catName, waitFor)
        self.find_element_by_name("_save", waitFor)

    def addProduct(self, cat, prodName, ext="jpg", price="1.1", stock="1", waitFor=1):
        self.driver.get(self.admin_url + self.addProductPath)

        select = Select(self.driver.find_element_by_id('id_category'))
        select.select_by_visible_text(cat)

        self.find_element_by_id("id_prodName",prodName, waitFor)
        imagePath =  os.path.join(self.imagesPath,cat.lower(),prodName+"."+ext)
        #self.driver.find_element_by_id("id_image").send_keys(imagePath)######
        self.find_element_by_id("id_image",imagePath)
        self.find_element_by_id("id_description",get_paragraphs(1)[0], waitFor)
        self.find_element_by_id("id_price",price, waitFor)
        self.find_element_by_id("id_stock",stock, waitFor)
        self.find_element_by_name("_save", waitFor)

    def seeHome(self, waitFor=1):
        self.driver.get(self.base_url)
        time.sleep(waitFor)

    def quit(self, waitFor=1):
        time.sleep(waitFor)
        self.driver.quit()

    def test_shop(self):
        #connect to Home
        self.seeHome(2)

        #login in
        self.login(self.username, self.passwd)

        #addCategories
        for catName in self.catList:
            self.addCat(catName,1)

        #addProducts
        counter =1
        for catName in self.catList:
            for prodName in self.productDict[catName]:
                self.addProduct(catName,prodName,
                                price = str(counter * 1.1),
                                stock = str(counter), waitFor = 0)
                counter += 1

        #connect to Home
        self.seeHome(1)

        #close browser
        self.quit(20)

if __name__ == "__main__":
    unittest.main()

