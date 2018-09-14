import csv

def clear():
	f = open('Banana.csv', "w+")
	f.close()


def add():
		
	while (True):
		arr = []
		csvfile = open('Banana.csv','a+')
		ID_No = raw_input('idnum:')
		FirstName = raw_input('FirstName:')
		LastName = raw_input('LastName:')
		Gender = raw_input('Gender:')
		Course = raw_input('Course:')
		Year = raw_input('Year:')

		arr.append(ID_No + ',' + FirstName + ',' + LastName + ',' + Gender + ',' + Course + ',' + Year + '\n')
		csvfile.writelines(arr)
		choice = raw_input('add a student? (yes/no): ')
		if choice == 'yes':
			pass
		elif choice == 'no':
			break

def  view():
	file = open('Banana.csv')
	for line in file:
		print line

def delete():
	arr = []
	nput = raw_input('enter idnum: ')
	file = open('Banana.csv', 'r')
	for line in file:
		x = line.split(',')
		idnum = x[0]
		if idnum == nput:
			print "DELETED"
		else:

			arr.append(line)
			print line

		delete_dis = open('Banana.csv','w')
		delete_dis.writelines(arr)
		delete_dis.close()


def update():
	nput = raw_input("enter idnum: ")
	file = open('Banana.csv', 'r')
	arr = []
	for line in file:
		x = line.split(',')
		idnum = x[0]
		if idnum == nput:
			print "result: "+line
			edit_dis = raw_input("enter what to change: \n-firstname\n-lastname\n-gender\n-course\n-year\n\n")
			if edit_dis == "firstname":
				Edit_FName == raw_input("enter changes: ")
				arr.append(x[0]+','+Edit_FName+','+x[2]+','+x[3]+','+x[4]+','+x[5]+'\n')
			elif edit_dis == "lastname":
				Edit_LName == raw_input("enter changes: ")
				arr.append(x[0]+','+x[1]+','+Edit_LName+','+x[3]+','+x[4]+','+x[5]+'\n')
			elif edit_dis == "Gender":
				Edit_GName = raw_input('enter changes: ')
				arr.append(x[0]+','+x[1]+','+x[2]+','+Edit_GName+','+x[4]+','+x[5]+'\n')
			elif edit_dis == "Course":
				Edit_CName == raw_input('enter changes: ')
				arr.append(x[0]+','+x[1]+','+x[2]+','+x[3]+','+Edit_CName+','+x[5]+'\n')
			elif edit_dis == "Year":
				Edit_YName = raw_input('enter changes: ')
				arr.append(x[0]+','+x[1]+','+x[2]+','+x[3]+','+x[4]+','+Edit_YName+'\n')

		else:

			arr.append(line)
		file.close()
		delete_dis = open('Banana.csv','w')
		delete_dis.writelines(arr)
		delete_dis.close()
				

while (True):
	choice = raw_input('\n\n-add\n-update\n-delete\n-view\n-exit\n\n')
	if choice == 'add':
		add()
	elif choice == 'delete':
		delete()
	elif choice == 'update':
		update()
	elif choice == 'view':
		view()
	elif choice == 'exit':
		break

		


