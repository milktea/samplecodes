#Milkteas Final Project
#From http://stoneriverelearning.com
#Course title: Python Programming for Beginners
#October 4, 2015

import statistics
student_list = {'Leonardo': [98, 76, 90],
		'Donatello': [88,83, 89],
		'Michelangelo': [88,87,89],
		'Raphael': [78,88,79]}

def enterGrade():
    student = raw_input('Name of the student:')
    grade = raw_input('Grade:')

    if student in student_list:
	student_list[student].append(grade)
    else:
	print('Student not in the list')
    
    print(student_list)
   
def removeStudent():
    student = raw_input('Student name to be removed:')
    if student in student_list:
	del student_list[student]
	print('%s is successfully removed.' % (student))
	print(student_list)
    else:
	print('Student not in the list')
   
def studentAverage():
    student = raw_input('Student Name:')
    if student in student_list:
	average = statistics.mean(student_list[student])	
	print ('%s has an average of %s' % (student, average))
    else:
	print('Student not in the list.')
def main():
    print("""
	Welcome to Grade Central
	Choose a number:
	[0] View List
	[1] Enter Student Grade
	[2] Remove A Student
	[3] Student Average Grade
	[4] Exit	
	""")

    input = raw_input('Number:')
    while True:   
	if input == '0':
	    print(student_list)
	    main()
    	if input == '1':
            enterGrade()
        elif input == '2':
	    removeStudent()
   	elif input == '3':
            studentAverage()
   	elif input == '4':
            exit()
	else:
	    print ('Invalid Number')

main()
