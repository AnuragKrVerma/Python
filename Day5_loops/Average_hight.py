student_heights = input("Input a list of student height\n").split()
c = 0
s = 0
for i in range(0 , len(student_heights)):
    student_heights[i] = int(student_heights[i])
    c += 1

for height in student_heights:
    s += height

print(s//c)