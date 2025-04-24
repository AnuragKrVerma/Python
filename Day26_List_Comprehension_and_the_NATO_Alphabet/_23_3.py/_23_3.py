with open("Python/Day26_List_Comprehension_and_the_NATO_Alphabet/_23_3.py/file1.txt") as file1:
    file1_data = file1.readlines()
with open("Python/Day26_List_Comprehension_and_the_NATO_Alphabet/_23_3.py/file2.txt") as file2:
    file2_data = file2.readlines()

result = [int(num) for num in file1_data if num in file2_data]
print(result)