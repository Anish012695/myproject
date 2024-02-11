def append_to_file(file_path, user_input):
    with open(file_path, 'a') as file:
        file.write(user_input + '\n')


user_string = input("Enter a string: ")


file_path = 'output.txt' 


append_to_file(file_path, user_string)

print(f"The string has been appended to {file_path}.")
