from com.lib.Browser import Browser

class Page:
    Browser = ""

    @staticmethod
    def initialize():
        if Page.Browser == "":
            Page.Browser = Browser()

Page.initialize()
