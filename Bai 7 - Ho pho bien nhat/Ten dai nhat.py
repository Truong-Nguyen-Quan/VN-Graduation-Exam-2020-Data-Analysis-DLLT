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
	name_student.append(student[1])

#find longest student's name
longest_name_len = [0]
longest_name = []
for name in name_student:
	if len(name) < longest_name_len[0]:
		continue
	if len(name) > longest_name_len[0]:
		longest_name_len.clear()
		longest_name.clear()
	longest_name_len.append(len(name)) 
	longest_name.append(name)
print(longest_name_len)
print(longest_name)
# print(name_student)