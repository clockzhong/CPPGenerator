#! /usr/bin/env python
import sys
import os
#sys.path.append(os.environ['PythonScriptRoot'])
#import EnvPython
import shutil
from CPPGenManager import CPPGenManager

#print "this script is not done yet!!!!!!"
#quit()

if len(sys.argv)>1:
	projectName=sys.argv[1]
else:
	print "ERROR!!!!!: You need define your class name as the 1st parameter, e.g. \"initCPPProject.py myProjectName\""
	quit()

if len(sys.argv)>2:
	projectPath=sys.argv[2]+'/'+projectName
else:
	projectPath='./'+projectName

print "We'll create your class:"+projectName+" in the path:"+projectPath

myCPPGenManager = CPPGenManager(projectPath)

myCPPGenManager.initialize()





