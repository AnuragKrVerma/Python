# 269
try:
    file = open("a_file.txt")
    a_dict = {"Key" :"value"}
    print(a_dict["key"])
except FileNotFoundError:
    file = open("Python/Day30_Errors,_Exceptions_and_JSON_Data_Improving_the_Password/a_file.txt" , "w")
    file.write("something")
except KeyError as error_message:
    print(f"The key {error_message} does not exist. ")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("file was closed")

# 270
height = float(input("Height: "))
weight =int(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3 meter")

bmi = weight/ height **2
print (bmi)
