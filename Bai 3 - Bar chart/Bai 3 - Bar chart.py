with open("clean data_csv.txt", mode="r", encoding="utf8") as file:
	datas = file.read().split("\n")

#remove last new line
datas.pop()

#count number of students not taking the exam
not_take_exam_student_list = [0,0,0,0,0,0,0,0,0,0,0]
for i in range(len(datas)):
	datas[i] = datas[i].split(",")
for data in datas:
	for i in range(len(data)):
		if (data[i]=="-1"):
			not_take_exam_student_list[i-5] += 1

#calculate total students
total_students = len(datas)-1

#get subject list
subject_list = datas[0][5:]

#calculate percentage
percentage_list = []
for not_take_exam_student in not_take_exam_student_list:
	percentage_list.append(round(not_take_exam_student/total_students*100,2))

import matplotlib.pyplot as plt

plt.bar(subject_list, percentage_list)
plt.title('Number of students not taking the exam')
plt.xlabel('Subjects')
plt.ylabel('Percentage')

axes = plt.gca()
axes.set_ylim([0,100])

rects = axes.patches

# Make some labels.
for rect, label in zip(rects, not_take_exam_student_list):
    height = rect.get_height()
    axes.text(rect.get_x() + rect.get_width() / 2, height + 3, label,
            ha='center', va='bottom')

plt.show()