#! /usr/bin/env python
import sys
import os
#sys.path.append(os.environ['PythonScriptRoot'])
#import EnvPython
import shutil
from CPPGenManager import CPPGenManager


if len(sys.argv)>1:
	className=sys.argv[1]
else:
	print "ERROR!!!!!: You need define your class name as the 1st parameter, e.g. \"genClass.py MyFirstClass [ProjectPATH]\""
	quit()


if len(sys.argv)>2:
	projectPath=sys.argv[2]
else:
	projectPath='.'

print "We'll create your class:"+className+" in the path:"+projectPath

myCPPGenManager = CPPGenManager(projectPath)

myCPPGenManager.addClass(className)


