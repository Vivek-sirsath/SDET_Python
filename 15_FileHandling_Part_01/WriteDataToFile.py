# Write data to file (abc.txt)

f = open("abc.txt", "w")

# f.write("Learning\n")
# f.write("Python is\n")
# f.write("very easy\n")

list = ["Hello everyone\n", "Good morning\n", "My name is Vivek\n"]
f.writelines(list)

f.close()

# Here, data will be overwritten. First line will be overwritten by list of lines.
# To overcome this, we need to open the file in 'Append' mode (a)

f = open("abc.txt", "a")
f.write("I am Senior Test Engineer")
