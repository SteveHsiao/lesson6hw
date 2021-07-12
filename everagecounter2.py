num_of_student = int(input("Please enter the 'num' of the student:"))
name_and_score_list = []


for i in range(num_of_student):
    name = input("Please enter the 'name' of the student:")
    name_and_score_list.append(name)
    score = int(input("Please enter the 'score' of the student:"))
    name_and_score_list.append(score)
    

max = 0
max_name = ""
for a in range(1,2*num_of_student + 1,2):
    if name_and_score_list[a] > max:
        max = name_and_score_list[a]
        max_name = name_and_score_list[a-1]


min = 101
min_name = ""
for b in range(1,2*num_of_student + 1,2):
    if name_and_score_list[b] < min:
        min = name_and_score_list[b]
        min_name = name_and_score_list[b-1]
        


sum = 0
for c in range(1,2*num_of_student + 1,2):
    total = name_and_score_list[c]
    sum += total




print("The highest score is :%s %d" % (max_name,max))
print("The lowest score is :%s %d" % (min_name,min))
print("The everage is :", sum/num_of_student)
    
    
     





