#! /usr/bin/env python
import sys
import os
sys.path.append(os.environ['PythonScriptRoot'])
import EnvPython
import unittest

from TextFileManager import TextFileManager

class TestTextFileManager(unittest.TestCase):
	def test_WriteLinesAndReadLines(self):
		fileName="test.txt"
		line1="line1"
		line2="line2"
		lineList=[line1, line2]
		myTextFileManager = TextFileManager(fileName);
		self.assertEqual(fileName, myTextFileManager.fileName);
		myTextFileManager.writeLines(lineList)
		#myTextFileManager.readLines()
		self.assertEqual(lineList, myTextFileManager.readLines())
		os.remove(fileName)

	def test_InsertLine(self):
		fileName="test.txt"
		line1="line1"
		line2="line2"
		line3="line3"
		lineList1=[line1, line3]
		lineList2=[line1, line2,line3]
		myTextFileManager = TextFileManager(fileName);
		self.assertEqual(fileName, myTextFileManager.fileName);
		myTextFileManager.writeLines(lineList1)
		myTextFileManager.insertLineAfter(line2,line1)
		self.assertEqual(lineList2,myTextFileManager.readLines())
		os.remove(fileName)

	def test_ReadAndWriteString(self):
		fileName1="test.txt"
		fileName2="test2.txt"
		line1="line1"
		line2="line2"
		line3="line3"
		lineList2=[line1, line2,line3]
		myTextFileManager = TextFileManager(fileName1);
		myTextFileManager2 = TextFileManager(fileName2);
		myTextFileManager.writeLines(lineList2)
		#print myTextFileManager.readString()
		myTextFileManager2.writeString(myTextFileManager.readString())
		self.assertEqual(myTextFileManager.readString(), myTextFileManager2.readString())
		os.remove(fileName1)
		os.remove(fileName2)		

	def test_InsertLineAfter(self):
		fileName="test.txt"
		line1="line1"
		line2="line2"
		line3="line3"
		lineList1=[line1, line3]
		lineList2=[line1, line2,line3]
		myTextFileManager = TextFileManager(fileName);
		myTextFileManager.writeLines(lineList1)
		myTextFileManager2 = TextFileManager(fileName);
		myTextFileManager2.insertLineBefore(line2,line3)
		self.assertEqual(lineList2,myTextFileManager2.readLines())
		os.remove(fileName)

		
suite = unittest.TestLoader().loadTestsFromTestCase(TestTextFileManager)
unittest.TextTestRunner(verbosity=2).run(suite)

