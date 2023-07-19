
new_member = input("Add a new member: ")

file = open("members.txt","r")
content = file.readlines()
file.close()

file_write = open("members.txt", "w")
content.append(new_member)
file_write.writelines(content)