student_heights = input("Input a list of student height\n").split()
for i in range(0 , len(student_heights)):
    student_heights[i] = int(student_heights[i])

max = student_heights[0]
min = student_heights[0]

for i in range(0 , len(student_heights)):
    if max < student_heights[i]:
        max = student_heights[i]
    elif min > student_heights[i]:
        min = student_heights[i]

print(max , min)