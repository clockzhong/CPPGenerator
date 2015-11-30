#! /usr/bin/env python
import sys
import os
sys.path.append(os.environ['PythonScriptRoot'])
import EnvPython
import shutil


from TextFileManager import TextFileManager

class CPPGenManager:
	def __init__(self, workingPath='.'):
		self.workingPath=workingPath
		pass
	def initialize(self):
		print "initialize the path:",self.workingPath
		if os.path.exists(self.workingPath):
			print "The directory:",self.workingPath, "exists already, we should not init it"
			return
		codePath=os.path.dirname(os.path.abspath(__file__))
		##print 'codePath is: ' + codePath
		shutil.copytree(codePath+"/template",self.workingPath)

	def genSRCString(self, className):
		sourceString=""
		sourceString+="#include \""+className+".hpp\"\n"
		sourceString+="#if DEBUG_"+className+"==0\n"
		sourceString+="    #define ELPP_DISABLE_INFO_LOGS\n"
		sourceString+="#endif\n"
		sourceString+="#include \"ClassLog.hpp\"\n"
		sourceString+="\n"

		#add constructor func
		sourceString+=className+"::"+className+"()\n"
		sourceString+="{\n"
		sourceString+="	return;\n"
		sourceString+="}\n"
		
		#add destructor func
		sourceString+=className+"::~"+className+"()\n"
		sourceString+="{\n"
		sourceString+="    return;\n"
		sourceString+="}\n"
		return sourceString
		
	def genINCString(self, className):
		sourceString=""
		sourceString+="#ifndef "+className.upper()+"_HPP\n"
		sourceString+="#define "+className.upper()+"_HPP\n"
		sourceString+="\n"

		sourceString+="class "+className+"\n"
		sourceString+="{\n"
		sourceString+="    private:\n"
		sourceString+="\n"
		sourceString+="    public:\n"
		sourceString+="    "+className+"();\n"
		sourceString+="    ~"+className+"();\n"
		sourceString+="};\n"
		sourceString+="#endif //"+className.upper()+"_HPP\n"
		return sourceString

	def genTestCodeString(self, className):
		sourceString=""
		sourceString+="#include \"gtest/gtest.h\"\n"
		sourceString+="#include \""+className+".hpp\"\n"
		sourceString+="\n"
		sourceString+="#if DEBUG_test"+className+"==0\n"
		sourceString+="    #define ELPP_DISABLE_INFO_LOGS\n"
		sourceString+="#endif\n"
		sourceString+="#include \"ClassLog.hpp\"\n"
		sourceString+="INITIALIZE_EASYLOGGINGPP\n"
		sourceString+="\n"
		sourceString+="\n"

		sourceString+="TEST(Test"+className+", basicTest)\n"
		sourceString+="{\n"
		sourceString+="    "+className+"    obj"+className+";\n"
		sourceString+="}\n"
		return sourceString


	def addClass(self, className):
		#add the src file: className.cpp in ./src/ direcotry
		srcFile=self.workingPath+"/src/"+className+".cpp"
		if os.path.isfile(srcFile):
			print srcFile, " already exists, we need not add this class:", className
			return
		srcFileManager=TextFileManager(srcFile)
		srcFileManager.writeString(self.genSRCString(className))

		##add the header file: className.hpp in ./inc/ direcotry
		incFile=self.workingPath+"/inc/"+className+".hpp"
		if os.path.isfile(incFile):
			print incFile, "already exists, we need not add this class:", className
			return
		incFileManager=TextFileManager(incFile)
		incFileManager.writeString(self.genINCString(className))

		#Added GoogleTest test case source code file:testClassName.cpp in ./tests/ directory
		testFile=self.workingPath+"/tests/test"+className+".cpp"
		if os.path.isfile(testFile):
			print testFile, " already exists, we need not add this class:", className
			return
		testFileManager=TextFileManager(testFile)
		testFileManager.writeString(self.genTestCodeString(className))

		#Add line in inc.cfg
		incCfgFile=self.workingPath+"/inc.cfg"
		incCfgFileManager=TextFileManager(incCfgFile)
		#add "export                  CLASS_LIST+=ClassName"
		insertString="export              CLASS_LIST+= "
		insertString+=className
		incCfgFileManager.insertLineBefore(insertString, "#The above CLASS_LIST definition done")
		#add "export BASH_CLASS_LIST+=ClassName"
		insertString="export BASH_CLASS_LIST+=\" "
		insertString+=className
		insertString+="\""
		incCfgFileManager.insertLineBefore(insertString, "#The above BASH_CLASS_LIST definition done")

		#add "export DEBUG_ClassName=${ENABLE_DEBUG_VALUE}"
		insertString="export DEBUG_"+className+"=${ENABLE_DEBUG_VALUE}"
		incCfgFileManager.insertLineBefore(insertString, "#The above debug flag switch done")
		#add "#export DEBUG_ClassName=1"
		insertString="#export DEBUG_"+className+"=1"
		incCfgFileManager.insertLineBefore(insertString, "#The above debug flag switch done")
		#add "export DEBUG_testClassName=${DEBUG_ClassName}"
		insertString="export DEBUG_test"+className+"=${DEBUG_"+className+"}\n"
		incCfgFileManager.insertLineBefore(insertString, "#The above debug flag switch done")


		makefileFile=self.workingPath+"/makefile"
		makefileFileManager=TextFileManager(makefileFile)
		#add "$(TESTS_PATH)/testClassName.o : $(TESTS_PATH)/testClassName.d" into ./makefile
		insertString="$(TESTS_PATH)/test"+className+".o : $(TESTS_PATH)/test"+className+".d"
		makefileFileManager.insertLineBefore(insertString, "####The above class test cases finished here")
		#add "$(TESTS_PATH)/testClassName : $(TESTS_PATH)/testClassName.o libMyClass.a" into ./makefile
		insertString="$(TESTS_PATH)/test"+className+" : $(TESTS_PATH)/test"+className+".o libMyClass.a"
		makefileFileManager.insertLineBefore(insertString, "####The above class test cases finished here")
		#add "	$(CXX)  $^ -o $@ $(CPPFLAGS)" into ./makefile
		insertString="	$(CXX)  $^ -o $@ $(CPPFLAGS)\n"
		makefileFileManager.insertLineBefore(insertString, "####The above class test cases finished here")
		


