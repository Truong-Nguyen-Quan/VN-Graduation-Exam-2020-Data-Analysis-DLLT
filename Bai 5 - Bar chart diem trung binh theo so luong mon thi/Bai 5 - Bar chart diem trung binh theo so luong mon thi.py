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
average_scores = [0,0,0,0,0,0,0,0,0,0,0,0]
for student in students:
	count = 0
	total_score = 0
	for s in range(11):
		if student[s+5] != "-1":
			total_score += float(student[s+5])
			count += 1
	average_scores[count] += total_score
	number_exam_taken[count] += 1
for i in range(len(number_exam_taken)):
	if number_exam_taken[i] != 0:
		average_scores[i] = round(average_scores[i]/number_exam_taken[i]/i,2)
print(average_scores)

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(12)
y = np.arange(12)
plt.xticks(x,y)
plt.bar(x, average_scores)
plt.title('Average scores for number of exams taken by students')
plt.xlabel('Number of exams taken')
plt.ylabel('Average scores')

axes = plt.gca()
axes.set_ylim([0,10])

# Make some labels.
rects = axes.patches
for rect, label in zip(rects, average_scores):
    height = rect.get_height()
    axes.text(rect.get_x() + rect.get_width() / 2, height, label, ha='center', va='bottom')

plt.show()