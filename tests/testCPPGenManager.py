#! /usr/bin/env python
import sys
import os
sys.path.append(os.environ['PythonScriptRoot'])
import EnvPython
import unittest
import shutil

from CPPGenManager import CPPGenManager

class TestCPPGenManager(unittest.TestCase):
	def test_BasicInit(self):
		myCPPGenManager = CPPGenManager("./temp")
		myCPPGenManager.initialize()
		#print myCPPGenManager.genSRCString("myFirstClass")
		#print myCPPGenManager.genINCString("myFirstClass")
		#print myCPPGenManager.genTestCodeString("MyFirstClass")
		myCPPGenManager.addClass("MyFirstClass")
		myCPPGenManager.addClass("MyFirstClass2")
		shutil.rmtree(myCPPGenManager.workingPath)
		
		
suite = unittest.TestLoader().loadTestsFromTestCase(TestCPPGenManager)
unittest.TextTestRunner(verbosity=2).run(suite)

