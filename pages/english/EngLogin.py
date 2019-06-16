from EngConfig import EngConfig
from com.pages.Page import Page
from com.lib.Config import Config
from com.lib.Url import Url
import time

class EngLogin(Page):
	def open(self):
		self.Browser.goTo(Url.EngBaseUrl + Url.EngUrl + Url.EngLoginUrl)

	def Login(self):
		driver = self.Browser.getDriver()
		emailField = driver.find_element_by_id("frm_email")
		emailField.clear()
		emailField.send_keys(EngConfig.userName)
		time.sleep(Config.time)
		passwordField = driver.find_element_by_id("frm_pswd")
		passwordField.clear()
		passwordField.send_keys(EngConfig.password)
		time.sleep(Config.time)
		driver.find_element_by_id("button").click()
		time.sleep(Config.time)