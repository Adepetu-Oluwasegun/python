# either relative, absolute path of file or name of file and also the mode in which you want to use the file can be read "r", write "w", append "a" and read and write "r+"
employee_file = open("employees.txt", "r")

print(employee_file.readable())

print(employee_file.read())

print(employee_file.readline())

print(employee_file.readlines())

employee_file.close()

employee_file = open("employees.txt", "a")

employee_file.write("\nderozan - jump shooter")

employee_file.close()