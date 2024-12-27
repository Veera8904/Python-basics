
input_names = ("veera","vijay","raju")


names_list = input_names.split(',')


names_list[-2] = "ajay"

last_element = names_list.pop()
names_list.insert(1, last_element)

names_list.append("NewName")
names_list.pop(0)

output_names = ','.join(names_list)
print(output_names)
