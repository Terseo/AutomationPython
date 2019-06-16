from com.pages.Page import Page
from com.lib.Url import Url
from EngConfig import EngConfig
from EngLogin import EngLogin

class Imports(Page):
	def open(self):
		login = EngLogin()
		login.open()
		login.Login()
		self.Browser.goTo(Url.EngBaseUrl + Url.EngUrl + Url.importsUrl)