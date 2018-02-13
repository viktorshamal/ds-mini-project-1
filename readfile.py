
class countfile:
	def __init__(self, n):
		
		self.dictonary = {}
		self.path1 = ""
		self.path2 = ""
		self.path3 = ""
		self.outfile1 = open("outfile1.txt","w+")
		
	def setpath1(self, path):
		
		self.path1 = path
		
	
	def readfile1(self):
		
		text = open(self._path1,'r')
		for line in text.readlines():
			for words in line():
				self.dictonary[words] = self._dictonary.get(words,0) + 1
		text.close()
		
	def writeout1(self):
		
		self.outfile1 = open("outfile1.txt","w+")
		for word in self.dictionary:
			self.outfile1.write("" + word + self.dictionary[word])