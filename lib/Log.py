from com.lib.Config import Config
import os, sys, filecmp, time, traceback

class Log():
 
	outputFile = ""
	project = ""

	def testCase(self, description, object, case):
		print "\n\nTest case" + " " + description
		try:
			for steps in case:
				eval('object.'+ steps)
		except Exception as error:
			print "***Test case '" + description + "' Failed"
			self.checkAndReportTestErrors(object.driver, object.project)
			object.driver.refresh()

	def saveTestResultToAnOutputFile(self, fileName, project):
		self.outputFile = open(Config.testPath + project + Config.resultPath + fileName, 'w')
		sys.stdout = self.outputFile
		sys.stderr = self.outputFile

	def closeTestResultOutputFile(self):
		self.outputFile.close()
		sys.stdout = sys.__stdout__
		sys.stderr = sys.__stderr__

	def compareActualAndExpectedResults(self, fileName, project):
		expectedResult = Config.testPath + project + Config.expectedPath + fileName
		actualResult = Config.testPath + project + Config.resultPath + fileName
		checkResult = filecmp.cmp(expectedResult, actualResult)
		if checkResult == True:
			os.remove(actualResult)
			print "Test passed successfully"
		else:
			print "***Test finished with failures, compare '" + expectedResult + "' and '" + actualResult + "' files to find out the reasons of the failure"
	
	def validateTestResult(self, outputFile, project):
		self.closeTestResultOutputFile()
		self.compareActualAndExpectedResults(outputFile, project)

	def takeScreenshot(self, driver, project, name = ""):
		currentDate = (time.strftime("%d-%m-%Y_"))
		currentTime = (time.strftime("%H:%M:%S"))
		screenshotName = (Config.testPath + project + Config.screenPath + currentDate + currentTime + name + ".png")
		driver.get_screenshot_as_file(screenshotName)
		print "check screenshot '" + screenshotName + "' to reproduce the issue"

	def checkAndReportTestErrors(self, driver, project):
		print traceback.format_exc()
		self.takeScreenshot(driver, project)