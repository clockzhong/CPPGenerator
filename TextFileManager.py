#! /usr/bin/env python
import os.path

class TextFileManager:
	def __init__(self, fileName):
		self.fileName=fileName
		if (os.path.isfile(fileName)):
			pass
			#print "we have file:", fileName
		else:
			pass
			#print "we have no file:", fileName
		#self.fileHandle=open(fileName, 'w+')
		#self.fileHandle.close()
	def writeLines(self,stringList):
		self.fileHandle=open(self.fileName, 'w+')
		for lineItem in stringList:
			self.fileHandle.write(lineItem+ os.linesep)
		self.fileHandle.close()
	def readLines(self):
		result=list()
		self.fileHandle=open(self.fileName, 'r')
		lineList=self.fileHandle.readlines();
		self.fileHandle.close()
		for line in lineList:
			line=line.rstrip('\n')
			result.append(line)
		return result
	def writeString(self,inputString):
		self.fileHandle=open(self.fileName, 'w+')
		self.fileHandle.write(inputString)
		self.fileHandle.close()
	def readString(self):
		result=""
		self.fileHandle=open(self.fileName, 'r')
		lineList=self.fileHandle.readlines();
		self.fileHandle.close()
		for line in lineList:
			result+=line
		return result



	def insertLineAfter(self, insertedLine, preLine):
		bSearched=False
		newLineList=[]
		lineList=self.readLines()
		for line in lineList:
			if bSearched:
				newLineList.append(insertedLine)
				bSearched=False
			if preLine==line:
				bSearched=True
			newLineList.append(line)
		self.writeLines(newLineList)

	def insertLineBefore(self, insertedLine, suffixLine):
		newLineList=[]
		lineList=self.readLines()
		for line in lineList:
			if suffixLine==line:
				newLineList.append(insertedLine)
			newLineList.append(line)
		self.writeLines(newLineList)
		

		
