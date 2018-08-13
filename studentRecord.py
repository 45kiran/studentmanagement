from Books import Books
class student:

	def __init__(self,name,address):
		self.name=name
		self.address=address

	def getName(self):
		return self.name
	def getAddress=address
	count=int(Input("Enter the number of student:"))
	for i in range(count)
		name=input("Enter the name":)
		address=input("input the address of the student:")
		student=student(name,address)
		studentList.append(student)

studentmap=map(lambda stud:stud.getName()+""+stud.getAddress(),studentList)
print(List(studentmap))

book=book(1,"Yuvraj paudel","python programming","2014")
book.showAuthorname()

