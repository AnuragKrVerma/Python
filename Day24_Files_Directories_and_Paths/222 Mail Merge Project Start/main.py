PLACEHOLDER = "[name]"
with open("Python/Day24_Files_Directories_and_Paths/222 Mail Merge Project Start/Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("/Project/Python/Day24_Files_Directories_and_Paths/222 Mail Merge Project Start/Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER,stripped_name)
    

        # with open(f"Python/Day24_Files_Directories_and_Paths/222 Mail Merge Project Start/Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as complete_letter:
        #     complete_letter.write(new_letter)

        with open(f"Python/Day24_Files_Directories_and_Paths/222 Mail Merge Project Start/Output/ReadyToSend/letter_for_{stripped_name}.txt") as letter:
            print(letter.read())