class marksheet():
	subjectlist=[]

	def addMarkAndSub(self,subject,mark):

		for i in range(len(subject)):
			subject={'subname':subject[i],'mark',mark[i]}

		self.subjectlist.append(subject)

	def calculatepercentage(self):
		sum=
		for subject in subjectlist:
			sum=sum+subject['mark']

			self.percentage
