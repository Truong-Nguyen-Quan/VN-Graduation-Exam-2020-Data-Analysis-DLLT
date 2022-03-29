with open('clean data_csv.txt', encoding = 'utf8', mode = 'r') as file:
	datas = file.read().split('\n')

#remove last line break
datas.pop()

#remove header
header = datas[0]
students = datas[1:]

#change text to list
for i in range(len(students)):
	students[i] = students[i].split(',')

#make list of student's name
name_student = []
for student in students:
	name_student.append(student[1].split(' '))

#make list of student's firstname
firstname_all = []
for name in name_student:
	firstname_all.append(name[-1])

#find and count student's firstname
firstname_unique = []
firstname_unique_count = []
for firstname in firstname_all:
	if firstname not in firstname_unique:
		firstname_unique.append(firstname)
	else:
		continue
for firstname in firstname_unique:
	count = 0
	for sn in firstname_all:
		if sn == firstname:
			count += 1
	firstname_unique_count.append(count)

#sort student's firstname top 20
top_20_firstname = []
top_20_firstname_count = []
for i in range(20):
	max = 0
	for m in firstname_unique_count:
		if m not in top_20_firstname_count and m>max:
			max=m
		else:
			continue
	top_20_firstname_count.append(max)
	top_20_firstname.append(firstname_unique[firstname_unique_count.index(max)])

#draw bar chart
import matplotlib.pyplot as plt
import numpy as np

plt.bar(top_20_firstname, top_20_firstname_count)
plt.title('Top 20 student\'s firstname')
plt.xlabel('Name of 20 student\'s firstname')
plt.ylabel('Number of student\'s firstname')

axes = plt.gca()
axes.set_ylim([0,top_20_firstname_count[0]])

# Make some labels.
rects = axes.patches
for rect, label in zip(rects, top_20_firstname_count):
    height = rect.get_height()
    axes.text(rect.get_x() + rect.get_width() / 2, height, label, ha='center', va='bottom')

plt.show()