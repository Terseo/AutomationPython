import os

class Config:

	#### BROWSERS ####
	#Select the browser which you want to use for the test execution
	environment = "firefox"
	#environment = "chrome"

	#### PATHS ####
	homePath = os.environ["HOME"]
	pwd = os.environ["PYTHONPATH"]
	testPath = pwd + "/" + "projects/"

	# In the result path you can find the results of executed scripts.
	resultPath = "result/"
	# In the expected path you can find "Golden files". You can compare it with test result in case the test fails.
	expectedPath = "expected/"
	# In the import path you can save files that you want to import during the text execution.
	importPath = "import/"
	# The export path is for exporting files if it is necessary
	exportPath = "export/"
	# If one of the commands is not done (for example web element not found)
	# you can get the screenshot of that moment in this path.
	screenPath = "screenshots/"

	# Select the time(seconds) for sleeping, if your ethernet connection is slow make the time bigger
	# This variable is used for waiting some processes
	time = 5
