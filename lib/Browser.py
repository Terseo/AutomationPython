from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoAlertPresentException
from com.lib.Url import Url
from com.lib.Config import Config
import os, sys, time

class Browser:
	driver = ""

	def __init__(self):
		if Config.environment is "firefox":
			self.driver = webdriver.Firefox(executable_path=r'/home/mate/Downloads/geckodriver')
		elif Config.environment is "chrome":
			self.driver = webdriver.Chrome()
		else: 
			print "Please specify the browser in Config.py file"
		self.verificationErrors = []
		self.accept_next_alert = True

	def goTo(self, url):
		self.driver.get(url)

	def getDriver(self):
		return self.driver

	def waitForElementByID(self, elementId):
		WebDriverWait(self.driver, Config.time).until(EC.visibility_of_element_located((By.ID, elementId)))

	def quit(self):
		self.driver.quit()
