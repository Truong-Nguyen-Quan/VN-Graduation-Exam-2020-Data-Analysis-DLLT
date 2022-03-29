with open("clean data_csv.txt", encoding = "utf8", mode = "r") as file:
	datas = file.read().split("\n")

#remove last new line
datas.pop()

#get students list
students = datas[1:]

#change each student text to list
for i in range(len(students)):
	students[i] = students[i].split(",")

#count number of exams taken by students
number_exam_taken = [0,0,0,0,0,0,0,0,0,0,0,0]
for student in students:
	count = 0
	for s in range(11):
		if student[s+5] != "-1":
			count += 1
	number_exam_taken[count] += 1

import matplotlib.pyplot as plt

mylabels = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]
figure, axis = plt.subplots()
axis.pie(number_exam_taken, labels=mylabels, autopct='%1.1f%%')
plt.title("Percentages of exams taken by students")

plt.show() 