with open('clean data_csv.txt', encoding = 'utf8', mode = 'r') as file:
	datas = file.read().split('\n')

#remove last line break
datas.pop()

#get list of students
students = datas[1:]
for i in range(len(students)):
	students[i] = students[i].split(',')

#get number of students with same ages
number_student_with_same_age = [0,0,0,0,0,0,0,0,0,0,0]
ave_score_student_with_same_age = [0,0,0,0,0,0,0,0,0,0,0]
for student in students:
	age_of_student = 2020 - int(student[4])
	total_score = 0
	count_subject = 0
	if age_of_student>27:
		age_of_student = 27
	number_student_with_same_age[age_of_student-17] += 1
	for i in range(11):
		if student[i+5]!="-1":
			total_score += float(student[i+5])
			count_subject += 1
	ave_score = total_score/count_subject
	ave_score_student_with_same_age[age_of_student-17] += ave_score

#average score of age group of student
for i in range(len(ave_score_student_with_same_age)):
	ave_score_student_with_same_age[i] = ave_score_student_with_same_age[i]/float(number_student_with_same_age[i])

#scale-up ave_score of student with same age
for i in range(len(ave_score_student_with_same_age)):
	ave_score_student_with_same_age[i] = ave_score_student_with_same_age[i]*70000/10

#draw barchart from number of students and their ages
#https://cmdlinetips.com/2019/10/how-to-make-a-plot-with-two-different-y-axis-in-python-with-matplotlib/
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(17,28)
y = ["17","18","19","20","21","22","23","24","25","26",">27",]
fig, ax1 = plt.subplots()
plt.xticks(x,y)
ax1.bar(x, number_student_with_same_age)
ax1.plot(x, ave_score_student_with_same_age, color = 'r', marker = 'o')
ax1.set_title('Number of students at same age')
ax1.set_xlabel('Ages')
ax1.set_ylabel('Number of students')
ax1.set_ylim(0,70000)

ax2 = ax1.twinx()
ax2.tick_params('y', colors = 'r')
ax2.set_ylabel("Average score")
ax2.set_ylim(0,10)

rects = ax1.patches

# Make some labels.
for rect, label in zip(rects, number_student_with_same_age):
    height = rect.get_height()
    ax1.text(rect.get_x() + rect.get_width() / 2, height + 3, label,
            ha='center', va='bottom')

plt.show()