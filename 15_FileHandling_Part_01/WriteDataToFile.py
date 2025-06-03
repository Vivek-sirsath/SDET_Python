# Write data to file (pqr.txt)

f = open("pqr.txt", "w")

# f.write("Learning\n")
# f.write("Python is\n")
# f.write("very easy\n")

list = ["Hello everyone\n", "Good morning\n", "My name is Vivek\n"]
f.writelines(list)

f.close()

# writelines() method writes the 'list of lines'
# Here, data will be overwritten using writelines() method. First line will be overwritten by list of lines.
# Here 'Learning Python is very easy' these lines are overwritten by 'Hello everyone.....'
# To overcome this problem, we need to open the file in 'Append' mode (a)

# APPEND MODE :

f = open("pqr.txt", "a")
f.write("I am Senior Test Engineer")
