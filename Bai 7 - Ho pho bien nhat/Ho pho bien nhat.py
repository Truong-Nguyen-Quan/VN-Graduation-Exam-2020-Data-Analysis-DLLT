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

#make list of student's surname
surname_all = []
for name in name_student:
	surname_all.append(name[0])

#find and count student's surname
surname_unique = []
surname_unique_count = []
for surname in surname_all:
	if surname not in surname_unique:
		surname_unique.append(surname)
	else:
		continue
for surname in surname_unique:
	count = 0
	for sn in surname_all:
		if sn == surname:
			count += 1
	surname_unique_count.append(count)

print(surname_unique_count)

#sort student's surname top 20
top_20_surname = []
top_20_surname_count = []
for i in range(20):
	max = 0
	for m in surname_unique_count:
		if m not in top_20_surname_count and m>max:
			max=m
		else:
			continue
	top_20_surname_count.append(max)
	top_20_surname.append(surname_unique[surname_unique_count.index(max)])

#draw bar chart
import matplotlib.pyplot as plt
import numpy as np

plt.bar(top_20_surname, top_20_surname_count)
plt.title('Top 20 student\'s surname')
plt.xlabel('Name of 20 student\'s surname')
plt.ylabel('Number of student\'s surname')

axes = plt.gca()
axes.set_ylim([0,top_20_surname_count[0]])

# Make some labels.
rects = axes.patches
for rect, label in zip(rects, top_20_surname_count):
    height = rect.get_height()
    axes.text(rect.get_x() + rect.get_width() / 2, height, label, ha='center', va='bottom')

plt.show()